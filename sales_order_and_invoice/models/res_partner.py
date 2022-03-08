# -*- coding: utf-8 -*-

from odoo import fields,models


class ResPartner(models.Model):
    _inherit='res.partner'

    #----------------------------
    #  fields Declaration
    #---------------------------

    partner_wise_uoms_id = fields.One2many('partner.wise.uom','partner_id')
    

	
    
   

    



    

    
