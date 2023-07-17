# -*- coding: utf-8 -*-
import logging

from odoo import http, tools
from odoo.addons.http_routing.models.ir_http import slug, unslug

# from odoo.exceptions import MissingError
from odoo.http import request

_logger = logging.getLogger(__name__)


class Enterprise(http.Controller):
    _partner_per_page = 12

    def rewrite_tag_path(self, tag, current_tag_ids, current_path):
        path: str = request.httprequest.full_path
        path = path.replace("?", "").split("/page/")[0].split("/tag/")[0]

        tag_slug = slug(tag)

        if current_tag_ids:
            if tag not in current_tag_ids:
                tag_slug = ",".join((current_path, tag_slug))
            else:
                tag_slug = ",".join([slug(t) for t in current_tag_ids if tag != t])

        if tag_slug:
            return f"{path}/tag/{tag_slug}"

        return path

    def tags_list(self, tags):
        PartnerCategory = request.env["res.partner.category"]
        tags_list = []

        current_tag_ids = set()
        if tags:
            for tag in tags.split(","):
                _, _id = unslug(tag)
                if _id:
                    current_tag_ids.add(_id)

        domain = [("active", "=", True), ("id", "in", list(current_tag_ids))]
        if current_tag_ids:
            domain += [("id", "in", list(current_tag_ids))]

        valid_current_ids = PartnerCategory.sudo().search(domain)

        _logger.info(f"Checked: {valid_current_ids}")

        for tag in PartnerCategory.sudo().search([("active", "=", True)]):
            current_path_string = ",".join([slug(v) for v in valid_current_ids])
            t = {
                "id": tag.id,
                "name": tag.name,
                "selected": True if tag.id in current_tag_ids else False,
                "url": self.rewrite_tag_path(
                    tag, valid_current_ids, current_path_string
                ),
            }

            tags_list.append(t)

        return tags_list, valid_current_ids.ids

    def _prepare_data_value(self, page=1, tags=None):
        Partner = request.env["res.partner"]

        partner_domain = [
          ('is_coaching','=',True)
        ]

        tag_list, _ids = self.tags_list(tags)
        if _ids:
            partner_domain.append(("category_id", "in", _ids))

        partners = Partner.sudo().search(
            partner_domain,
            limit=self._partner_per_page,
            offset=(page - 1) * self._partner_per_page,
        )

        total = Partner.sudo().search_count(partner_domain)

        pager = tools.lazy(
            lambda: request.website.pager(
                url=request.httprequest.path.partition("/page/")[0],
                total=total,
                page=page,
                step=self._partner_per_page,
            )
        )

        return {
            "partners": partners,
            "pager": pager,
            "tags": tag_list,
        }

    @http.route(
        [
            "/organization",
            "/organization/page/<int:page>",
            "/organization/tag/<string:tag>",
            "/organization/tag/<string:tag>/page/<int:page>",
        ],
        type="http",
        auth="public",
        website=True,
    )
    def enterprise(self, tag=None, page=1, **kw):
        _logger.info(f"Echo -> {tag}")
        value = self._prepare_data_value(page, tag)
        return request.render("couching_partner.index", value)
