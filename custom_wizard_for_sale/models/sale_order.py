# -*- coding: utf-8 -*-

from odoo import models,fields,api
import datetime


class SaleOrder(models.Model):
    _inherit ='sale.order'


    #------------------------
    #  fields Declaration
    #------------------------


    is_active=fields.Boolean("Active" , default=True)

    def action_button(self):
        src = self.env.context.copy()
        src['default_sale_order_id'] =self.id
        return {'type': 'ir.actions.act_window',
             'res_model': 'confirm.wizard',
             'view_mode': 'form',            
             'target': 'new', 
             'context': src
             }