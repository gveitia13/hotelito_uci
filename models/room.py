from odoo import models, fields

class Room(models.Model):
    _name = "hotel.room"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    
    number = fields.Integer('Numero de la Habitacion', required=True)
    apartment_id = fields.Many2one('hotel.apartment', string="Apartamento")
    state = fields.Selection([
      ('ocupado', 'Ocupado'),
      ('open', 'Disponible'),
      ('close', 'Cerrado'),
      ('manteined', 'En Mantenimiento')],
      string='Estado'
    )
    room_type = fields.Selection([
        ('simple', 'Simple'),
        ('doble', 'Doble')
    ])
 