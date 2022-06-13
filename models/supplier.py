from odoo import api, fields, models

class Supplier(models.Model):
    _name = 'toko.supplier'
    _description = 'New Description'

    kode_supplier = fields.Integer(string='kode supplier')
    name_supplier = fields.Char(string='nama supplier')
    alamat_supplier = fields.Integer(string='alamat supplier')
    no_tlp_supplier = fields.Integer(string='no tlp supplier')
    
    buku_ids = fields.One2many(comodel_name='toko.buku', 
                                 inverse_name='supplier_id', 
                                 string='Bukunya')
     