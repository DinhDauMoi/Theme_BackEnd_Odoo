# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2016-Today Geminate Consultancy Services (<http://geminatecs.com>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
from odoo import fields, http, _
from odoo.http import request

class Company(http.Controller):
    @http.route('/get/company/address', type='json', auth="public",website=True)
    def rescofig_setting(self):
        if request.env.company:
            company = request.env.company
            street = company.street if company.street else ' '  
            street2 = company.street2 if company.street2 else ' '  
            city = company.city if company.city else ' '  
            state = company.state_id.name if company.state_id else ' ' 
            country = company.country_id.name if company.country_id else ' ' 
            code = company.zip if company.zip else ' ' 
            address =  street + ' ' + street2 + ' ' + city + ' ' + state + ' ' + country + ' ' + code
            return {'address':address,'company_name':company.name,'google_api':company.google_api}
        else:
            return False


    @http.route('/test/index', type='http',auth='public', csrf=False,website=True)
    def test_index(self):

        temp_id =  request.env['ir.module.module'].browse(486)
        return request.render("geminate_ecommerce_theme.test_index1" ,{'temp_id':temp_id})