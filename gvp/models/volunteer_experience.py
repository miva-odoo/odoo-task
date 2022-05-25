# -*- coding: utf-8 -*-

from odoo import models, fields

class VolenteerExperience(models.Model):
    _name = 'volenteer.experience'

    #----------------------------
    #  fields Declaration
    #---------------------------

    partner_id = fields.Many2one('res.partner')
    name = fields.Char('Organization Name')
    role = fields.Char('Role Name')
    is_currently = fields.Boolean('I Am Currently in this role')
    start_date = fields.Datetime()
    end_date = fields.Datetime()
