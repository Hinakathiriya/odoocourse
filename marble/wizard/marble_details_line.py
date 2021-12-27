from odoo import fields, models

class MarbleDetailsLine(models.TransientModel):
    _name = 'marble.details.line'
    _description =' Marble details line'

    name = fields.Char()

    def marble_details_line(self):
        print("\n\nHello wizard")
