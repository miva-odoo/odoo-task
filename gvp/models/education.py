# -*- coding: utf-8 -*-

from odoo import models, fields

class Education(models.Model):
    _name = 'education'

    #----------------------------
    #  fields Declaration
    #---------------------------

    partner_id = fields.Many2one('res.partner')
    name = fields.Char('Education Name')
    year = fields.Char('Passing Years')
    percentage = fields.Float('Percentage')
    start_date = fields.Datetime()
    end_date = fields.Datetime()
    college = fields.Text()
