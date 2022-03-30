# -*- coding: utf-8 -*-

from odoo import models,fields,api
from odoo.exceptions import UserError


class ProductTemplate(models.Model): 
    _inherit ='product.template'


    #------------------------
    #  fields Declaration
    #------------------------

    barcode_print = fields.Char(string="Barcode Label")


    def barcode_label_print(self):
        action = self.env['ir.actions.report']._for_xml_id('sale_customization_barcode.custom_report_second_report')
        action['context'] = {'default_product_ids': self.ids}
        return action
