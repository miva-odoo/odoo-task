{
#imfromation
    
 'name':'Credit Limit Custom',
 'version': '15.0',
 'summary': 'Credit Limit Custom',
 'description': 'Credit Limit Custom',
 'category': 'custom',

# Author
 'author': 'odoo Ps',
 'website': 'https://www.odoo.com/',
 'license': '',

# Dependency
 'depends': ['contacts','sale_management'],
 'data': [
     'views/res_partner_view.xml',
    
     
 ],

 # Other
 'installable': True,
 'auto_install': False,
}