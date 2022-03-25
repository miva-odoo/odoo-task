# -*- coding: utf-8 -*-

import re
from odoo import http
from odoo.http import request


class ContactController(http.Controller):

    @http.route('/my/edit/skills', type='http', auth='user', website=True)
    def edit_skills(self, **kwargs):
        skills = request.env['skill'].search([])
        return request.render('gvp.edit_skills', {'skills': skills, 'partner': request.env.user.partner_id})

    @http.route('/my/submit/skills', type='http', auth='user')
    def submit_skills(self, **kwargs):
        request.env.user.partner_id.write({'skills_ids': [int(kwargs.get('skills'))]})
        return request.redirect('/my')