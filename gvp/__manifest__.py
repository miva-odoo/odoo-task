{
    #information
    'name': 'Gvp Csaa',
    'summary':'Gvp Csaa',
    'description':'vGvp Csaa',
    'category': 'sales',

    # Dependency
    'data': [
        'views/gvp_portal_menu.xml',
        'views/res_partner_view.xml',
        'views/skill_view.xml',
        'views/education_view.xml',
        'views/experience_view.xml',
        'views/gvp_portal_templates.xml',
        'security/ir.model.access.csv',
    ],
    'depends': [
        'account',
        'contacts',
        'website'
    ],
    
    # Other
    'installable': True,
    'auto_install': False,
    'application': True,
    'license': 'LGPL-3',
}
