from odoo import models, fields, api


# 部门表，一对多，一个部门有多个资产
class Section(models.Model):
    _name = 'assets.section'
    _description = '部门'
    name = fields.Char('部门')
    # section_ids = fields.One2many('assets.main', 'section_id', string='部门')
