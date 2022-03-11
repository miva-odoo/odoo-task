
# -*- coding: utf-8 -*-

from odoo import models,fields,api
import datetime


class SaleOrderLine(models.Model):
    _inherit ='account.move.line'


    #------------------------
    #  fields Declaration
    #------------------------

    second_discount = fields.Float(string="2nd Disc. %" )

    





