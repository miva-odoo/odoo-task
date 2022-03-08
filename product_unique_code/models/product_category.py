
# -*- coding: utf-8 -*-

from odoo import models,fields,api



class ProductCategory(models.Model):
    _inherit ='product.category'


    #------------------------
    #  fields Declaration
    #------------------------

    assign_sequence = fields.Boolean()

    #-----------------------
    # method declaration
    #----------------------
    
   