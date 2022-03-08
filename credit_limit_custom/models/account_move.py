# -*- coding: utf-8 -*-

from odoo import fields,models,api
from odoo.exceptions import UserError


class AccountMove(models.Model):
    _inherit='account.move'

    def action_post(self):
         if self.amount_total > self.partner_id.credit_limit:  
             raise UserError ("Total tax is greater than the credit limit")
         else:     
             return super(AccountMove, self).action_post()

  
 
   



    

    


