{
#information
    
 'name':'Sale Custom Barcode',
 'version': '15.0',
 'summary': 'Sale Custom Barcode',
 'description': 'Sale Custom Barcode',
 'category': 'custom',

# Author

 'author': 'odoo Ps',
 'website': 'https://www.odoo.com/',
 'license': '',

# Dependency
 'depends': [
     'sale_management',
     'stock',
 ],
 
 'data': [
     'views/product_template_view.xml',
     'reports/barcode_label_template.xml',
     'reports/product_report.xml',
     
    
 ],

 # Other
 'installable': True,
 'auto_install': False,
}
