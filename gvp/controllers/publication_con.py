# -*- coding: utf-8 -*-

import re
from odoo import http
from odoo.http import request


class ContactControllerPub(http.Controller):


    @http.route('/my/get/publication', type='json', auth='user')
    def list_education(self, **kwargs):
        educations = request.env['publication'].search_read([], ['name'])
        partner = request.env.user.partner_id
        partner_publication = request.env.user.partner_id.publication_ids
        return {'educations': educations, 'partner': partner, 'partner_publication': partner_publication.ids}

    @http.route('/my/update/publications', type='json', auth='user')
    def update_educations(self, publication, **kwargs):
        publication = [int(publication) for publication in publication]
        return request.env.user.partner_id.write({'publication_ids': publication})

    @http.route('/my/edit/publication', type='http', auth='user', website=True)
    def edit_publication(self, **kwargs):
        publications = request.env['publication'].search([])
        return request.render('gvp.edit_publications',
                              {'publications ': publications , 'partner': request.env.user.partner_id})

    @http.route('/my/submit/publication', type='http', auth='user')
    def submit_educations(self, **kwargs):
        publications = kwargs.get('my_publication')
        if publications :
            publications = [int(publications ) for publications  in publications.split(',')]
            request.env.user.partner_id.write({'publication_ids': publications })
        else:
            request.env.user.partner_id.write({'publication_ids': False})
        return request.redirect('/my')