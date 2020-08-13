from odoo import models, fields, api


# 型号表，一对多，一型号有多个资产
class Type(models.Model):
    _name = 'assets.type'
    _description = '型号'
    name = fields.Char('资产型号')
    # type_ids = fields.One2many('assets.main', 'type_id', string='资产型号')
