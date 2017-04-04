# -*- coding: utf-8 -*-
# © 2017 Pharmadus I.T.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from openerp import models, fields, api


class ProductStockUnsafety(models.Model):
    _inherit = 'product.stock.unsafety'

    default_code = fields.Char(related='product_id.default_code')
    qty_available = fields.Float(related='product_id.qty_available')
    virtual_available = fields.Float(related='product_id.virtual_available')
    virtual_conservative = fields.Float(related='product_id.virtual_conservative')
    production_planning_qty = fields.Float(related='product_id.production_planning_qty')
    production_qty = fields.Float(related='product_id.production_qty')
    out_of_existences = fields.Float(related='product_id.out_of_existences')
    real_incoming_qty = fields.Float(related='product_id.real_incoming_qty')
    stock_by_day_i = fields.Float(string='Stock by day [I]', digits=(16, 2),
                                  readonly=True)
    stock_by_day_p = fields.Float(string='Stock by day [P]', digits=(16, 2),
                                  readonly=True)
    stock_by_day_p_ind_min = fields.Float(string='Minimum stock by day [P] (indirect)',
                                          digits=(16, 2), readonly=True)
    stock_by_day_i_total = fields.Float(
        string='Stock by day [I] (direct+indirect)', digits=(16, 2),
        readonly=True)
    stock_by_day_p_total = fields.Float(
        string='Stock by day [P] (direct+indirect)', digits=(16, 2),
        readonly=True)
    uom_id = fields.Many2one(related='product_id.uom_id')
    bom_member = fields.Boolean(related='product_id.bom_member')
    has_bom = fields.Boolean(related='product_id.has_bom')

    @api.model
    def create(self, vals):
        res = super(ProductStockUnsafety, self).create(vals)
        res.write({
            'stock_by_day_i': res.product_id.stock_by_day_i,
            'stock_by_day_p': res.product_id.stock_by_day_p,
            'stock_by_day_i_total': res.product_id.stock_by_day_i_total,
            'stock_by_day_p_total': res.product_id.stock_by_day_p_total
        })
        return res

    @api.multi
    def create_production_planning_order(self):
        return self.product_id.create_production_planning_order()
