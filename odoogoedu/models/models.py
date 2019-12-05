# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Course(models.Model):
    _name = 'odoogoedu.course'
    _description = "课程记录"
    name = fields.Char(string="课程名",required=True)
    description = fields.Text(string="课程描述")
    responsible_id=fields.Many2one('res.users',ondelete='set null',string="负责人",index=True)
    session_ids=fields.One2many('odoogoedu.session','course_id',string="课时")


class Session(models.Model):
    _name = 'odoogoedu.session'
    _description = "课时"

    name=fields.Char(required=True,string="课时名称")
    start_date=fields.Date(string='开始时间')
    duration=fields.Float(digits=(6,2),help="时长（天）",string="课时时长")
    seats=fields.Integer(string="座位数")
    instructor_id=fields.Many2one('res.partner',string="老师")
    course_id=fields.Many2one('odoogoedu.course',ondelete='cascade',string="课程",required=True)
    attendee_ids=fields.Many2many('res.partner',string="学生")
