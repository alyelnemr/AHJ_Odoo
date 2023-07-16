# -*- coding: utf-8 -*-

from odoo import models, fields, api


class OasisPatients(models.Model):
    _name = 'oasis.doctors'
    _description = 'Oasis Doctors'
    _rec_name = 'doctor_name'

    doctor_id = fields.Char('Doctor ID', required=True)
    doctor_name = fields.Char('Doctor Name', required=True)
    doctor_name_ar = fields.Char('Doctor Name Arabic')
    specialty_name = fields.Char('Specialty Name')
    user_id = fields.Many2one('res.users', string=" User ID ")
