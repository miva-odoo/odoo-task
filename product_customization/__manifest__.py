{
#information
    
 'name':'Product Customization',
 'version': '15.0',
 'summary': 'Product Customization',
 'description': 'Product Customization',
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
     'views/product_template_view.xml',
     'views/product_product_view.xml',
    
 ],

 # Other
 'installable': True,
 'auto_install': False,
}
