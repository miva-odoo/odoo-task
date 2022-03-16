# -*- coding: utf-8 -*-

from datetime import datetime
from odoo import fields,models,api


class StockQuant(models.Model):
    _inherit='stock.quant'

    #----------------------------
    #  fields Declaration
    #---------------------------

    ageing_date = fields.Date(string="Ageing Date")
    ageing_period = fields.Selection([
        ('zero_to_thirty', 'zero_to_thirty'),
        ('thirty_to_sixty', 'thirty_to_sixty'),
        ('sixty_to_ninety', 'sixty_to_ninety'),
        ('niety_to_one_hundred_twenty', 'niety_to_one_hundred_twenty'),
        ('one_hundred_twenty_to_max', 'one_hundred_twenty_to_max')
    ])

    #----------------------------
    #  method Declaration
    #---------------------------
    
    def _set_ageing_period(self):
        qunats = self.env['stock.quant'].search([])
        ageing_date = datetime.now().date()
        for record in qunats:
            days = ageing_date - record.create_date.date()
            day = days.days  
            if 0 <= day <= 30:
                record.ageing_period = 'zero_to_thirty'
            elif 31 <= day <= 60:
                record.ageing_period = 'thirty_to_sixty'
            elif 61 <= day <= 90:
                record.ageing_period = 'sixty_to_ninety'
            elif 91 <= day <= 120:
                record.ageing_period = 'niety_to_one_hundred_twenty'
            else:
               record.ageing_period = 'one_hundred_twenty_to_max' 

       
       
       
    
           

               
                         


        

             