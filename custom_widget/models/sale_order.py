# -*- coding: utf-8 -*-

from odoo import models,fields,api
import datetime


class SaleOrder(models.Model):
    _inherit ='sale.order'


    #------------------------
    #  fields Declaration
    #------------------------

    miva = fields.Char(string='MIVA')

