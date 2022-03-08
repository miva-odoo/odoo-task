# -*- coding: utf-8 -*-

from curses import resize_term
from odoo import models,fields,_,api


class ProductTemplate(models.Model):
    _inherit ='product.template'


    assign_sequence = fields.Boolean()
    
  
    # @api.model
    # def create(self,vals):            
    #     if vals.get('reference', _('New')) == _('New'):
    #         vals['reference'] = self.env['ir.sequence'].next_by_code('product.template') or _('New')
    #     res = super(ProductTemplate,self).create(vals)
    #     return res


    # @api.model
    # def create(self,vals): 
    #     res = super(ProductTemplate,self).create(vals)  
    #     for  rec in res:
    #         if res.categ_id and res.categ_id.assign_sequence:
    #             res.default_code = self.env['ir.sequence'].next_by_code('product.template') 
    #         return res
            
    @api.model
    def create(self,vals): 
        res = super(ProductTemplate,self).create(vals)  
        if res.categ_id and res.categ_id.assign_sequence:
                res.default_code = self.env['ir.sequence'].next_by_code('product.template')
        elif res.categ_id.parent_id :
                assign_sequence = []
                assign_sequence  = self.category_sequence(res.categ_id.parent_id,assign_sequence)
                if assign_sequence :
                    res.default_code = self.env['ir.sequence'].next_by_code('product.template') 

        return res

    def category_sequence(self, parent_category,assign_sequence):
        if parent_category.parent_id:
            assign_sequence.append(True)
            self.category_sequence(parent_category,assign_sequence)
        return assign_sequence



            

   