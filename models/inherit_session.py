from openerp import api, fields, models

class InheritSession(models.Model):
    _inherit= "openacademy.session"
    
    instructor_id = fields.Many2one("res.partner", string="Instructor")
    taken_seats=fields.Float(digits=(4,0), compute='_taken_seats')
    
    @api.one
    @api.depends('seats','instructor_id')
    def _taken_seats(self):
        if self.seats:
            self.taken_seats=100 * len(self.instructor_id)/ self.seats
            
        
        
        
    
    