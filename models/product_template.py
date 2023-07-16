# -*- coding: utf-8 -*-
from odoo import api, fields, models, _, exceptions


class ProductInherit(models.Model):
    _inherit = 'product.template'

    is_medicine = fields.Boolean(string='Is Medicine', default=True)
