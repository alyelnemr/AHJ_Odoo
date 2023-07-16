# -*- coding: utf-8 -*-

from odoo import models, fields, api
import requests


class OasisPatients(models.Model):
    _name = 'oasis.patients'
    _description = 'Oasis Patients'
    _rec_name = 'patient_name'

    patient_id = fields.Char('Patient ID', required=True)
    patient_file_id = fields.Char('Patient File Number')
    patient_name = fields.Char('Patient Name', required=True)
    patient_episode_id = fields.One2many('patient.episodes', 'patient_id', string='Patient Episodes')

    def load_patients_from_oasis(self):
        url = 'http://hjh-repsrv-02:1022/api/getInpatient'
        res = requests.request("GET", url)
        for item in res.json():
            all_patients = []
            all_doctors = []
            all_rooms = []
            all_work_entities = []
            previous_patient = self.env['oasis.patients'].search([('patient_id', '=', item['PATIENT_ID'])])
            if not previous_patient:
                all_patients.append(
                    {
                        'patient_file_id': item['PATIENT_FILE_ID'],
                        'patient_id': item['PATIENT_ID'],
                        'patient_name': item['PATIENT_NAME'],
                    }
                )
            previous_doctor = self.env['oasis.doctors'].search([('doctor_id', '=', item['DOCTOR_ID'])])
            if not previous_doctor:
                all_doctors.append(
                    {
                        'doctor_name': item['DOCTOR_NAME'],
                        'doctor_name_ar': item['DOCTOR_NAME_AR'],
                        'doctor_id': item['DOCTOR_ID'],
                        'specialty_name': item['SPECIALTY'],
                    }
                )
            previous_room = self.env['oasis.rooms'].search([('room_no', '=', item['ROOM_NO'])])
            if not previous_room:
                all_rooms.append(
                    {
                        'room_no': item['ROOM_NO'],
                        'room_name': item['ROOM_NAME'],
                    }
                )
            previous_work_entity = self.env['oasis.workentity'].search([('work_entity_id', '=', item['WORK_ENTITY'])])
            if not previous_work_entity:
                all_work_entities.append(
                    {
                        'work_entity_name': item['WORKEN'],
                        'work_entity_id': item['WORK_ENTITY'],
                    }
                )
            if all_patients:
                self.env['oasis.patients'].create(all_patients)
            if all_doctors:
                self.env['oasis.doctors'].create(all_doctors)
            if all_rooms:
                self.env['oasis.rooms'].create(all_rooms)
            if all_work_entities:
                self.env['oasis.workentity'].create(all_work_entities)
        all_episodes = []
        for item in res.json():
            is_first_doctor = False
            if item['DOCTOR_SEQ'] == "1" or item['DOCTOR_SEQ'] == 1:
                is_first_doctor = True
            previous_episode = self.env['patient.episodes'].search([('patient_episode_id', '=', item['PATIENT_EPISODE_ID'])])
            if not previous_episode and is_first_doctor:
                patient_id = self.env['oasis.patients'].search([('patient_id', '=', item['PATIENT_ID'])])
                doctor_id = self.env['oasis.doctors'].search([('doctor_id', '=', item['DOCTOR_ID'])])
                room_id = self.env['oasis.rooms'].search([('room_no', '=', item['ROOM_NO'])])
                work_entity_id = self.env['oasis.workentity'].search([('work_entity_id', '=', item['WORK_ENTITY'])])
                all_episodes.append(
                    {
                        'patient_id': patient_id.id,
                        'episode_no': item['EPISODE_NO'],
                        'patient_episode_id': item['PATIENT_EPISODE_ID'],
                        'admission_no': item['ADMISSION_NO'],
                        'doctor_id': doctor_id.id,
                        'doctor_ids': [(4, doctor_id.id)],
                        'room_id': room_id.id,
                        'work_entity_id': work_entity_id.id,
                    }
                )
        if all_episodes:
            self.env['patient.episodes'].create(all_episodes)
        for item in res.json():
            is_first_doctor = False
            if item['DOCTOR_SEQ'] == "1" or item['DOCTOR_SEQ'] == 1:
                is_first_doctor = True
            previous_episode = self.env['patient.episodes'].search([('patient_episode_id', '=', item['PATIENT_EPISODE_ID'])])
            doctor_id = self.env['oasis.doctors'].search([('doctor_id', '=', item['DOCTOR_ID'])])
            if previous_episode:
                if is_first_doctor:
                    previous_episode.doctor_id = doctor_id.id
                previous_episode.doctor_ids = [(4, doctor_id.id)]
#
# {
#     'patient_file_id': item['PATIENT_FILE_ID'],
#     'patient_id': item['PATIENT_ID'],
#     'patient_name': item['PATIENT_NAME'],
#     'admission_no': item['ADMISSION_NO'],
#     'episode_no': item['EPISODE_NO'],
#     'room_name': item['ROOM_NAME'],
#     'room_no': item['ROOM_NO'],
#     'work_entity_name': item['WORKEN'],
#     'work_entity_id': item['WORK_ENTITY'],
#     'doctor_name': item['DOCTOR_NAME'],
#     'doctor_name_ar': item['DOCTOR_NAME_AR'],
#     'doctor_id': item['DOCTOR_ID'],
#     'specialty_name': item['SPECIALTY'],
# }