from odoo import http
from odoo.http import request
from odoo import fields, http, SUPERUSER_ID, _
from odoo.addons.portal.controllers.portal import pager as portal_pager, get_records_pager
from odoo.addons.portal.controllers import portal


class TimeOffcontroller(portal.CustomerPortal):
    def _prepare_home_portal_values(self, counters):
        values = super()._prepare_home_portal_values(counters)
        partner = request.env.user.partner_id

        HrLeave = request.env['hr.leave']
        if 'leave_count' in counters:
            values['leave_count'] = HrLeave.search_count([
                ('message_partner_ids', 'child_of', [partner.commercial_partner_id.id]),
                ('state', 'in', ['draft', 'confirm','refused','validate1','validate'])
            ]) if HrLeave.check_access_rights('read', raise_exception=False) else 0
        return values
    
    @http.route(['/my/timeoff', '/my/timeoff/page/<int:page>'], type='http', auth="user", website=True)
    def portal_my_timeoff(self, page=1, date_begin=None, date_end=None, sortby=None, **kw):
        values = self._prepare_portal_layout_values()
        partner = request.env.user.partner_id
        HrLeave = request.env['hr.leave']
        
        domain = [
            ('message_partner_ids', 'child_of', [partner.commercial_partner_id.id]),
            ('state', 'in', ['draft', 'confirm','refused','validate1','validate'])
        ]
        leave_count = HrLeave.search_count(domain)
        pager = portal_pager(
            url="/my/timeoff",
            total=leave_count,
            page=page,
        )
        res = request.env['hr.leave'].search([('employee_ids','=',request.env.user.name)])
        values.update({
           
            'res': res.sudo(),
            'pager': pager,
            'default_url': '/my/timeoff',
        })
        return request.render('timeoff_custom.portal_my_timeoff_details', values,{'res':res})
        

