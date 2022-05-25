from odoo import api, fields, models, _

from odoo.exceptions import UserError



class ConfirmOrder(models.TransientModel):
    _name = 'confirm.order'
    _description = 'Confirm order'

    order_name =  fields.Char()
    sale_order_id = fields.Many2one('sale.order',readonly=True)

    
    def action_confirm_wizard(self):
        sale_order = self._context.get('active_ids')
        quotations_ids = self.env['sale.order'].browse(sale_order).\
            filtered(lambda res: res.state == 'draft' or res.state == "sent")
        for sale_order in quotations_ids:
            sale_order.action_confirm()
