from odoo import api, fields, models, _, tools


class LibraryBook(models.Model):
    _name = "library.book"
    _description = "Library Book"

    name = fields.Char(string='Name')
    author_ids = fields.Many2many('library.partner', string='Partner')
    edition_date = fields.Date
    isbn = fields.Char(string='isbn')
    publisher_id = fields.Many2one('library.publisher')
    rental_ids = fields.One2many('library.rental', 'book_id')

