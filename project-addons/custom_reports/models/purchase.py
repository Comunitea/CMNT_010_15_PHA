# -*- coding: utf-8 -*-
# © 2017 Pharmadus I.T.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from openerp import models, fields, api


class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'

    product_supplier_reference = fields.Char(compute='_get_supplier_reference')

    @api.one
    def _get_supplier_reference(self):
        if self.product_id.supplier_ids:
            self.product_supplier_reference = self.product_id.supplier_ids.\
                filtered(lambda r: r.name == self.order_id.partner_id).product_code
