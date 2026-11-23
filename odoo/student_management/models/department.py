from odoo import fields, models


class Department(models.Model):
        _name='student.department'
        _description= 'Student Department'

        name=fields.Char(string="Department",required=True)
        student_id=fields.One2many(
              'student.management',
             'department_id',
               string="Student"
         )
