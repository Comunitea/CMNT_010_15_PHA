# -*- coding: utf-8 -*-
# © 2019 Pharmadus I.T.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, api, _


class DeactivateProduct(models.TransientModel):
    _name = 'deactivate.product'

    @api.multi
    def deactivate_product(self):
        if self.env.context.get('active_model') == 'product.product' and \
                self.env.context.get('active_ids'):
            # Models to deactivate/remove product reference
            quality_limits = self.env['product.quality.limits']
            pricelist_items = self.env['product.pricelist.item']
            stock_warehouse_op = self.env['stock.warehouse.orderpoint']
            mrp_bom_line = self.env['mrp.bom.line']
            mrp_bom = self.env['mrp.bom']
            protocol_link = self.env['product.protocol.link']

            product_ids = self.env['product.product'].browse(
                self.env.context.get('active_ids'))
            for product_id in product_ids:
                ql = quality_limits.search([('name', '=', product_id.product_tmpl_id.id)])
                if ql:
                    ql.active = False

                pi = pricelist_items.search([('product_id', '=', product_id.id)])
                if pi:
                    pi.unlink()

                swo = stock_warehouse_op.search([('product_id', '=', product_id.id)])
                if swo:
                    swo.active = False

                mbl = mrp_bom_line.search([('product_id', '=', product_id.id)])
                if mbl:
                    mbl.unlink()

                mb = mrp_bom.search([('product_id', '=', product_id.id)])
                if mb:
                    mb.active = False

                pl = protocol_link.search([('product', '=', product_id.id)])
                if pl:
                    pl.unlink()

                # Finally, deactivate targeted product
                product_id.product_tmpl_id.active = False
                product_id.active = False

            return self.env['custom.views.warning'].show_message(
                _('Product(s) deactivated'),
                _('The deactivation of the selected product(s) has been carried out correctly')
            )
        else:
            return self.env['custom.views.warning'].show_message(
                _('There is nothing to deactivate'),
                _('No products selected to process!')
            )
