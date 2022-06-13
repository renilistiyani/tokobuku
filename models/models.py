# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class toko_buku(models.Model):
#     _name = 'toko_buku.toko_buku'
#     _description = 'toko_buku.toko_buku'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
