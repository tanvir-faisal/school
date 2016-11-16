from openerp import api, fields, models

class InheritCourse(models.Model):
    _inherit = "openacademy.course"
    
    start_date=fields.Date(default=fields.Date.today())
    end_date=fields.Date(default=fields.Date.today())
    
    