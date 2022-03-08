{
#imfromation
    
 'name':'Product Unique Code',
 'version': '15.0',
 'summary': 'Product Unique Code',
 'description': 'Product Unique Code',
 'category': 'custom',

# Author
 'author': 'odoo Ps',
 'website': 'https://www.odoo.com/',
 'license': '',

# Dependency
 'depends': ['contacts','sale_management'],
 'data': [
     'views/product_category_view.xml',
    #  'views/product_template_view.xml',
     'data/product_template_sequence.xml',
     
 ],

 # Other
 'installable': True,
 'auto_install': False,
}