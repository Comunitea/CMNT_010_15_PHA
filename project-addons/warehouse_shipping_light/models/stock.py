# -*- coding: utf-8 -*-
##############################################################################
#
#    Copyright (C) 2015 Pharmadus. All Rights Reserved
#    $Óscar Salvador <oscar.salvador@pharmadus.com>$
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

from openerp import models, fields, api


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    complete = fields.Integer('Number of complete',
                              compute='_compute_packages_and_weight',
                              readonly=True,
                              store=True)
    number_of_packages = fields.Integer('Number of packages',
                              compute='_compute_packages_and_weight',
                              readonly=True,
                              store=True)
    number_of_palets = fields.Integer('Number of palets',
                              compute='_compute_packages_and_weight',
                              readonly=True,
                              store=True)
    weight = fields.Float('Weight',
                              compute='_compute_packages_and_weight',
                              readonly=True,
                              store=True)
    real_weight = fields.Float('Real weight to send',
                              required=True,
                              default=0)

    @api.one
    @api.depends('pack_operation_ids',
                 'pack_operation_ids.complete',
                 'pack_operation_ids.package',
                 'pack_operation_ids.product_qty',
                 'pack_operation_ids.product_id')
    def _compute_packages_and_weight(self):
        complete_sum = 0
        weight_sum = 0
        package_list = [] # Count different packages
        palet_list = []  # Count differents palets

        for po in self.pack_operation_ids:
            complete_sum += po.complete
            if po.package > 0 and not po.package in package_list:
                package_list.append(po.package)
            if po.palet > 0 and not po.palet in palet_list:
                palet_list.append(po.palet)
            weight_sum += po.product_id.product_tmpl_id.weight * po.product_qty

        self.complete = complete_sum
        self.number_of_packages = len(package_list) + complete_sum
        self.number_of_palets = len(palet_list)
        self.weight = weight_sum

    @api.one
    def create_pack_ops(self):
        picking = self._ids
        ctx = {
            'active_model': self._name,
            'active_ids': picking,
            'active_id': len(picking) and picking[0] or False
        }
        self.env['stock.transfer_details'].with_context(ctx).create({'picking_id': len(picking) and picking[0] or False})


class StockPackOperation(models.Model):
    _inherit = 'stock.pack.operation'

    palet = fields.Integer('Palet', default=0)
    complete = fields.Integer('Complete',
                              compute='_compute_complete_and_rest',
                              readonly=True,
                              store=True)
    package = fields.Integer('Package', default=0)
    rest = fields.Integer('Rest',
                          compute='_compute_complete_and_rest',
                          readonly=True,
                          store=True)

    @api.one
    @api.depends('product_id', 'product_qty')
    def _compute_complete_and_rest(self):
        for rec in self:
            complete_qty = rec.product_id.product_tmpl_id.box_elements
            if complete_qty > 0:
                div = divmod(rec.product_qty, complete_qty)
                rec.complete = div[0]
                rec.rest = div[1]
            else:
                rec.complete = 0
                rec.rest = self.product_qty
