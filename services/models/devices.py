from odoo import fields, models, api


class Device(models.Model):
    """This model describe a device"""

    _name = 'devices.model'
    _description = 'Main device model'

    name = fields.Char(string='Device name', required=True)

    serial_number = fields.Char(string="Serial Number", required=True)
    description = fields.Text(string="Description")
    service_id = fields.One2many('device.to.services', 'device_id', string="services")
    owner_id = fields.Many2one('res.partner', string="Owner of device", required=True)
    create_date = fields.Date(string="Create date", required=True)
    death_date = fields.Date(string="Date of death", required=True)

    @api.model
    def create(self, vals):
        """ for new features """
        return super().create(vals)

    def write(self, vals):
        """ for new features """
        return super().write(vals)
