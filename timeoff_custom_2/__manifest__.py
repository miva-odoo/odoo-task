# -*- coding: utf-8 -*-
{
    #  Information
    'name':'TimeOff Custom',
    'version': '15.0',
    'summary': 'TimeOff Custom',
    'description':'TimeOff Custom',
    'category':'',

    # Author
    'author': 'Odoo Ps',
    'website': 'https://www.odoo.com/',
    'license': '',
    
    # Dependency
    'data':[
        'views/time_portal_templates.xml',
        ],
    'depends':['website','hr_holidays'],
    'demo':[],
    
    # Other
    'application':True,
    'installble':True,
}