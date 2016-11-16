from openerp import api, exceptions, fields, models
import re
from openerp import _
from openerp.exceptions import except_orm, Warning, RedirectWarning

class Student(models.Model):
    _name='school.student'
    _order='id desc'
    
    name=fields.Char(string="Student Name", required=True)
    contact_no=fields.Integer()
    address=fields.Text()
    date_of_birth=fields.Date(default=fields.Date.today())
    email=fields.Char()
    gender=fields.Selection([('male','Male'),('female','Female')])
    responsible_id=fields.Many2one("res.users",string="Users", default=lambda self: self.env.user)
    course_id=fields.Many2one("openacademy.course",string="Courses")
    #state=fields.Selection([('draft',"Draft"),('confirm',"Confirm"),('done',"Done"),('cancel',"Cancel")], default="draft")
    subject=fields.Integer(string="Subject")
    total_marks=fields.Float(string="Total Marks")
    average_marks=fields.Float(string="Average Marks" , readonly=True)
    
    
    
    @api.one
    @api.constrains('email')
    def check_email_validation(self):
        if self.email:
            if re.match("^.+\\@(\\[?)[a-zA-Z0-9\\-\\.]+\\.([a-zA-Z]{2,3}|[0-9]{1,3})(\\]?)$", self.email) == None:
               raise exceptions.ValidationError("Email not valid.")
    
    
    
    @api.onchange("subject", "total_marks")
    def average_marks_calc(self):
        if self.subject and self.total_marks:
            self.average_marks= self.total_marks/ self.subject
            
            
    
            
            
    