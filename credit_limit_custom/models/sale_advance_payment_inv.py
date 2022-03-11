# -*- coding: utf-8 -*-

from odoo import models,fields,api
from odoo.exceptions import UserError


class SaleAdvancePaymentInv(models.TransientModel):

    _inherit ='sale.advance.payment.inv'


    def  _prepare_invoice_values(self):
         if self.amount_total > self.partner_id.credit_limit: 
             raise UserError ("Total tax is greater than the credit limit")  
         return super(SaleAdvancePaymentInv, self)._prepare_invoice_values()
