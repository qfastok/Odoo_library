from odoo import api, fields, models, _, tools


class LibraryRental(models.Model):
    _name = "library.rental"
    _description = "Library Rental"

    customer_id = fields.Many2one("library.partner")
    book_id = fields.Many2one("library.book")
    rental_date = fields.Date
    return_date = fields.Date
    customer_address = fields.Text(rental="customer_id.address", string="Customer Address")
    customer_email = fields.Char(rental="customer_id.email", string="Customer Email")
    book_authors = fields.Char(rental="book_id.author_ids", string="Book Author")
    book_edition_date = fields.Date(rental="book_id.edition_date", string="Book Edition Date")
    book_publisher = fields.Char(rental="book_id.publisher_id", string="Book Publisher")
