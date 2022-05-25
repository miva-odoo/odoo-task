from odoo import http
from odoo.http import request
from odoo.addons.portal.controllers import portal

class MyCustomerPortal(portal.CustomerPortal):
    
   def _prepare_home_portal_values(self, counters):
        values = super()._prepare_home_portal_values(counters)
        partner = request.env.user.partner_id

        HrLeave = request.env['hr.leave']
        print('>>>>>>>>>>>>>>>', counters)
        # if 'leave_count' in counters:
        values['leave_count'] = HrLeave.search_count([])
            # ]) if HrLeave.check_access_rights('read', raise_exception=False) else 0
        return values
        
    # def _prepare_home_portal_values(self, counters):
    #     values = super()._prepare_home_portal_values(counters)
    #     res = request.env['hr.leave'].search([('employee_ids','=',request.env.user.name)])
    #     values['len_hr'] = 4
    #     return values