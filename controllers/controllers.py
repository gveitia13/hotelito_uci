# -*- coding: utf-8 -*-
# from odoo import http


# class ../odoo-custom-addons/comercio(http.Controller):
#     @http.route('/../odoo-custom-addons/comercio/../odoo-custom-addons/comercio', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/../odoo-custom-addons/comercio/../odoo-custom-addons/comercio/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('../odoo-custom-addons/comercio.listing', {
#             'root': '/../odoo-custom-addons/comercio/../odoo-custom-addons/comercio',
#             'objects': http.request.env['../odoo-custom-addons/comercio.../odoo-custom-addons/comercio'].search([]),
#         })

#     @http.route('/../odoo-custom-addons/comercio/../odoo-custom-addons/comercio/objects/<model("../odoo-custom-addons/comercio.../odoo-custom-addons/comercio"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('../odoo-custom-addons/comercio.object', {
#             'object': obj
#         })
