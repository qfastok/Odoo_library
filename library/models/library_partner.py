from odoo import api, fields, models, _, tools


class LibraryPartner(models.Model):
    _name = "library.partner"
    _description = "Library Partner"

    name = fields.Char(string='Name')
    email = fields.Char(string='Email')
    address = fields.Text('Address')
    partner_type = fields.Selection([
        ('customer', 'Customer'),
        ('author', 'Author'),
    ])
    rental_ids = fields.One2many('library.rental', 'customer_id')
