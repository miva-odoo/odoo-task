{
#information
 'name':'Custom Sale Order Report',
 'version': '15.0',
 'summary': 'Custom Sale Order Report',
 'description': 'Custom Sale Order Report',
 'category': 'custom',

# Author

 'author': 'odoo Ps',
 'website': 'https://www.odoo.com/',
 'license': '',

# Dependency
 'depends': [
     'sale_management',
 ],
 
 'data': [
     'view/order_sale_view.xml',    
 ],

 # Other
 'installable': True,
 'auto_install': False,
}
