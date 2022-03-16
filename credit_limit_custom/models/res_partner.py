# -*- coding: utf-8 -*-

from odoo import fields,models,api


class ResPartner(models.Model):
    _inherit='res.partner'

    #----------------------------
    #  fields Declaration
    #---------------------------

    credit_limit = fields.Float(string="Credit Limit")


    def name_search(self, name='', args=None, operator='ilike', limit=100):
        args = args or []
        domain = []
        if name:
            domain = ['|','|',('name',operator,name),('phone',operator,name),('email',operator,name)]
        return self._search(domain + args,limit=limit,access_rights_uid = name_get_uid)
       



    

    
