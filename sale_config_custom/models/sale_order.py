# -*- coding: utf-8 -*-

from xmlrpc.client import Boolean
from odoo import models,fields,api


class SaleOrder(models.Model):
    _inherit ='sale.order'

  #-----------------------
  # field declaration
  #----------------------
  
    user_name = fields.Char(default="Minaxi")
    is_sale_user = fields.Boolean(compute='_compute_user')

  #-----------------------
  # method declaration
  #----------------------

    @api.model
    def create(self, vals):
        result = super(SaleOrder, self).create(vals)
        config_user = self.env['ir.config_parameter'].sudo().get_param('sale_config_custom.user_id')
        if config_user:
            result.user_id = config_user
        return result

  

    @api.depends('user_name')
    def _compute_user(self) :
        for record in self:
            record.is_sale_user  = self.env['ir.config_parameter'].sudo().get_param('sale_config_custom.is_sale_user')

        


