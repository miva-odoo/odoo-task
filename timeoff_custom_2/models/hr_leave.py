# -*- coding: utf-8 -*-

from odoo import models, api

class SaleOrder(models.Model):
    _inherit = "hr.leave"
    
    #---------------------------
    #Method Declaration
    #---------------------------
    
    def _prepare_home_portal_values(self, counters):
        values = super()._prepare_home_portal_values(counters)
        res = self.env['hr.leave'].search([('employee_ids','=',self.env.user.name)])
        values['len_hr'] = len(res)
        return values
        