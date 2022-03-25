
# -*- coding: utf-8 -*-

from odoo import fields, models, api

class ResPartner(models.Model):
    _inherit = "res.partner"


    #----------------------------
    #  fields Declaration
    #---------------------------

    name = fields.Char()
    education_ids = fields.One2many('education', 'partner_id')
    experience_ids = fields.One2many('experience', 'employee_id')
    skills_ids = fields.Many2many('skill' ,string="Skill name")
   
