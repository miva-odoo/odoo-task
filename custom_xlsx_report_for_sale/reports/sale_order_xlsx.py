# -*- coding: utf-8 -*-

from odoo import models
class SaleOrderXlsx(models.AbstractModel):
    _name = 'report.custom_xlsx_report_for_sale.custom_report_testing_xls'
    _inherit = 'report.report_xlsx.abstract'
    def generate_xlsx_report(self, workbook, data, sale):
        sheet = workbook.add_worksheet('Sale Oder Detail')
        bold = workbook.add_format({'bold': True})
        format_1 = workbook.add_format({'bold': True,'align':'center','bg_color':'blue'})
        row = 3
        col = 3
        # sheet.set_column('D:E',30)
        sheet.set_column('D:D',15)
        for obj in sale:
            row += 1
            sheet.merge_range(row,col,row,col + 1, '---Sale Order Details--- ',format_1)

            row += 1
            sheet.write(row,col, 'Sale Order NO :- ', bold)
            sheet.write(row,col + 1, obj.name)
            
            row += 1
            sheet.write(row,col, 'Date :- ', bold)
            sheet.write(row,col + 1, obj.date_order)

            row += 3

            # row += 1 
            # sheet.write(row,col, 'Patner Address :- ', bold)
            # sheet.write(row,col + 1, obj.message_ids)