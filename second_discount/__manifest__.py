{
#information
    
 'name':'Second Discount',
 'version':'15.0',
 'summary':'Second Discount',
 'description':'Second Discount',
 'category':'custom',

# Author
 'author': 'odoo Ps',
 'website':'https://www.odoo.com/',
 'license':'',

# Dependency
 'depends': ['contacts','sale_management'],
 'data': [
     'views/sale_order_view.xml', 
     'views/account_move_view.xml',
     'reports/sale_report_saleorder.xml',
     'reports/account_report_invoice_with_payments_report.xml',
 ],

 # Other
 'installable': True,
 'auto_install': False,
}
