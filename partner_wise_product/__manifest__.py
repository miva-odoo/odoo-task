{
#imfromation
    
 'name':'Sales Order and Invoice',
 'version': '15.0',
 'summary': 'Sales Order and Invoice',
 'description': 'Sales Order and Invoice',
 'category': 'custom',

# Author
 'author': 'odoo Ps',
 'website': 'https://www.odoo.com/',
 'license': '',

# Dependency
 'depends': ['contacts','sale_management'],
 'data': [
     'views/res_partner_view.xml',
     'security/ir.model.access.csv',
     
 ],

 # Other
 'installable': True,
 'auto_install': False,
}