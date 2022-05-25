# -*- coding: utf-8 -*-

from odoo import models, fields

class GvpEducation(models.Model):
    _name = 'experience'

    #----------------------------
    #  fields Declaration
    #---------------------------

    partner_id = fields.Many2one('res.partner')
    title = fields.Char('Experience Title')
    employee_type = fields.Char('Employee Type')
    employee_name = fields.Char('Employee Name')
    start_date = fields.Datetime()
    end_date = fields.Datetime()
    industry_name = fields.Char()
    description = fields.Text()
