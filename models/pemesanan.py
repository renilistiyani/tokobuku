from odoo import api, fields, models

class Pemesanan(models.Model):
    _name = 'toko.pemesanan'
    _description = 'New Description'

    nama_pemesan = fields.Char(string='nama pemesan')
    kode_pemesanan = fields.Integer(string='kode pemesanan')
    tanggal = fields.Datetime(string='tanggal pemesanan',default=fields.Datetime.now)
    harga_pesan = fields.Integer(string='harga pesan')
    jumlah_pesan = fields.Integer(string='jumlah pesan')
    
    total_pemesanan = fields.Integer(
        compute='_compute_total_pemesanan', 
        string='Total Pemesanan')
    
    @api.model
    def _compute_total_pemesanan(self):
        for record in self:
            total=sum(self.env['toko.buku_pemesanan'].search([('order_id','=',record.id)]).mapped('total_pemesanan'))
            record.total_pemesanan=total