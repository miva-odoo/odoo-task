# -*- coding: utf-8 -*-

from odoo import models,fields,api
from odoo.exceptions import UserError


class SaleOrder(models.Model):
    _inherit ='sale.order'

  #-----------------------
  # method declaration
  #----------------------
     
    def action_confirm(self):
         if self.amount_total > self.partner_id.credit_limit:  
             raise UserError ("Total tax is greater than the credit limit")
         else:     
             return super(SaleOrder, self).action_confirm()

    def  _prepare_invoice(self):
         if self.amount_total > self.partner_id.credit_limit: 
             print('+++++++++++++++++++++++++++++++++++') 
             raise UserError ("Total tax is greater than the credit limit")
         else:     
             return super(SaleOrder, self)._prepare_invoice()
    

   


    
                

   

    