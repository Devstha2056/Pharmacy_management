from odoo import models, api, fields
from datetime import datetime, timedelta
from odoo.exceptions import UserError
from odoo.exceptions import ValidationError
import base64
import  os


class ImageStorage(models.Model):
    _name = 'image.storage'
    _description = 'Image Storage'
    _rec_name = 'datas_fname'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    attachment_ids = fields.Many2many(
        'ir.attachment',
        string="Attached Files"
    )

    capture_image = fields.Binary(string='Attached File', store=True)
    image_id = fields.Many2one('ticket.management', string='Image List')
    datas_fname = fields.Char(string="File Name")

    @api.model
    def create(self, vals):
        res = super(ImageStorage, self).create(vals)
        if 'capture_image' in vals and vals['capture_image']:
            attachment = res._create_attachment()
            res.attachment_ids = [(4, attachment.id)]  # Link to Many2many field
        return res

    def write(self, vals):
        res = super(ImageStorage, self).write(vals)
        for record in self:
            if 'capture_image' in vals and vals['capture_image']:
                attachment = record._create_attachment()
                record.attachment_ids = [(4, attachment.id)]  # Append to Many2many
        return res

    def _create_attachment(self):
        """Creates an attachment record from the uploaded image."""
        self.ensure_one()  # Ensure only one record is processed
        if not self.capture_image:
            return False

        attachment = self.env['ir.attachment'].create({
            'name': self.datas_fname or 'Unnamed Image',
            'type': 'binary',
            'datas': self.capture_image,  # The binary image field
            'res_model': 'ticket.management',
            'res_id': self.image_id.id if self.image_id else None,  # Link the attachment to the related ticket
        })
        return attachment

    @api.constrains('capture_image')
    def _check_capture_image_size(self):
        param = self.env['ir.config_parameter'].sudo()
        size_limit = int(
            param.get_param('attachment_size_restriction.attachment_size_limit', default=1048576))

        for record in self:
            if record.capture_image:
                image_size = len(base64.b64decode(record.capture_image or b''))  # actual byte size
                if image_size > size_limit:
                    raise ValidationError(
                        f"The uploaded image exceeds the maximum allowed size of {size_limit // 1024} KB."
                    )

    @api.constrains('capture_image', 'datas_fname')
    def _check_capture_image_constraints(self):
        param = self.env['ir.config_parameter'].sudo()
        size_limit = int(
            param.get_param('attachment_size_restriction.attachment_size_limit', default=1048576))  # 1MB default
        allowed_extensions = ['.jpg', '.jpeg', '.png', '.pdf', '.doc', '.docx','.xlsx','.csv']

        for record in self:
            # Validate file size
            if record.capture_image:
                size = len(base64.b64decode(record.capture_image or b''))
                if size > size_limit:
                    raise ValidationError(
                        f"The uploaded file exceeds the maximum allowed size of {round(size_limit / 1024)} KB."
                    )

            # Validate file extension
            if record.datas_fname:
                _, ext = os.path.splitext(record.datas_fname.lower())
                if ext not in allowed_extensions:
                    raise ValidationError(
                        f"Invalid file type '{ext}'. Allowed types: {', '.join(allowed_extensions)}"
                    )
    def download_attachment(self):
        """Redirects to the attachment URL for download"""
        self.ensure_one()
        if not self.attachment_ids:
            return False

        # Assuming the first attachment should be downloaded
        attachment = self.attachment_ids[0]

        return {
            'type': 'ir.actions.act_url',
            'url': f'/web/content/{attachment.id}?download=true',
            'target': 'self',
        }

