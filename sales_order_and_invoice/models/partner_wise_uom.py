# -*- coding: utf-8 -*-

from odoo import fields,models

class PartnerWiseUom(models.Model):
	_name = 'partner.wise.uom'


	#----------------------------
    #  fields Declaration
    #---------------------------

	partner_id = fields.Many2one('res.partner')
	product_id = fields.Many2one('product.product')
	uom_id = fields.Many2one('uom.uom', domain="[('category_id','=', category_uom_ids)]")
	category_uom_ids = fields.Many2one(related="product_id.uom_id.category_id")
	

