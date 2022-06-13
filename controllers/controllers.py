# -*- coding: utf-8 -*-
# from odoo import http


# class TokoBuku(http.Controller):
#     @http.route('/toko_buku/toko_buku/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/toko_buku/toko_buku/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('toko_buku.listing', {
#             'root': '/toko_buku/toko_buku',
#             'objects': http.request.env['toko_buku.toko_buku'].search([]),
#         })

#     @http.route('/toko_buku/toko_buku/objects/<model("toko_buku.toko_buku"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('toko_buku.object', {
#             'object': obj
#         })
