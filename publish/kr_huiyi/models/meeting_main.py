from odoo import models, fields, api
from odoo.exceptions import ValidationError


class KrHuiyi(models.Model):
    _name = 'meeting.main'
    _description = '会议'
    _order = 'start_time desc'

    name = fields.Many2one('meeting.site', string='会议地点', required=True)
    start_time = fields.Datetime('开始时间', required=True)
    end_time = fields.Datetime('结束时间')
    remark = fields.Char('备注')

    @api.constrains('end_time')
    def _check_end_time(self):
        for record in self:
            if record.start_time > record.end_time:
                raise ValidationError('结束时间不可以早于开始时间！')
