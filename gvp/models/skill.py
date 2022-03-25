
# -*- coding: utf-8 -*-

from odoo import models, fields

class Skill(models.Model):
    _name = 'skill'


    #----------------------------
    #  fields Declaration
    #---------------------------

    skill_id = fields.Many2one('res.partner')
    name = fields.Char(string="Skill Name")

