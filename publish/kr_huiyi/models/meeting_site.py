from odoo import fields, api, models


class KrSite(models.Model):
    _name = 'meeting.site'
    _description = '会议地点'

    name = fields.Char('地点')
    huiyi_ids = fields.One2many('meeting.main', 'name', string='会议')
