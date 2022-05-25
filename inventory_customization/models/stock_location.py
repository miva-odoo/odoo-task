
# -*- coding: utf-8 -*-


from odoo import models,fields


class StockLocation(models.Model): 
    _inherit ='stock.location'

    #------------------------
    #  fields Declaration
    #------------------------
    
    is_saleable =fields.Boolean(string="Saleable Quantities")
