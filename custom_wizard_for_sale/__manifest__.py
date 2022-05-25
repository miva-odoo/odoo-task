{
#information
    
 'name':'Custom Wizard For Sale',
 'version': '15.0',
 'summary': 'Custom Wizard For Sale',
 'description': 'Custom Wizard For Sale',
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
     'views/order_sale_view.xml',
     'wizards/confiem_order_view.xml',
     'security/ir.model.access.csv',
    
 ],

 # Other
 'installable': True,
 'auto_install': False,
}
