# -*- coding: utf-8 -*-

from odoo import models, fields, api


class OasisPatients(models.Model):
    _name = 'patient.prescription'
    _description = 'Oasis Patients Prescription'
    _rec_name = 'prescription_title'

    prescription_title = fields.Char('Title', required=True, default="Prescription")
    patient_episode_id = fields.Many2one(comodel_name="patient.episodes", string='Patient Episode', required=True, copy=False)
    product_id = fields.Many2one(comodel_name="product.product", string="Medicine", domain=[('is_medicine', '=', True)], required=1)
    quantity = fields.Integer(string='Medicine Quantity', default=1, required=1)
    is_active = fields.Boolean(string='Is Active', default=True)
    start_treatment = fields.Datetime(string='Start Of Treatment', required=False, default=fields.Datetime.now)
    end_treatment = fields.Datetime(string='End Of Treatment', required=False, default=fields.Datetime.now)
    route = fields.Many2one('drug.route', string=" Administration Route ")
    dose = fields.Float(string='Dose', default=1, required=1)
    frequency = fields.Integer(string='Frequency')
    frequency_unit = fields.Selection([('wr', '(When Required)'),
                                       ('seconds', 'Seconds'),
                                       ('minutes', 'Minutes'),
                                       ('hours', 'hours'),
                                       ('days', 'Days'),
                                       ('weeks', 'Weeks')], string='Unit', required=True, default='wr')
    notes = fields.Text(string='Notes')
    doctor_user = fields.Many2one('res.users', string='Doctor', default=lambda self: self.env.user)
