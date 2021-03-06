# -*- coding: utf-8 -*-
##############################################################################
#
#    Copyright (C) 2014 Pexego Sistemas Informáticos All Rights Reserved
#    $Omar Castiñeira Saavedra <omar@pexego.es>$
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
    'name': "Quality protocols reports",
    'version': '1.2',
    'category': 'quality',
    'description': """Allow to print quality protocols reports
                      -This module requires the installation of PhantomJS http://phantomjs.org/download.html
                      -After installation must add a parameter with key=addons_path and the absolute path of project_addons folder""",
    'author': 'Comunitea, Pharmadus I.T.',
    'website': 'www.comunitea.com, www.pharmadus.com',
    "depends": ['base',
                'survey',
                'stock',
                'web',
                'mrp',
                'mrp_operations',
                'mrp_hoard',
                'lot_states',
                'product_gtin_codes',
                'mrp_automatic_lot',
                'mrp_location_dest',
                'product_spec',
                'stock_available_ph',
                'quality_management_menu'],
    "data": ['data/report_paperformat.xml',
             'data/remove_old_translations.xml',
             'data/ir_actions_server.xml',
             'data/configuration.xml',
             'views/mrp_label_report.xml',
             'wizard/duplicate_protocol_wizard.xml',
             'wizard/print_protocol_view.xml',
             'wizard/print_mrp_labels_view.xml',
             'wizard/quality_print_all_protocols_view.xml',
             'views/quality_protocol_report_view.xml',
             'views/product_view.xml',
             'views/production_view.xml',
             'views/stock_view.xml',
             'views/mrp_view.xml',
             'views/survey_view.xml',
             'views/mrp_workcenter_line_view.xml',
             'views/mrp_indicators_base_report_view.xml',
             'views/protocol_type_view.xml',
             'security/ir.model.access.csv',
             'security/quality_protocol_report_security.xml'],
    "installable": True
}
