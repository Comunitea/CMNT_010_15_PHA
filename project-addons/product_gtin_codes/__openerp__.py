# -*- coding: utf-8 -*-
# © 2017 Pharmadus I.T.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    'name': 'GTIN product codes',
    'version': '1.0',
    'category': 'stock',
    'summary' : 'Add a sheet on product form to generate product GTIN 12, 13 and 14 codes',
    'description': " //static/description/index.html//",
    'icon': '//static/description/icon.png//',
    'author': 'Pharmadus I.T.',
    'website': 'www.pharmadus.com',
    'depends': [
        'product',
    ],
    'data': [
        'views/product_view.xml',
        'security/ir.model.access.csv',
    ],
    'installable': True
}
