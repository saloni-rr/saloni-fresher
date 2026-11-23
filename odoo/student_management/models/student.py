from odoo import fields, models

class Student(models.Model):
    _name = 'student.management'
    _description = 'Student Management'

    # char
    name=fields.Char(string=' Student Name',required=True,index=True)
    phone=fields.Char(string='Student Phone', readonly=True)
    email=fields.Char(string='Student Email',copy=False)
    # integer
    age=fields.Integer(string='Student Age')
    # Float
    percentage = fields.Float(string="Percentage",help="Enter in Percentage or CGPA")
    #Boolean
    active = fields.Boolean(string="Active",default="True")
    # Text
    description = fields.Text(string="Description")
    # Date
    dob = fields.Date(string="Date of Birth")
    # Datetime
    admission = fields.Datetime(string="Admission")
    # Binary
    photo = fields.Binary(string="Photo")
    # Html
    notes = fields.Html(string="Notes")

    department_id=fields.Many2one(
            'student.department',
             string='Department'
    )
    user_id = fields.Many2one(
        'res.users',
        string='User'
    )
    email = fields.Char(related='user_id.email')