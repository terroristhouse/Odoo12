# -*- coding: utf-8 -*-
# from odoo import http


# class KrHuiyi(http.Controller):
#     @http.route('/kr_huiyi/kr_huiyi/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/kr_huiyi/kr_huiyi/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('kr_huiyi.listing', {
#             'root': '/kr_huiyi/kr_huiyi',
#             'objects': http.request.env['kr_huiyi.kr_huiyi'].search([]),
#         })

#     @http.route('/kr_huiyi/kr_huiyi/objects/<model("kr_huiyi.kr_huiyi"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('kr_huiyi.object', {
#             'object': obj
#         })
