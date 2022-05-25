# -*- coding: utf-8 -*-


from odoo import models, fields

class Publication(models.Model):
    _name = 'publication'

    #----------------------------
    #  fields Declaration
    #---------------------------

    partner_id = fields.Many2one('res.partner')
    name = fields.Char('Publication Name')
    author = fields.Char('Authore')
    discription = fields.Char('Discription')

