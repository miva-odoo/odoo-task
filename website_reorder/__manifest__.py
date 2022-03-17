{
#information
  
 'name':'Reorder ON Website',
 'version': '15.0',
 'summary': 'Reorder ON Website',
 'description': 'Reorder ON Website',
 'category': 'custom',

# Author
 'author': 'odoo Ps',
 'website': 'https://www.odoo.com/',
 'license': '',

# Dependency
 'depends': ['website','sale_management','website_sale',],
 'data': [
     'views/sale_order_protal_template.xml',
     'data/email_template_data.xml',
    
 ],

 # Other
 'installable': True,
 'auto_install': False,
}