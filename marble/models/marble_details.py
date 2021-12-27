# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError

class MarbleOrder(models.Model):
    _name = 'marble.order'
    _description = 'Marble Order'

    vendor_name = fields.Many2one('res.partner')
    date = fields.Date()

#class MarbleDetailsLine(models.Model):
 #   _name = 'marble.details.line'
#    _description = 'Marble Details Line'

    

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
    total_price = fields.Float(compute="_compute_price")

    @api.depends('quantity', 'unit_price')
    def _compute_price(self):
        for record in self:
            record.total_price = record.quantity * record.unit_price

    #def action_transfer(self):
     #   for record in self:
      #      if record.state == 'transfer':
       #         raise UserError("Transfer...")

    #def _inverse_area(self):
     #   for record in self:
      #      record.living_area = record.garden_area = record.total_area / 2