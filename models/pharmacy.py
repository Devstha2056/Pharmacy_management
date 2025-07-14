

from odoo import models, fields, api


class Pharmacy(models.Model):
    _name = 'pharmacy.pharmacy'
    _description = 'Pharmacy Management System'

    name = fields.Char()
    value = fields.Integer()
    value2 = fields.Float(compute="_value_pc", store=True)
    description = fields.Text()

    # @api.depends('value')
    # def value_pc(self):
    #     for record in self:
    #         record.value2 = float(record.value) / 100
    #
