# -*- coding: utf-8 -*-

import re
from odoo import http
from odoo.http import request


class ContactControllerEdu(http.Controller):

    # @http.route('/my/get/skills', type='json', auth='user')
    # def get_skills(self, **kwargs):
    #     skills = request.env['skill'].search_read([], ['name'])
    #     partner_skills = request.env.user.partner_id.skills_ids
    #     return {'skills': skills, 'partner_skills_ids': partner_skills.ids, 'partner_skills': partner_skills.mapped('name')}

    
    @http.route('/my/get/educations', type='json', auth='user')
    def list_education(self, **kwargs):
        educations = request.env['education'].search_read([], ['name'])
        partner = request.env.user.partner_id
        partner_education = request.env.user.partner_id.education_ids
        return {'educations': educations, 'partner': partner, 'partner_education': partner_education.ids}


    @http.route('/my/update/educations', type='json', auth='user')
    def update_educations(self, educations, **kwargs):
        educations = [int(education) for education in educations]
        return request.env.user.partner_id.write({'education_ids': educations})

    @http.route('/my/edit/educataions', type='http', auth='user', website=True)
    def edit_educataions(self, **kwargs):
        educataions = request.env['educataion'].search([])
        return request.render('gvp.edit_educataions', {'educataions': educataions, 'partner': request.env.user.partner_id})
        
    @http.route('/my/submit/educataion', type='http', auth='user')
    def submit_educations(self, **kwargs):
        educations = kwargs.get('my_educations')
        if educations:
            educations = [int(educations) for skill in educations.split(',')]
            request.env.user.partner_id.write({'education_ids': educations})
        else:
            request.env.user.partner_id.write({'education_ids': False})
        return request.redirect('/my')



    @http.route('/my/get/experiences', type='json', auth='user')
    def list_exp(self, **kwargs):
        experiences = request.env['experience'].search_read([], ['title'])
        partner = request.env.user.partner_id
        partner_experience = request.env.user.partner_id.experience_ids
        return {'experiences': experiences, 'partner': partner, 'partner_experiences': partner_experience.ids}


    @http.route('/my/update/experiences', type='json', auth='user')
    def update_exp(self, experiences, **kwargs):
        experiences = [int(experience) for experience in experiences]
        return request.env.user.partner_id.write({'experience_ids': experiences})

    @http.route('/my/edit/experiences', type='http', auth='user', website=True)
    def edit_exp(self, **kwargs):
        experiences = request.env['experiences'].search([])
        return request.render('gvp.edit_experiences', {'experiences': experiences, 'partner': request.env.user.partner_id})
        
    @http.route('/my/submit/experiences', type='http', auth='user')
    def submit_exp(self, **kwargs):
        experiences = kwargs.get('my_experiences')
        if experiences:
            experiences = [int(educations) for skill in educations.split(',')]
            request.env.user.partner_id.write({'education_ids': educations})
        else:
            request.env.user.partner_id.write({'education_ids': False})
        return request.redirect('/my')





    # @http.route('/my/delete/education/<model("education"):education>', type='http', auth='user', website=True)
    # def delete_education(self, education, **kwargs):
    #     education.unlink()
    #     return request.redirect('/my/list/education')




