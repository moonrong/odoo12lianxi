# -*- coding: utf-8 -*-
from odoo import http

# class Odoogoedu(http.Controller):
#     @http.route('/odoogoedu/odoogoedu/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/odoogoedu/odoogoedu/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('odoogoedu.listing', {
#             'root': '/odoogoedu/odoogoedu',
#             'objects': http.request.env['odoogoedu.odoogoedu'].search([]),
#         })

#     @http.route('/odoogoedu/odoogoedu/objects/<model("odoogoedu.odoogoedu"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('odoogoedu.object', {
#             'object': obj
#         })