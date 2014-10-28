# -*- coding: utf-8 -*-
##############################################################################
#
#    Odoo, Open Source Management Solution
#    Copyright (C) 2014 Pharmadus i+D+I (<http://www.pharmadus.com>)
#    $Marcos Ybarra<marcos.ybarra@pharmadus.com>$
#    Copyright (C) 2011 NovaPoint Group LLC (<http://www.novapointgroup.com>)
#    Copyright (C) 2004-2010 OpenERP SA (<http://www.openerp.com>)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>
#
##############################################################################

{
    'name' : 'Promotions for Odoo',
    'version' : '0.1',
    'author': 'Pharmadus I+D+i',
    'website': 'www.pharmadus.com',
    'category' : 'Generic Modules/Sales & Purchases',
    'depends' : ["base","sale","stock"],
    'description': """
    Promotions on Sale Order for Odoo
    = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
    Features:
    1. Promotions based on conditions and coupons
    2. Web services API compliance
    
    Credits:
        Migrated to V8 from Promotions for OpenERP
    """,
    'data': [
        'security/ir.model.access.csv',
        'views/rule.xml',
        'views/sale.xml',
                ],
    'installable': True,
    'auto_install': False,
}
