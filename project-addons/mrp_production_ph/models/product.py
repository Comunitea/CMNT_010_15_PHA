# -*- coding: utf-8 -*-
# © 2019 Pharmadus I.T.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    production_warning = fields.Char()


class ProductCategory(models.Model):
    _inherit = 'product.category'

    lot_assignment_by_quality_dept = fields.Boolean(default=False)