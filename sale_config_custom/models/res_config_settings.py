# -*- coding: utf-8 -*-

from odoo import models,fields,api


class ResConfigSettings(models.TransientModel): 
    _inherit ='res.config.settings'


    #------------------------
    #  fields Declaration
    #------------------------

    is_sale_user = fields.Boolean(config_parameter='sale_config_custom.user_test')
    user_id = fields.Many2one('res.users',config_parameter='sale_config_custom.user_id')
    


   
    