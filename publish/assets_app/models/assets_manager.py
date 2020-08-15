from odoo import models, fields, api


# 借出人表，一对多，一个人可借出多个资产
class User(models.Model):
    _name = 'assets.manager'
    _description = '资产借出人'
    name = fields.Char('资产借出人', required=True)
    card_number = fields.Char('联系电话')
    email = fields.Char('电子邮箱')
    desc_detail = fields.Text('备注')  # 使用人备注
    # user_ids = fields.One2many('assets.main', 'user_id', string='使用人')
    use_ids = fields.One2many('assets.use', 'lender', string='借出记录')
