# -*- coding: utf-8 -*-

from odoo import models, fields, api


class OasisPatients(models.Model):
    _name = 'oasis.workentity'
    _description = 'Oasis Work Entities'
    _rec_name = 'work_entity_name'

    work_entity_name = fields.Char('Work Entity Name', required=True)
    work_entity_id = fields.Char('Work Entity ID', required=True)
