{
    #  Information

    'name': 'Partner Ledger Report Customization',
    'version': '15.0.0',
    'summary': 'Partner Ledger Report Customization',
    'description': """
        Partner Ledger Report Customization """,
    'category': 'Sales',

    # Author

    'author': 'Odoo PS',
    'website': 'https://www.odoo.com',

    # Dependency
    
    'depends': ['account'],
    'data': [
        'security/ir.model.access.csv' ,
        'reports/report.xml' ,
        'reports/report_template.xml' ,
        'views/account_move_views.xml' ,
        'wizards/partner_ledger_report_wizard.xml'
    ],

    # Other
    'installable': True,
    'auto_install': False,
    'application' : True,

} 