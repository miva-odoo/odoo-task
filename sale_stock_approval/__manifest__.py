{
#imfromation
    
 'name':'Sale Stock Approval',
 'version': '15.0',
 'summary': 'Sale Stock Approval',
 'description': 'Sale Stock Approval',
 'category': 'custom',

# Author

 'author': 'odoo Ps',
 'website': 'https://www.odoo.com/',
 'license': '',

# Dependency
 'depends': ['contacts','sale_management','delivery_barcode','stock',],
 'data': [
     'views/order_sale_view.xml',
    
 ],

 # Other
 'installable': True,
 'auto_install': False,
}
