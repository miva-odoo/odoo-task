# -*- coding: utf-8 -*-

from odoo import models,fields,api
from odoo.exceptions import UserError

class SaleOrder(models.Model): 
    _inherit ='sale.order'


    #------------------------
    #  fields Declaration
    #------------------------

    zero_stock_approval = fields.Boolean(string='Zero Stock approval')
    bool_approval = fields.Boolean(string = 'New Approval', compute = '_compute_user_group')

    #-----------------------
    # method declaration
    #----------------------
   
    

    # @api.constrains('zero_stock_approval')
    # def _zero_stock_approval(self):
    #     for record in self:
    #         if record.zero_stock_approval != True:
    #             raise UserError("Approval are not True pls first true approual")
           

    def action_confirm(self):
     for record in self:
         if not record.zero_stock_approval:
             raise UserError ("Approval are not True pls first true approual")
         else:
             return super(SaleOrder, self).action_confirm()

    @api.depends('zero_stock_approval')
    def _compute_user_group(self) :     
        if self.env.user.has_group('sales_team.group_sale_manager'):  
            self.bool_approval = True
        else :
            self.bool_approval = False






   