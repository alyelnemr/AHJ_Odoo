# -*- coding: utf-8 -*-

from odoo import models, fields, api


class OasisPatients(models.Model):
    _name = 'oasis.rooms'
    _description = 'Oasis Rooms'
    _rec_name = 'room_name'

    room_no = fields.Char('Room Number', required=True)
    room_name = fields.Char('Room Name', required=True)
