{
#information
    
 'name':'General Ledger report',
 'version': '15.0',
 'summary': 'General Ledger report',
 'description': 'General Ledger report',
 'category': 'custom',

# Author

 'author': 'odoo Ps',
 'website': 'https://www.odoo.com/',
 'license': '',

# Dependency
 'depends': [
     'account_accountant',
 ],
 
 'data': [
     'views/account_move_views.xml',
     
    
 ],

 # Other
 'installable': True,
 'auto_install': False,
}
