{
    'name': 'Library Management',
    'description': 'Manage Library book catalogue and lending',
    'author': 'Mr. Liu',
    'depends': ['base'],
    'application': True,
    'data': [
        'security/library_security.xml',
        'security/ir.model.access.csv',
        'views/library_menu.xml',
        'views/book_view.xml',
        'views/book_list_template.xml',
        'reports/library_book_report.xml',
        'reports/library_book_sql_report.xml',
    ],
    'demo': [
        'data/book_demo.xml',
    ],
}
