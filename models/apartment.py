from odoo import models, fields


class Apartment(models.Model):
    _name = "hotel.apartment"
    _rec_name = 'number'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    
    number = fields.Char(string="Número")
    building_id = fields.Many2one('hotel.building', "Edificio")
    capacity = fields.Char(string="Capacidad")
    apartment_state = fields.Selection([('open', 'Disponible'), ('close','Ocupado')],
        'Estado', defualt = 'open', required = True
    )
    guest_id = fields.One2many('hotel.guest', 'apartment_id', 'Huespedes')