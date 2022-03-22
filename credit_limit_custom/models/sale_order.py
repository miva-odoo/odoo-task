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
         return super(SaleOrder, self).action_confirm()

    def  _prepare_invoice(self):
         if self.amount_total > self.partner_id.credit_limit: 
             raise UserError ("Total tax is greater than the credit limit")     
         return super(SaleOrder, self)._prepare_invoice()

class ChangePasswordWizard(models.TransientModel):
    """ A wizard to manage the change of users' passwords. """
    _name = "change.password.wizard"
    _description = "Change Password Wizard"

    def _default_user_ids(self):
        user_ids = self._context.get('active_model') == 'res.users' and self._context.get('active_ids') or []
        return [
            Command.create({'user_id': user.id, 'user_login': user.login})
            for user in self.env['res.users'].browse(user_ids)
        ]

    user_ids = fields.One2many('change.password.user', 'wizard_id', string='Users', default=_default_user_ids)

    def change_password_button(self):
        self.ensure_one()
        self.user_ids.change_password_button()
        if self.env.user in self.user_ids.user_id:
            return {'type': 'ir.actions.client', 'tag': 'reload'}
        return {'type': 'ir.actions.act_window_close'}


    

   


    
                

   

    