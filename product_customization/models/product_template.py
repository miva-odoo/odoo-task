# -*- coding: utf-8 -*-

from odoo import models,fields,api


class ProductTemplate(models.Model): 
    _inherit ='product.template'


    #------------------------
    #  fields Declaration
    #------------------------

    internal_refence_miva = fields.Char('Internal Reference New', compute='_compute_default_miva',
        inverse='_set_default_miva', store=True)
    


    @api.depends('product_variant_ids', 'product_variant_ids.internal_refence_miva')
    def _compute_default_miva(self):
        unique_variants = self.filtered(lambda template: len(template.product_variant_ids) == 1)
        for template in unique_variants:
            template.internal_refence_miva = template.product_variant_ids.internal_refence_miva
        for template in (self - unique_variants):
            template.internal_refence_miva = False

    def _set_default_miva(self):
        for template in self:
            if len(template.product_variant_ids) == 1:
                template.product_variant_ids.internal_refence_miva = template.internal_refence_miva
    

    # @api.model_create_multi
    # def create(self,vals_list): 
    #     res = super(ProductTemplate,self).create(vals_list)
    #     for  vals in zip(vals_list):
    #         related_vals = {}
    #     if vals.get('internal_refence_miva'):
    #             related_vals['internal_refence_miva'] = vals['internal_refence_miva']
    #     if related_vals:
    #             res.write(related_vals)
    #     return res


    @api.model_create_multi
    def create(self, vals_list):
        templates = super(ProductTemplate, self).create(vals_list)
        for template, vals in zip(templates, vals_list):
            related_vals = {}
            if vals.get('internal_refence_miva'):
                related_vals['internal_refence_miva'] = vals['internal_refence_miva']
            if related_vals:
                template.write(related_vals)
        return templates


        

   