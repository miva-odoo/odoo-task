{
    #  Information

    'name': 'Custom Report For Sale Order',
    'version': '15.0.0',
    'summary': 'Custom Report For Sale Order',
    'description': "Custom Report For Sale Order",
    'category': 'custom',

    # Author

    'author': 'Odoo PS',
    'website': 'https://www.odoo.com',

    # Dependency
    
    'depends': ['sale_management'],
    'data': [
        'reports/sale_order_report.xml' ,
        'reports/sale_order_report_template.xml' ,
    ],

    # Other
    'installable': True,
    'auto_install': False,
   

} 