{
#information
    
 'name':'Custom Xlsx Report For Sale',
 'version': '15.0',
 'summary': 'Custom Xlsx Report For Sale',
 'description': 'Custom Xlsx Report For Sale',
 'category': 'custom',

# Author

 'author': 'odoo Ps',
 'website': 'https://www.odoo.com/',
 'license': '',

# Dependency
 'depends': [
     'sale',
     'report_xlsx',
 ],
 
 'data': [
     'reports/sale_order_report.xml',
     
    
 ],

 # Other
 'installable': True,
 'auto_install': False,
}
