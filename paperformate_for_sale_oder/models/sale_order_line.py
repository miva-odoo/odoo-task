# -*- coding: utf-8 -*-

from odoo import models,fields,api
import datetime


class SaleOrderLine(models.Model):
    _inherit ='sale.order.line'


    #------------------------
    #  fields Declaration
    #------------------------

    second_discount = fields.Float(string="2nd Disc. %" )

    @api.depends('price_subtotal','second_discount','price_unit')
    def _compute_amount(self):
        res = super()._compute_amount() 
        for rec in self :
            rec.price_subtotal = rec.price_subtotal - ((rec.second_discount* rec.price_subtotal)/100)
        return res          





