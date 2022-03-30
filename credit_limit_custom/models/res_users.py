# -*- coding: utf-8 -*-

from odoo import fields,models,api


class ResUser(models.Model):
    _inherit='res.users'

    #----------------------------
    #  method Declaration
    #---------------------------


    def name_get(self):
        res = []
        for user in self:
            name = user.name +' : '+ user.login
            res.append((user.id, name))
        return res      


