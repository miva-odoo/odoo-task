{
#information
    
 'name':'Sale Config Custom',
 'version': '15.0',
 'summary': 'Sale Config Custom',
 'description': 'Sale Config Custom',
 'category': 'custom',

# Author

 'author': 'odoo Ps',
 'website': 'https://www.odoo.com/',
 'license': '',

# Dependency
 'depends': ['sale_management','stock',],
 'data': [
     'views/res_config_settings_view.xml',
     'views/sale_order_view.xml',

        
 ],

 # Other
 'installable': True,
 'auto_install': False,
}
