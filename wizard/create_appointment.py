from odoo import api, fields, models, _


class CreateAppointment(models.TransientModel):
    _name = "create.appointment.wizard"
    _description = "Create Appointment Wizard"

    date_appointment = fields.Date(string='Date')
    patient_id = fields.Many2one('hospital.patient', string='Patient', require=True)

    def action_create_appointment(self):
        print('-------------Button clciked')
        vals = {
            'patient_id': self.patient_id.id,
            'date_appointment': self.date_appointment
        }
        print('vals...', vals)
        self.env['hospital.appointment'].create(vals)
