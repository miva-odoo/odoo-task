# -*- coding: utf-8 -*-

{
    #  Information
    'name':'Report Qweb Txt Custom',
    'version': '14.0',
    'summary': 'Report Qweb Txt Custom',
    'description':'Report Qweb Txt Custom',
    'category':'',

    # Author
    'author': 'Odoo Ps',
    'website': 'https://www.odoo.com/',
    'license': '',
    
    # Dependency
    'data':[
        'reports/sale_order_report.xml',
        'reports/report.xml',
        'reports/sale_invoice_template.xml',
        'reports/sale_invoice_return.xml',
        'views/sale_order_menu.xml',
        'wizard/sale_order_wizard.xml',
        'security/ir.model.access.csv',
    ],
    'depends':['sale_management'],
    'demo':[],
    
    # Other
    'application':True,
    'installble':True,
}