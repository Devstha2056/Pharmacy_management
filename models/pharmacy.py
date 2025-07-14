
from odoo import models, fields, api

class Pharmacy(models.Model):
    _name = 'pharmacy.pharmacy'
    _description = 'Pharmacy Management System'

    name = fields.Char(string='Pharmacy Name')

    user_id = fields.Many2one('res.users', string='User')
    # employee_id = fields.Many2one('hr.employee', string='Employee')
    company_id = fields.Many2one('res.company', string='Company')
    partner_id = fields.Many2one('res.partner', string='Customer', help="Customer Name")
    country_id = fields.Many2one('res.country', string='Country', help="Country Name",store=True)
    email_id = fields.Char(related='partner_id.email', string='Email', readonly=False, help="Email of Customer")
    phone_id = fields.Char(related='partner_id.phone', string='Mobile', readonly=False,help="Phone Number of Customer")
    street_id = fields.Char(related='partner_id.street', string='Street', readonly=False, help="Street of Customer")
    city_id = fields.Char(related='partner_id.city', string='City', readonly=False,help="City of Customer")
    is_active = fields.Boolean(string='Is Active', default=True)
    capture_images = fields.One2many('image.storage', 'image_id', string='Attached Images', store=True, tracking=True)
    capture_image = fields.Binary(string='Attached File', store=True)

