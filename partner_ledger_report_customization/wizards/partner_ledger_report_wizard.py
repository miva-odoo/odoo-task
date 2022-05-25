# -- coding: utf-8 --

from odoo import models,fields


class PartnerLedgerReportWizard(models.TransientModel):
    
    _name = 'partner.ledger.report.wizard'
    _description = 'Partner Ledger Report Wizard'

    # ==========================
    # Field Declaration
    # ==========================

    partner_id = fields.Many2many('res.partner')
    from_date = fields.Date()
    to_date = fields.Date()
    value = fields.Selection([
        ('detailed', 'Detailed'),
        ('summary', 'Summary')], default="detailed")

    # ==========================
    # Method Declaration
    # ==========================

    def pertner_ledger_report_wizard(self):
        return self.env.ref('partner_ledger_report_customization.partner_ledger_report').report_action(self)