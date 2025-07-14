# -*- coding: utf-8 -*-
# from odoo import http


# class PharmacyManagement(http.Controller):
#     @http.route('/pharmacy_management/pharmacy_management', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/pharmacy_management/pharmacy_management/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('pharmacy_management.listing', {
#             'root': '/pharmacy_management/pharmacy_management',
#             'objects': http.request.env['pharmacy_management.pharmacy_management'].search([]),
#         })

#     @http.route('/pharmacy_management/pharmacy_management/objects/<model("pharmacy_management.pharmacy_management"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('pharmacy_management.object', {
#             'object': obj
#         })

