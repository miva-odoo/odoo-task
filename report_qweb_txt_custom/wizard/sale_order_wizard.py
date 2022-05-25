# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _
from odoo.exceptions import UserError


class PosDetails(models.TransientModel):
    _name = 'sale.details.wizard'
    _description = 'Sale Details Report'

    def _default_start_date(self):
        """ Find the earliest start_date of the latests sessions """
        # restrict to configs available to the user
        # config_ids = self.env['account.move'].search([]).ids
        # exclude configs has not been opened for 2 days
        # self.env.cr.execute("""
        #     SELECT
        #     max(start_at) as start,
        #     config_id
        #     FROM pos_session
        #     WHERE config_id = ANY(%s)
        #     AND start_at > (NOW() - INTERVAL '2 DAYS')
        #     GROUP BY config_id
        # """, (config_ids,))
        # latest_start_dates = [res['start'] for res in self.env.cr.dictfetchall()]
        # # earliest of the latest sessions
        # return latest_start_dates and min(latest_start_dates) or fields.Datetime.now()

    start_date = fields.Datetime(required=True, default=_default_start_date)
    end_date = fields.Datetime(required=True, default=fields.Datetime.now)
    partner_id =fields.Many2one('res.partner')
    order_name = fields.Char("Report")

    # @api.onchange('partner_id')
    # def get_pending_so_values(self):
    #     print('>>>>>>>>>>>>>>>>>>>>>>>>>')
    #     # sale_order = self.env['sale.oder'].search(['partner_id' , '=',14 ])
    #     sale_order = self.env['account.move'].search([('partner_id', '=', self.partner_id.id)])
    #     print('sale order recode:;;;;;;;;',  sale_order)
    #     if self.partner_id:
    #         self.order_name = sale_order/nnmnm mnjnjnjnjnjnjjmnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnm

    def print_report(self):
        action = self.env['ir.actions.report']._for_xml_id('report_qweb_txt_custom.account_move_report_custom')
        # action['context'] = {'default_partner_ids': self.ids}
        return action

    @api.onchange('start_date')
    def _onchange_start_date(self):
        pass
        # if self.start_date and self.end_date and self.end_date < self.start_date:
        #     self.end_date = self.start_date

    @api.onchange('end_date')
    def _onchange_end_date(self):
        pass
        # if self.end_date and self.end_date < self.start_date:
        #     self.start_date = self.end_date

    # def generate_report(self):
    #     data = {'date_start': self.start_date, 'date_stop': self.end_date, 'config_ids': self.pos_config_ids.ids}
    #     return self.env.ref('point_of_sale.sale_details_report').report_action([], data=data)
