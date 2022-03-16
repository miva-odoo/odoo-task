{
#infromation
    
 'name':'Stock Aageing Costomization',
 'version':'15.0',
 'summary':'Stock Aageing Costomization',
 'description':'Stock Aageing Costomization',
 'category':'custom',

# Author
 'author': 'odoo Ps',
 'website':'https://www.odoo.com/',
 'license':'',

# Dependency
 'depends': ['stock'],
 'data': [
     'views/stock_quant_view.xml', 
     'data/ageing_period_cron.xml'
     
 ],

 # Other
 'installable': True,
 'auto_install': False,
}
