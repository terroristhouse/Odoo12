from odoo import models, fields, api


# 使用人表，一对多，一个人有多个资产
class User(models.Model):
    _name = 'assets.user'
    _description = '使用人'
    name = fields.Char('使用人', required=True)
    card_number = fields.Char('联系电话')
    email = fields.Char('电子邮箱')
    desc_detail = fields.Text('备注')  # 使用人备注
    # user_ids = fields.One2many('assets.main', 'user_id', string='使用人')
    use_ids = fields.One2many('assets.use', 'name_id', string='使用记录')
