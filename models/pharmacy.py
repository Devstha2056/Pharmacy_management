
from odoo import models, fields, api

class Pharmacy(models.Model):
    _name = 'pharmacy.pharmacy'
    _description = 'Pharmacy Management System'

    name = fields.Char(string='Pharmacy Name', required=True)
    order_number = fields.Char(string='Order Number', required=True, help="Unique Order Number for the Pharmacy")
    date = fields.Date(string='Order Date', required=True, help="Date of the Order")
    description = fields.Text(string='Description', help="Description of the Pharmacy Order")
    user_id = fields.Many2one('res.users', string='User', required=True)

    company_id = fields.Many2one('res.company', string='Company', required=True)
    partner_id = fields.Many2one('res.partner', string='Customer', required=True, help="Customer Name")
    country_id = fields.Many2one('res.country', string='Country', required=True, help="Country Name",store=True)
    email_id = fields.Char(related='partner_id.email', string='Email', readonly=False, help="Email of Customer")
    phone_id = fields.Char(related='partner_id.phone', string='Mobile', readonly=False, required=True,help="Phone Number of Customer")
    street_id = fields.Char(related='partner_id.street', string='Street', readonly=False, required=True, help="Street of Customer")
    city_id = fields.Char(related='partner_id.city', string='City', readonly=False,help="City of Customer")
    is_active = fields.Boolean(string='Is Active', default=True)
   
    capture_image = fields.Image(string='Upload Doctor Perception', store=True)


    @api.model
    def create(self, vals):
        if vals.get('order_number', 'New') == 'New':
            vals['order_number'] = self.env['ir.sequence'].next_by_code('pharmacy.pharmacy') or 'New'
        return super(Pharmacy, self).create(vals)

