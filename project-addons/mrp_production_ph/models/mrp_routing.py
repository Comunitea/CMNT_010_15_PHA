# -*- coding: utf-8 -*-
# © 2018 Pharmadus I.T.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields, api

class MrpRouting(models.Model):
    _inherit = 'mrp.routing'

    wildcard_route = fields.Boolean()