{
#information
    
 'name':'Inventory Customization',
 'version': '15.0',
 'summary': 'Inventory Customization',
 'description': 'Inventory Customization',
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
    'views/stock_location_view.xml',
    'views/sale_order_view.xml',
    
 ],

 # Other
 'installable': True,
 'auto_install': False,
}
