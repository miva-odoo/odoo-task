# -*- coding: utf-8 -*-

from odoo import models,fields,api



class SaleOrder(models.Model):
    _inherit ='sale.order'

  #-----------------------
  # method declaration
  #----------------------
     
    # def action_confirm(self):
    #     res = super(SaleOrder, self).action_confirm()
    #     for order in self:
    #         for line in order.order_line:
    #             is_saleble = line.product_id.property_stock_inventory.location_id.is_saleable
    #             print('>>>>>>>>>>>>>>>>> product', line.product_id.name)
    #             print('>>>>>>>>>>>>>>>>> product stock inv', line.product_id.property_stock_inventory)
    #             print('>>>>>>>>>>>>>>>>> location', line.product_id.property_stock_inventory.location_id.name)
    #             print('>>>>>>>>>>>>>>>>> is saleble', line.product_id.property_stock_inventory.location_id.is_saleable)
    #             # print('>>>>>>>>>>>>>>>>> is saleble', is_saleble)
    #             if is_saleble:
    #                 print('>>>>>>>>>>>>>>>if part run', line.product_id.qty_available)
    #                 line.saleable_quantitiesed = line.product_id.qty_available
    #             else:
    #                 print('>>>>>>>>>> else part >>>>>>>>>>>>>>.')
    #                 line.saleable_quantitiesed = 0.0
    #                 # line.saleable_quantitiesed = line.product_id.qty_available
    #     return res
#  print('>>>>>>>>>>>>>>>>> product', line.product_id.name)
                # print('>>>>>>>>>>>>>>>>> product stock inv', line.product_id.property_stock_inventory)
                # print('>>>>>>>>>>>>>>>>> location', line.product_id.property_stock_inventory.location_id.name)
                # print('>>>>>>>>>>>>>>>>> is saleble', line.product_id.property_stock_inventory.is_saleable)
                # print('>>>>>>>>>>>>>>>>> is saleble', is_saleble)