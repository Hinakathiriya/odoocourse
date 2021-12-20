# -*- coding: utf-8 -*-
from odoo import models, fields, api

class MarbleOrder(models.Model):
    _name = 'marble.order'
    _description = 'Marble Order'

    vendor_name = fields.Many2one('res.partner')
    date = fields.Date()

class MarbleDetailsLine(models.Model):
    _name = 'marble.details.line'
    _description = 'Marble Details Line'

    

    #pro_id = fields.Many2one('marble.details')
    #quantity_id = fields.One2many('marble.details')
    #unit_price_id = fields.Many2one('marble.details')


class MarbleDetails(models.Model):
    _name = 'marble.details'
    _description = 'Marble Details'

    pro_name = fields.Char(string="Product Name", default="Unknown", required=True)
    quantity = fields.Integer()
    uom = fields.Integer()
    unit_price = fields.Float()
    total_price = fields.Float()

#\     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
