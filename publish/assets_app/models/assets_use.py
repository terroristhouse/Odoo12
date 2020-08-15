from odoo import models, fields, api
import datetime


# 使用记录表，多对一，多个使用记录对应一个资产
class Use(models.Model):
    _name = 'assets.use'
    _description = '使用记录'
    _order = 'create_on desc'

    zichan_id = fields.Many2one('assets.main', '设备编号', required=True)
    name_id = fields.Many2one('assets.user', '使用人', required=True)
    local_id = fields.Many2one('assets.site', '使用地点', required=True)
    create_on = fields.Date('借出时间')
    end_on = fields.Date('回收时间')
    lender = fields.Many2one('assets.manager', '借出人', required=True)
    desc_detail = fields.Text('备注')  # 借用备注
    # color = fields.Integer('Color Index')
    # state_use = fields.Selection(
    #     [('0', '准备借用'),
    #      ('1', '外借中'),
    #      ('2', '已回收')], '状态', default='0', required=True
    # )
    priority = fields.Selection(
        [('0', 'Low'),
         ('1', 'Normal'),
         ('2', 'High')],
        'Priority', default='1'
    )
    kanban_state = fields.Selection(
        [('normal', 'In Progress'),
         ('blocked', 'Blocked'),
         ('done', 'Ready for next stage')],
        'Kanban State',
        default='normal'
    )

    @api.model
    def _default_stage(self):
        Stage = self.env['assets.use.stage']
        return Stage.search([], limit=1)

    @api.model
    def _group_expand_stage_id(self, stages, domain, order):
        return stages.search([], order=order)

    stage_id = fields.Many2one('assets.use.stage', default=_default_stage, group_expand='_group_expand_stage_id')
    state_use = fields.Selection(related='stage_id.state')

    def button_done(self):
        # self.write({'state_use': '2'})
        self.write({'end_on': datetime.date.today()})
        # return True
        Stage = self.env['assets.use.stage']
        done_stage = Stage.search(
            [('state', '=', '2')], limit=1
        )
        for checkout in self:
            checkout.stage_id = done_stage
        return True

    @api.onchange('state_use')
    def onchange_state_use(self):
        today = fields.Date.today()
        if self.state_use == '2':
            self.end_on = today
        elif self.state_use == '1':
            self.create_on = today
            self.end_on = ''
        else:
            self.end_on = ''
            self.create_on = ''

# , default=lambda self: fields.Date.today()
