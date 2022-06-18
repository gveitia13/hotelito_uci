from odoo import models, fields


class Persona(models.Model):
    _name = "hotel.persona"
    _description = 'Persona del SGU'

    tipo_identidad = fields.Selection([
        ('cubana', 'Cubana'),
        ('extranjera', 'Extranjera'), ],
        string='Tipo de identidad',
        default='cubana',
        required=True
    )
    carnet = fields.Char('Número de carnet', required=True)  # arreglar esto
    serie_carnet = fields.Integer('Número de serie CI', required=True)
    provincia = fields.Selection([
        ('havana', 'Havana'),
        ('pinar_del_rio', 'Pinar del Río'),
        ('cienfuegos', 'Cienfuegos'),
        ('granma', 'Granma'),
    ],
        string='Provincia registro civil',
        required=True)
    registro_civil = fields.Selection([
        ('marianao', 'Marianao'),
        ('centro_habana', 'Centro Habana'),
        ('playa', 'playa'),
    ],
        string='Registro civil',
        required=True)
    lugar_nacimiento = fields.Char('Lugar de nacimiento')
    tomo_ci = fields.Integer('Tomo ci')
    folio_ci = fields.Integer('Folio ci')
    nacionalidad = fields.Selection([
        ('cubana', 'Cubana'),
        ('extranjera', 'Extranjera'), ],
        string='Nacionalidad',
        default='cubana',
        required=True
    )
    nombre = fields.Char('Nombre', required=True)
    nombre2 = fields.Char('2do Nombre')
    apellido = fields.Char('1er Apellido', required=True)
    apellido2 = fields.Char('2do Apellido', required=True)
    ciudadania = fields.Selection([
        ('cubana', 'Cubana'),
        ('extranjera', 'Extranjera'), ],
        string='Ciudadanía',
        default='cubana',
        required=True
    )
    foto = fields.Binary(string='Foto')
