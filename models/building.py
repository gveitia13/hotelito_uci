from odoo import models, fields

class Building(models.Model):
    _name = "hotel.building"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    
    number = fields.Integer('Numero del Edificio', required=True)
    apartment_ids = fields.One2many('hotel.apartment', 'building_id', string="Apartamentos")
 