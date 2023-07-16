# -*- coding: utf-8 -*-

from odoo import models, fields, api


class OasisPatients(models.Model):
    _name = 'drug.route'
    _description = 'Oasis Drug Routes'
    _rec_name = 'route_name'

    route_name = fields.Char('Route Name', required=True)
