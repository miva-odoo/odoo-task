# -- coding: utf-8 --

from odoo import models , fields , api
from odoo.exceptions import UserError


class SaleOrder(models.Model):
    _inherit = 'sale.order'


   