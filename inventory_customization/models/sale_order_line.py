# -*- coding: utf-8 -*-

from odoo import models,fields,api



class SaleOrderLine(models.Model):
    _inherit ='sale.order.line'


    #------------------------
    #  fields Declaration
    #------------------------

    saleable_quantitiesed = fields.Float('Saleable Quantities',compute='_compute_saleable_qty')

   
    #------------------------
    #  method Declaration
    #------------------------
    @api.depends('product_id','product_id.property_stock_inventory')
    def _compute_saleable_qty(self):
        for line in self:
            location_ids = self.env['stock.location'].search([('is_saleable', '=', True)])
            quants = location_ids.quant_ids
            for quant in quants:
                if quant.product_id == line.product_id:
                   line.saleable_quantitiesed = line.product_id.qty_available
                else:
                    line.saleable_quantitiesed = 0.0
                  
    
        




       

 
   