# -*- coding: utf-8 -*-
##############################################################################
#
#    Copyright (C) 2015 Pexego All Rights Reserved
#    $Jesús Ventosinos Mayor <jesus@pexego.es>$
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published
#    by the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
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

{
    'name': 'Product analysis',
    'version': '8.0.2.0.0',
    'category': 'product',
    'description': """""",
    'author': 'Pexego',
    'website': '',
    "depends": ['product', 'lot_states', 'quality_protocol_report',
                'stock_reception', 'product_spec', 'custom_views', 'web_sheet_full_width_selective', 'lot_states'],
    "data": ['views/product_view.xml', 'views/stock_view.xml', 'views/product_analysis_view.xml',
             'views/lot_analysis_sheet_report.xml',
             'views/lot_analysis_certificate_report.xml',
             'views/stock_lot_analysis_report.xml', 'views/assets.xml',
             'security/ir.model.access.csv'],
    "installable": True
}
