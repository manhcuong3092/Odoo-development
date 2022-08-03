from odoo import api, fields, models, _

class HospitalPatient(models.Model):
    _name = "hospital.appointment"
    _inherit = ["mail.thread", 'mail.activity.mixin']
    _description = "Hospital Appointment"

    name = fields.Char('Order reference', require=True, copy=False, readonly=True,
                            default=lambda self:_('New'))
    note = fields.Text(string='Description')
    date_appointment = fields.Date(string='Date')
    date_checkup = fields.Datetime(string='Check up time')
    state = fields.Selection([('draft', 'Draft'), ('confirm', 'Confirmed'),
                              ('done', 'Done'), ('cancel', 'Cancelled')],
                             default='draft', string='Status', tracking=True)

    patient_id = fields.Many2one('hospital.patient', string='Patient', require=True)
    age = fields.Integer('Age', related='patient_id.age', required=True, tracking=True)

    def action_confirm(self):
        self.state = 'confirm'

    def action_done(self):
        self.state = 'done'

    def action_draft(self):
        self.state = 'draft'

    def action_cancel(self):
        self.state = 'cancel'

    @api.model
    def create(self, vals):
        if not vals.get('note'):
            vals['note'] = 'New Patient'
        if vals.get('name', _('New')) == _('New'):
            vals['name'] = self.env['ir.sequence'].next_by_code('hospital.appointment') or _('New')
        res = super(HospitalPatient, self).create(vals)
        return res