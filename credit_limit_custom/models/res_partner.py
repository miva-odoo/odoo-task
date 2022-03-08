# -*- coding: utf-8 -*-

from odoo import fields,models,api


class ResPartner(models.Model):
    _inherit='res.partner'

    #----------------------------
    #  fields Declaration
    #---------------------------

    credit_limit = fields.Float(string="Credit Limit")

 
   



    

    
