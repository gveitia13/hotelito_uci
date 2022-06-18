from odoo import models, fields

class Solicitudes(models.Model):
    _name = "hotel.request"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    
    
    number = fields.Integer('Numero de Solicitud', required=True)
    guest_ids = fields.Many2many('hotel.guest', string="Huespedes")
    motive = fields.Text(string="Motivo", required=True)
    state = fields.Selection([
        ('pending', 'Pendiente'),
        ('accept', 'Aceptada'),
        ('canceled', 'Cancelada'),
        ('reject', 'Rechazada')], 
        string='Estado',
        group_expand='_group_expand_states',
        default='pending',
        tracking=True)
    color = fields.Integer('Color', default=0)
    amount = fields.Integer('Monto', required=True)
    ingreso = fields.Integer('Ingreso', required=True)
    tag_ids = fields.Many2many(
        'crm.tag', 'request_tag_rel', 'request_id', 'tag_id', string='Etiquetas',
        )
    priority = fields.Selection([
      ('0', 'Bajo'),
      ('1', 'Medio'),
      ('2', 'Alta'),
      ('3', 'Muy alta')],
      string='Prioridad',
      default='1'
    )
    
    init_date = fields.Date(
       'Fecha de Inicio',
       required=True,
    )
    end_date = fields.Date(
       'Fecha de Fin',
       required=True,
    )
    
    level = fields.Selection([('hight', 'Alto'), ('low','Bajo')],
        'Nivel', required = True
    )
    
    def _group_expand_states(self, states, domain, order):
        return [key for key, val in type(self).state.selection]