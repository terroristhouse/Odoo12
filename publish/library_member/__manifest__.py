{
    'name': 'Library Members',
    'description': 'Manage people who will be able to borrow books',
    'author': 'Mr. Liu',
    'depends': ['library_app', 'mail'],
    'application': False,
    'data': [
        'security/library_security.xml',
        'security/ir.model.access.csv',
        'views/library_menu.xml',
        'views/member_view.xml',
        'views/book_view.xml',
        'views/book_list_template.xml',
    ]
}
