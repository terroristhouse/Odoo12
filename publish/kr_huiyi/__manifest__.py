# -*- coding: utf-8 -*-
{
    'name': "会议管理",

    'summary': """
        会议室使用情况""",

    'description': """
        会议室使用情况
    """,

    'author': "刘飞",
    'website': "/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],
    'application': True,

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/meeting_main_view.xml',
        'views/meeting_site_view.xml',
        'views/meeting_main_kanban_view.xml',
        'views/meeting_menu.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
