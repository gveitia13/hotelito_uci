import string
from odoo import models, fields

class Guest(models.Model):
    _name = "hotel.guest"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    
    name = fields.Char("Nombre")
    lastname = fields.Char("Apellidos")
    origin = fields.Char("Lugar de Procedencia")
    motive = fields.Text("Motivo")
    identified = fields.Integer("Numero de Identificacion")
    init_date = fields.Date(
       'Fecha de Entrada',
       required=True,
    )
    end_date = fields.Date(
       'Fecha de Salida',
       required=True,
    )
    apartment_id = fields.Many2one('hotel.apartment', string="Apartamento")
    request_ids = fields.Many2many('hotel.request', string="Solicitudes")
    register_number = fields.Integer("Numero de Registro")
    carpetera = fields.Char("Nombre de la Carpetera")