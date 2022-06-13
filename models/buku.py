from odoo import api, fields, models

class Buku(models.Model):
    _name = 'toko.buku'
    _description = 'New Description'

    kode_buku = fields.Integer(string='kode buku')
    nama_buku = fields.Char(string='nama buku')
    harga_buku = fields.Integer(string='harga buku')
    jumlah_buku = fields.Integer(string='jumlah buku')
    supplier_id = fields.Many2one(comodel_name='toko.supplier', string='')
    