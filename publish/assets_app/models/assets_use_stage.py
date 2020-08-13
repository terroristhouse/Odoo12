from odoo import fields, models


class UseStage(models.Model):
    _name = 'assets.use.stage'
    _description = '使用状态'
    _order = 'sequence,name'

    name = fields.Char()
    sequence = fields.Integer(default=10)
    fold = fields.Boolean(default=True)
    state = fields.Selection(
        [('0', '准备借用'),
         ('1', '外借中'),
         ('2', '已回收')], '状态', default='0', required=True
    )
