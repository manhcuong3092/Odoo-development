from odoo import api, fields, models, _


class CreateAppointment(models.TransientModel):
    _name = "create.appointment.wizard"
    _description = "Create Appointment Wizard"

    name = fields.Char(string='Name', required=True)
    patient_id = fields.Many2one('hospital.patient', string='Patient', require=True)

    def action_create_appointment(self):
        print('-------------Button clciked')
