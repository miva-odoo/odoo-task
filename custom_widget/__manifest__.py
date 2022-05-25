{
#information
    
 'name':'Custom Widget',
 'version': '15.0',
 'summary': 'Custom Widget',
 'description': 'Custom Widget',
 'category': 'custom',

# Author





 'website': 'https://www.odoo.com/',
 'license': '',

# Dependency
 'depends': [
     'sale_management',
 ],
 
 'data': [
     'views/order_sale_view.xml',
    #  'views/account_move_view.xml',
     
    
 ],

 'assets': {
     'web.assets_backend': [
            'custom_widget/static/src/legacy/scss/miva_ribbon.scss',
            'custom_widget/static/src/legacy/js/widgets/miva_ribbon.js',    
        ],
    },
        
 # Other
 'installable': True,
 'auto_install': False,
}
