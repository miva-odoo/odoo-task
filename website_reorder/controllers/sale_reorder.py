# -- coding: utf-8 --

from odoo import http
from odoo.http import request

class SaleReorder(http.Controller):


    @http.route('/reorder', type='http', auth="user", website=True)
    def reorder(self, **kwargs):

        # rec = request.env['sale.order'].browse((kwargs.get('order_id')))

        rec = request.env['sale.order'].browse(int(kwargs.get('order_id')))
        order = request.website.sale_get_order()

        for res in rec.order_line:
            res.copy({'order_id':order.id})
        else:
            return http.request.redirect('/shop/cart')