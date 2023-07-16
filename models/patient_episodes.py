# -*- coding: utf-8 -*-

from odoo import models, fields, api


class OasisPatients(models.Model):
    _name = 'patient.episodes'
    _description = 'Oasis Patients Episodes'

    patient_id = fields.Many2one(comodel_name="oasis.patients", string="Patient ID", required=1)
    episode_no = fields.Char('Episode Number', required=True)
    patient_episode_id = fields.Char('Patient Episode', copy=False)
    doctor_id = fields.Many2one(comodel_name="oasis.doctors", string="Doctor ID", required=1)
    doctor_ids = fields.Many2many(comodel_name="oasis.doctors", string="Doctor ID", required=False)
    room_id = fields.Many2one(comodel_name="oasis.rooms", string="Room", required=1)
    work_entity_id = fields.Many2one(comodel_name="oasis.workentity", string="Work Entity", required=1)
    admission_no = fields.Char('Admission Number')
    patient_prescription = fields.One2many('patient.prescription', 'patient_episode_id', string='Patient Prescriptions')

    def name_get(self):
        result = []
        for rec in self:
            name = rec.patient_id.patient_file_id + ' | ' + rec.patient_id.patient_name
            result.append((rec.id, name))
        return result
