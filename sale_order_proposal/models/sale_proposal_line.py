# -*- coding: utf-8 -*-

from odoo import models,fields,api,_
from datetime import datetime, timedelta
from odoo.exceptions import AccessError, UserError, ValidationError


class SaleProposalLine(models.Model):
    _name = 'sale.proposal.line'
    _inherit = ['mail.thread', 'mail.activity.mixin']


    pr_id =fields.Many2one('sale.proposal')
    product_id = fields.Many2one(
        'product.product', string='Product',)


    order_id = fields.Many2one('sale.proposal', string='Order Reference', required=True, ondelete='cascade', index=True,
                               copy=False)
    name = fields.Text(string='Description', required=True)
    sequence = fields.Integer(string='Sequence', default=10)
    price_unit = fields.Float('Unit Price', required=True,  default=0.0)

    price_subtotal = fields.Char(string='Subtotal', store=True)
    price_tax = fields.Float( string='Total Tax', store=True)
    # price_total = fields.Monetary(string='Total', store=True)

    price_reduce = fields.Float(string='Price Reduce', digits='Product Price',
                                store=True)
    tax_id = fields.Many2many( string='Taxes',)
    product_uom_qty = fields.Float(string='Quantity', digits='Product Unit of Measure', required=True, default=1.0)

    # price_reduce_taxinc = fields.Monetary( string='Price Reduce Tax inc',
    #                                       store=True)
    # price_reduce_taxexcl = fields.Monetary( string='Price Reduce Tax excl',
    #                                        store=True)

    discount = fields.Float(string='Discount (%)', digits='Discount', default=0.0)

