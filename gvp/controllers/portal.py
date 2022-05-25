# -*- coding: utf-8 -*-

from odoo.addons.portal.controllers.portal import CustomerPortal
from odoo.http import request


class GvpCustomerPortal(CustomerPortal):

    def _prepare_portal_layout_values(self):
        res = super()._prepare_portal_layout_values()
        res.update({
            'partner': request.env.user.partner_id,
            'education': request.env.user.partner_id.education_ids,
            'experience': request.env.user.partner_id.experience_ids,
            'skills': request.env.user.partner_id.skills_ids,
            'publication': request.env.user.partner_id.publication_ids,
            'vol_experience': request.env.user.partner_id.volunteer_experience_ids,
            
        })
        return res
