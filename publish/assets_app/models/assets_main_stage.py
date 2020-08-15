from odoo import fields, models


class UseStage(models.Model):
    _name = 'assets.main.stage'
    _description = '资产状态'
    _order = 'sequence,name'

    name = fields.Char()
    sequence = fields.Integer(default=10)
    fold = fields.Boolean(default=True)
    state = fields.Selection(
        [('zaiyong', '在用'),
         ('daixiu', '待修'),
         ('zaixiu', '在修'),
         ('beiyong', '备用'),
         ('xianzhi', '闲置'),
         ('tiaoji', '调剂'),
         ('daibaofei', '待报废'),
         ('baofei', '报废')
         ], '资产状态', default='zaiyong', required=True
    )  # 资产状态
