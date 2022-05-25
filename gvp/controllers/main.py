# -*- coding: utf-8 -*-

from odoo import http
from odoo.http import request


class ContactController(http.Controller):

    @http.route('/my/get/skills', type='json', auth='user')
    def get_skills(self, **kwargs):
        skills = request.env['skill'].search_read([], ['name'])
        partner_skills = request.env.user.partner_id.skills_ids
        return {'skills': skills, 'partner_skills_ids': partner_skills.ids, 'partner_skills': partner_skills.mapped('name')}

    @http.route('/my/update/skills', type='json', auth='user')
    def update_skills(self, skills, **kwargs):
        skills = [int(skill) for skill in skills]
        return request.env.user.partner_id.write({'skills_ids': skills})

    @http.route('/my/edit/skills', type='http', auth='user', website=True)
    def edit_skills(self, **kwargs):
        skills = request.env['skill'].search([])
        return request.render('gvp.edit_skills', {'skills': skills, 'partner': request.env.user.partner_id})

    @http.route('/my/submit/skills', type='http', auth='user')
    def submit_skills(self, **kwargs):
        skills = kwargs.get('my_skills')
        if skills:
            skills = [int(skill) for skill in skills.split(',')]
            request.env.user.partner_id.write({'skills_ids': skills})
        else:
            request.env.user.partner_id.write({'skills_ids': False})
        return request.redirect('/my')