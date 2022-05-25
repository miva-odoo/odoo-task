
# -*- coding: utf-8 -*-

from odoo import models


class PurchaseOrder(models.Model): 
    _inherit ='purchase.order'

    
    def button_confirm(self):
        res = super(PurchaseOrder, self).button_confirm()
        for receipt in self.picking_ids:
            if self.partner_ref:
                receipt.origin += ' ( ' + self.partner_ref + ' )'
        return res

    # def _prepare_picking(self):
    #     res = super()._prepare_picking(self)
    #     print("______________________")
    #     for receipt in self.picking_ids:
    #         print("++++++++++++++++++++++")
    #         if self.partner_ref:
    #                 receipt.origin += ' ( ' + self.partner_ref + ' )'
    #     return res

