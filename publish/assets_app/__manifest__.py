{
    'name': '资产管理',
    'description': '卡尔-运维组资产管理',
    'author': '刘飞',
    'depends': ['base'],
    'application': True,

    'data': [
        'security/assets_security.xml',
        'security/ir.model.access.csv',
        'views/assets_main_view.xml',
        'views/assets_use_view.xml',
        'views/assets_use_kanban_view.xml',
        'views/assets_user_view.xml',
        'data/assets_use_stage.xml',
        'views/assets_menu.xml',
    ]
}
