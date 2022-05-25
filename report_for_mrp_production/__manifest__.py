{
#information
    
 'name':'Report for Mrp Production',
 'version': '15.0',
 'summary': 'Report for Mrp Production',
 'description': 'Report for Mrp Production',
 'category': 'custom',

# Author

 'author': 'odoo Ps',
 'website': 'https://www.odoo.com/',
 'license': '',

# Dependency
 'depends': [
     'mrp',
 ],
 
 'data': [
     'reports/mrp_production_report.xml',
     'reports/mrp_production_report_template.xml',
 ],

 # Other
 'installable': True,
 'auto_install': False,
}
