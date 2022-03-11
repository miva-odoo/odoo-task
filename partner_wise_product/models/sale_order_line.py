# -- coding: utf-8 --

from odoo import models,fields,api


class SaleOrderLine(models.Model) :
    _inherit = 'sale.order.line'


    #-----------------------
    # method declaration
    #----------------------

    @api.onchange('product_id')
    def product_sale(self) :
       
        for rec in self :
            uom_details_ids = rec.order_id.partner_id.partner_wise_uoms_id
            for record in uom_details_ids:
                if rec.product_id == record.product_id:
                    rec.product_uom = record.uom_id
      
