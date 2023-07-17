# -*- coding: utf-8 -*-
{
    "name": "Couching",
    "summary": """Couching.""",
    "description": """
        Couching
    """,
    "author": "T4Tek Team",
    "website": "https://couching.t4site.tk",
    "category": "Couch/Partner",
    "version": "16.0.1.0.0",
    "depends": [
        "website",
        "website_partner",
    ],
    "data": [
        "data/data.xml",
        "views/templates.xml",
        "views/view.xml",
    ],
    "assets": {
        "web.assets_frontend": {
            "couching_partner/static/src/**/*",
        },
    },
    "license": "LGPL-3",
}  # type: ignore
