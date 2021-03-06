# -*- coding: utf-8 -*-
# © 2018 Comunitea
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, api


class PaletTagParser(models.AbstractModel):
    """
    """
    _name = 'report.warehouse_shipping_light.report_container_labels'

    @api.multi
    def render_html(self, data=None):
        report_name = 'warehouse_shipping_light.report_container_labels'
        picks = self.env['stock.picking'].browse(self._ids)
        packages = {}
        for picking in picks:
            packages[picking.id] = []
            sscc_list = picking.mapped('pack_operation_ids').mapped(
                'sscc_ids').filtered(lambda r: r.type in ('2', '3'))
            for sscc in sscc_list.filtered(lambda r: r.type == '2'):
                packages[picking.id].append(sscc)
            for sscc in sscc_list.filtered(lambda r: r.type == '3').sorted(
                    lambda x: x.operation_ids[0].package):
                index = sscc.operation_ids[0].package - 1
                packages[picking.id].insert(index, sscc)
        docargs = {
            'doc_ids': [],
            'doc_model': 'stock.picking',
            'docs': picks,
            'packages': packages
        }
        return self.env['report'].render(report_name, docargs)
