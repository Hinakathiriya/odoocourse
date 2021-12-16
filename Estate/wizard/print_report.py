from odoo import fields, models

class PrintReport(models.TransientModel):
    _name = 'print.report'
    _description = 'Print Report'

    amount = fields.Integer("Enter Amount")

    def print(self):
        print("\n\nPrint report")
        docs = self.env['estate.property'].search([('expected_price', '>=', self.amount)]).ids
        return self.env.ref('estate.report_print_property').report_action(docs)