
from odoo import models, fields, api
from datetime import date

class Pharmacy(models.Model):
    _name = 'pharmacy.pharmacy'
    _description = 'Pharmacy Management System'
    _inherit = ['mail.thread']
    _order = 'order_number desc'
    _rec_name = 'order_number'

    user_id = fields.Many2one('res.users', string='Name')

    order_number = fields.Char(string='Order Number', readonly=True, copy=False, default='New')

    date = fields.Date(string='Order Date', help="Date of the Order")

    description = fields.Text(string='Description', help="Description of the Pharmacy Order")

    partner_id = fields.Many2one('res.partner', string='Customer',required=True,  help="Customer Name")

    country_id = fields.Many2one('res.country', string='Country', help="Country Name",store=True)

    email_id = fields.Char(related='partner_id.email', string='Email', readonly=False, help="Email of Customer")

    phone_id = fields.Char(related='partner_id.phone', string='Mobile',required=True, readonly=False,help="Phone Number of Customer")

    street_id = fields.Char(related='partner_id.street', string='Street', readonly=False, help="Street of Customer")

    city_id = fields.Char(related='partner_id.city', string='City', readonly=False,help="City of Customer")

    is_active = fields.Boolean(string='Is Active', default=True)



    capture_image = fields.Image(string='Upload Doctor Perception', store=True)

    age = fields.Char(string="Age", compute="_compute_age", store=True)

    date_of_birth = fields.Date(string="Date of Birth")
    @api.model
    def create(self, vals):
        if vals.get('order_number', 'New') == 'New':
            vals['order_number'] = self.env['ir.sequence'].next_by_code('pharmacy.pharmacy') or 'New'
        return super(Pharmacy, self).create(vals)

    @api.depends('date_of_birth')
    def _compute_age(self):
        for rec in self:
            if rec.date_of_birth:
                today = date.today()
                dob = rec.date_of_birth

                years = today.year - dob.year
                months = today.month - dob.month
                days = today.day - dob.day

                if days < 0:
                    months -= 1
                if months < 0:
                    years -= 1
                    months += 12

                if years > 0 and months > 0:
                    rec.age = f"{years} year {months} month"
                elif years > 0:
                    rec.age = f"{years} year"
                elif months > 0:
                    rec.age = f"{months} month"
                else:
                    rec.age = "Less than a month"
            else:
                rec.age = "Not set"
