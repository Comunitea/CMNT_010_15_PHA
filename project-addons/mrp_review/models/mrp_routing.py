# -*- coding: utf-8 -*-
# © 2017 Comunitea
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields


class MrpRouting(models.Model):

    _inherit = 'mrp.routing'

    decrease_percentage = fields.Float()
