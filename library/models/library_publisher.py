from odoo import api, fields, models, _, tools


class LibraryPublisher(models.Model):
    _name = "library.publisher"
    _description = "Library Publisher"

    name = fields.Char(string='Name')
