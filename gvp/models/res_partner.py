
# -*- coding: utf-8 -*-

from odoo import fields, models, api

class ResPartner(models.Model):
    _inherit = "res.partner"

    #----------------------------
    #  fields Declaration
    #---------------------------

    name = fields.Char()
    education_ids = fields.One2many('education', 'partner_id')
    experience_ids = fields.One2many('experience', 'partner_id')
    publication_ids = fields.One2many('publication', 'partner_id')
    volunteer_experience_ids = fields.One2many('volenteer.experience', 'partner_id')
    skills_ids = fields.Many2many('skill' ,string="Skill name")
   
