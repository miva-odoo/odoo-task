# -*- coding: utf-8 -*-

from odoo import fields,models


class ResPartner(models.Model):
    _inherit='res.partner'

    #----------------------------
    #  fields Declaration
    #---------------------------

    day_to_delivrer = fields.Integer(string="Days to Deliver")




    

    
