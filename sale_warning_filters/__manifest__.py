{
#information
    
 'name':'Sale Warning Filters',
 'version': '15.0',
 'summary': 'Sale Warning Filters',
 'description': 'Sale Warning Filters',
 'category': 'custom',

# Author

 'author': 'odoo Ps',
 'website': 'https://www.odoo.com/',
 'license': '',

# Dependency
 'depends': [
  'stock',
  'sale_management',
 ],
 
 'data': [
  'views/order_sale_view.xml'
 ],

 # Other
 'installable': True,
 'auto_install': False,
}
