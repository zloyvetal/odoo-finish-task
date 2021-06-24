from odoo import fields, models, api


class Services(models.Model):
    """ This model describe a services """

    _name = 'services.model'
    _description = 'Main service model'

    name = fields.Char(string="Service Name", required=True)
    base_currency_id = fields.Many2one('res.currency', required=True)
    price = fields.Monetary(currency_field='base_currency_id', string="Price", required=True)
    description = fields.Text(string="Description")

    @api.model
    def create(self, vals):
        """ for new features """
        return super().create(vals)

    def write(self, vals):
        """ for new features """
        return super().write(vals)
