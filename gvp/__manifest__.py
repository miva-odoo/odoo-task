# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    #information
    'name': 'Gvp Csaa',
    'summary':'Gvp Csaa',
    'description':'Gvp Csaa',
    'category': 'sales',

    # Dependency
    'data': [
        'views/gvp_portal_menu.xml',
        'views/res_partner_view.xml',
        'views/skill_view.xml',
        'views/education_view.xml',
        'views/experience_view.xml',
        'views/publication_view.xml',
        'views/volunteer_experience_view.xml',
        'views/gvp_portal_templates.xml',
        'views/education_template_edit.xml',
        'security/ir.model.access.csv',

    ],
    'assets': {
        'web.assets_frontend': [
            'gvp/static/src/js/skills.js',
            'gvp/static/src/js/educations.js',
            'gvp/static/src/js/ex.js',
            'gvp/static/src/js/publication.js',
            'gvp/static/src/xml/skills.xml',
            'gvp/static/src/xml/education.xml',
            'gvp/static/src/xml/publication.xml',
        ],
        'web.assets_qweb': [
            'gvp/static/src/xml/skills.xml',
            'gvp/static/src/xml/education.xml',
        ],
    },        
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
