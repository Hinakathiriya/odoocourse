# -*- coding: utf-8 -*-
# from odoo import http


# class Marble(http.Controller):
#     @http.route('/marble/marble/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/marble/marble/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('marble.listing', {
#             'root': '/marble/marble',
#             'objects': http.request.env['marble.marble'].search([]),
#         })

#     @http.route('/marble/marble/objects/<model("marble.marble"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('marble.object', {
#             'object': obj
#         })
