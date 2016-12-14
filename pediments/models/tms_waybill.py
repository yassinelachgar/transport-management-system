# -*- coding: utf-8 -*-
# Copyright 2016, Jarsa Sistemas, S.A. de C.V.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import fields, models


class TmsWaybill(models.Model):
    _inherit = 'tms.waybill'

    customs_ids = fields.One2many(
        'tms.pediments',
        'waybill_id',
        string="Customs")
