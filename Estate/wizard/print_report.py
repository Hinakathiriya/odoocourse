from odoo import fields, models

class PrintReport(models.TransientModel):
    _name = 'print.report'
    _description = 'Print Report'

    amount = fields.Integer("Enter Amount")

    def print(self):
        print("\n\nPrint report ")