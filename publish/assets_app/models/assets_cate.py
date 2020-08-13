from odoo import models, fields, api


# 类别表，一对多，一类别有多个资产
class Cate(models.Model):
    _name = 'assets.cate'
    _description = '类别'
    name = fields.Char('资产类别')
    # cate_ids = fields.One2many('assets.main', 'cate_id', string='资产')
