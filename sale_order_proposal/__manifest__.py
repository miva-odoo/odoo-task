{
#information
    
 'name':'Sale Order Proposal',
 'version': '15.0',
 'summary': 'Sale Order Proposal',
 'description': 'Sale Order Proposal',
 'category': 'custom',

# Author

 'author': 'odoo Ps',
 'website': 'https://www.odoo.com/',
 'license': '',

# Dependency
 'depends': ['sale_management'],
 
 'data': [
  'views/sale_proposal_menu.xml',
  'views/sale_proposal_view.xml',
  'views/sale_proposal_line_view.xml',
  'security/ir.model.access.csv',
  'data/product_template_sequence.xml'
 ],

 # Other
 'installable': True,
 'auto_install': False,
}
