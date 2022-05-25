# -- coding: utf-8 --

from odoo import models


class AccountMove(models.Model):

    _inherit = 'account.move'

    # ==========================
    # Method Declaration
    # ==========================
    
    def get_sale_order_ref(self):
        sale_id = self.invoice_line_ids.sale_line_ids.order_id
        return sale_id or False
