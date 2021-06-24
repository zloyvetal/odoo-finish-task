from logging import getLogger

from odoo import fields, models

_logger = getLogger(__name__)


class ReportFilter(models.TransientModel):
    _name = 'report.filter'
    _description = 'report filter'

    date_from = fields.Date('Start date', required=True)
    date_to = fields.Date('End date', required=True)
    device_id = fields.Many2one("devices.model", string="Device", required=True)

    def print_report(self):
        data = {'date_from': self.date_from, 'date_to': self.date_to, 'device_id': self.device_id.id}

        return self.env.ref('services.report_device_t').report_action(self, data)


class ReportPDF(models.AbstractModel):
    _name = 'report.services.report_device_templates'

    def _get_report_values(self, docids, data=None):
        domain = [('status', '!=', 'cancel')]
        if data.get('date_from'):
            domain.append(('service_day', '>=', data.get('date_from')))
        if data.get('date_to'):
            domain.append(('service_day', '<=', data.get('date_to')))
        if data.get("device_id"):
            domain.append(('device_id', '=', data.get('device_id')))
        device = self.env['devices.model'].browse(data.get('device_id'))
        data.update({'device': device})
        docs = self.env['device.to.services'].search(domain)

        return {
            'doc_ids': docs.ids,
            'doc_model': 'device.to.services',
            'docs': docs,
            'datas': data
        }
