from odoo import models, fields


class OmoUsersPartnerInherit(models.Model):
    """ Inherit basic partner model """
    _inherit = 'res.partner'

    device_ids = fields.One2many('devices.model', 'owner_id', string="Devices")
