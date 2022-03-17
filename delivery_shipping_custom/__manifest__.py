{
#information
    
 'name':'Delivery Shipping Sale',
 'version':'15.0',
 'summary':'Delivery Shipping For sale',
 'description':'Delivery Shipping For sale',
 'category':'custom',

# Author
 'author': 'odoo Ps',
 'website':'https://www.odoo.com/',
 'license':'',

# Dependency
 'depends': ['contacts','sale_management','delivery_barcode','stock','account_accountant'],
 'data': [
    #  'views/res_partner_view.xml',
     'views/order_sale.xml',
     'views/stock_picking.xml',
 ],

 # Other
 'installable': True,
 'auto_install': False,
}