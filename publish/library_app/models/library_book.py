from odoo import fields, models, api
from odoo.exceptions import Warning
from odoo.exceptions import ValidationError


class Book(models.Model):
    _name = 'library.book'
    _description = 'Book'
    _order = 'name,date_published desc'

    # String fields
    name = fields.Char('Title', required=True)
    isbn = fields.Char('ISBN')
    book_type = fields.Selection(
        [('paper', 'Paperback'),
         ('hard', 'Hardcover'),
         ('electronic', 'Electronic'),
         ('other', 'Other')],
        'Type'
    )
    notes = fields.Text('Internal Notes')
    descr = fields.Html('Description')

    # Number fields
    copies = fields.Integer(default=1)
    avg_rating = fields.Float('Average Rating', (3, 2))
    price = fields.Monetary('Price', 'currency_id')
    currency_id = fields.Many2one('res.currency')  # price helper

    # Date and time fields
    date_published = fields.Date()
    last_borrow_date = fields.Datetime(
        'Last Borrowed On',
        default=lambda self: fields.Datetime.now()
    )

    # Other fields
    image = fields.Binary('Cover')
    active = fields.Boolean('Active?', default=True)

    # Relational fields
    publisher_id = fields.Many2one('res.partner', string='Publisher')
    author_ids = fields.Many2many('res.partner', string='Authors')

    publisher_country_id = fields.Many2one(
        'res.country', string='Publisher Country',
        compute='_compute_publisher_country',
        # store = False, 默认不在数据库中存储
        inverse='_inverse_publisher_country',
        search='_search_publisher_country',
    )

    _sql_constraints = [
        ('library_book_name_date_uq',
         'UNIQUE(name, date_published)',
         'Book title and publication date must be unique'),
        ('library_book_check_date',
         'CHECK (date_published <= current_date)',
         'Publication date must not be in the future')
    ]

    @api.constrains('isbn')
    def _constrain_isbn_valid(self):
        for book in self:
            if book.isbn and not book._check_isbn():
                raise ValidationError('%s is an invalid ISBN' % book.isbn)

    def _inverse_publisher_country(self):
        for book in self:
            book.publisher_id.country_id = book.publisher_country_id

    def _search_publisher_country(self, opearator, value):
        return [('publisher_id.country_id', opearator, value)]

    @api.depends('publisher_id.country_id')
    def _compute_publisher_country(self):
        for book in self:
            book.publisher_country_id = book.publisher_id.country_id

    def _check_isbn(self):
        self.ensure_one()
        isbn = self.isbn.replace('-', '')
        digits = [int(x) for x in isbn if x.isdigit()]
        if len(digits) == 13:
            ponderations = [1, 3] * 6
            terms = [a * b for a, b in zip(digits[:12], ponderations)]
            remain = sum(terms) % 10
            check = 10 - remain if remain != 0 else 0
            return digits[-1] == check

    def button_check_isbn(self):
        for book in self:
            if not book.isbn:
                raise Warning('please provide an ISBN for %s' % book.name)
            if book.isbn and not book._check_isbn():
                raise Warning('%s is an invalid ISBN' % book.name)
            return True
