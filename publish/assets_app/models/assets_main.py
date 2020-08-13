from odoo import fields, models, api


class AssetsMain(models.Model):
    _name = 'assets.main'
    _description = '资产'
    _order = 'name'

    name = fields.Char('设备编号', required=True)  # 设备编号
    desc_detail = fields.Text('备注')  # 设备备注
    number = fields.Integer('数量', required=True)  # 资产数量
    sequ = fields.Char('序列号')  # 资产序列号
    local_id = fields.Many2one('assets.site', '地点', required=True)  # 所在地点
    section_id = fields.Many2one('assets.section', '部门')  # 所在部门
    user_id = fields.Many2one('assets.user', '使用人')  # 使用人
    cate_id = fields.Many2one('assets.cate', '类别', required=True)  # 资产类别
    secret_id = fields.Selection(
        [('gongkai', '公开'),
         ('mimi', '秘密'),
         ('jimi', '机密'),
         ('juemi', '绝密')], '密级', required=True
    )  # 资产密级
    state_id = fields.Selection(
        [('zaiyong', '在用'),
         ('daixiu', '待修'),
         ('zaixiu', '在修'),
         ('beiyong', '备用'),
         ('xianzhi', '闲置'),
         ('tiaoji', '调剂'),
         ('daibaofei', '待报废'),
         ('baofei', '报废')], '资产状态', required=True
    )  # 资产状态
    type_id = fields.Many2one('assets.type', '型号')  # 资产型号
    use_ids = fields.One2many('assets.use', 'zichan_id', string='使用记录')  # 使用记录

    _sql_constraints = [
        ('unique_course_name',
         'unique(name)', '设备编号重复！'),
        ('unique_course_sequ',
         'unique(sequ)', '设备序列号重复！')
    ]
