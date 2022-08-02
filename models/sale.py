from odoo import api, fields, models, tools

class HospitalPatient(models.Model):
    _inherit = "sale.order"

    sale_description = fields.Char(string='Sale Description', require=True)
