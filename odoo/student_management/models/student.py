from odoo import fields, models

class Student(models.Model):
    _name = 'student.management'
    _description = 'Student Management'
   #
    image=fields.Image(string="Image")
    # char
    name=fields.Char(string=' Student Name',required=True,index=True)
    phone=fields.Char(string='Student Phone', readonly=True)
    email=fields.Char(string='Student Email',copy=False)
    # integer
    age=fields.Integer(string='Student Age')
    # Float
    percentage = fields.Float(string="Percentage",help="Enter in Percentage or CGPA")
    fees=fields.Float(string="Fees")
    #Boolean
    is_active = fields.Boolean(string="Active",default="True")
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
    #Selection
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female')
    ])

    department_id=fields.Many2one(
            'student.department',
             string='Department'
    )
    department_ids = fields.Many2many(
        'student.department',
        string='Departments'
    )
    user_id = fields.Many2one(
        'res.users',
        string='User'
    )
    email = fields.Char(related='user_id.email')