from datetime import datetime

from odoo import fields, models, api


class DeviceToServices(models.Model):
    """This model creating for relationship between device and service models"""

    _name = 'device.to.services'
    _description = 'Related model for device and services'

    service_day = fields.Datetime(string="Service day", default=datetime.now())
    device_id = fields.Many2one('devices.model', required=True)
    service_id = fields.Many2one('services.model', required=True)
    base_currency_id = fields.Many2one('res.currency')
    serial_number = fields.Char(related="device_id.serial_number", string="Serial number")
    status = fields.Selection([('ok', 'Done'), ('in_work', 'In progress'), ('cancel', 'Cancel')], string='Status',
                              default="in_work")
    price = fields.Monetary(related="service_id.price", string="Price", currency_field='base_currency_id')

    @api.model
    def create(self, vals):
        """ for new features """
        return super().create(vals)

    def write(self, vals):
        """ for new features """
        return super().write(vals)
