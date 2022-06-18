from odoo import models, fields


class Persona(models.Model):
    _name = "hotel.persona"
    _description = 'Persona del SGU'

    # Información Nominal
    tipo_identidad = fields.Selection([
        ('cubana', 'Cubana'),
        ('extranjera', 'Extranjera'), ],
        string='Tipo de identidad',
        default='cubana',
        required=True
    )
    carnet = fields.Float('Número de carnet', required=True, size=11, digits=(11, 0))  # arreglar esto
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
    foto = fields.Image(string='Foto')
    # Dirección Particular
    dir_permanente = fields.Char('Residencia permanente')
    dir_numero = fields.Integer('No')
    dir_apartamento = fields.Char('Apartamento')
    dir_provincia = fields.Selection([
        ('havana', 'Havana'),
        ('pinar_del_rio', 'Pinar del Río'),
        ('cienfuegos', 'Cienfuegos'),
        ('granma', 'Granma'),
    ],
        string='Provincia registro civil',
        required=True)

    dir_municipio = fields.Selection([
        ('marianao', 'Marianao'),
        ('centro_habana', 'Centro Habana'),
        ('playa', 'playa'),
    ],
        string='Registro civil',
        required=True)
    dir_localidad = fields.Char('Localidad')
    dir_entre = fields.Char('Entre')
    dir_circunscripcion = fields.Char('Circunscripción')
    dir_km = fields.Char('Km')
    dir_cpa = fields.Char('CPA')
    dir_carretera = fields.Char('Carretera')
    dir_edificio = fields.Char('Edificio')
    dir_pais = fields.Selection([
        ('cuba', 'Cuba'),
        ('eeuu', 'EEUU'),
        ('angola', 'Angola'),
        ('vietnam', 'VietNam'),
    ],
        string='Provincia registro civil',
        required=True)
    dir_finca = fields.Char('Finca')
    # Rasgos fenotípicos
    rasgo_sexo = fields.Selection([
        ('f', 'Femenino'),
        ('m', 'Masculino'),
        ('otro', 'Otro'),
    ],
        string='Sexo',
        required=True)
    rasgo_raza = fields.Selection([
        ('b', 'Blanca'),
        ('m', 'Mestizo'),
        ('n', 'Negro'),
    ],
        string='Raza', )
    rasgo_ojos = fields.Selection([
        ('a', 'Azul'),
        ('v', 'Verde'),
        ('n', 'Negro'),
        ('c', 'Carmelita'),
    ],
        string='Color de ojos', )
    rasgo_pelo = fields.Selection([
        ('r', 'Rubio'),
        ('ca', 'Castaño'),
        ('n', 'Negro'),
        ('c', 'Carmelita'),
    ],
        string='Color de pelo', )
    rasgo_peso = fields.Char('Peso (Kg)')
    rasgo_estatura = fields.Char('Estatura (cm)')
    rasgo_discapacidad = fields.Selection([
        ('c', 'Ciego'),
        ('s', 'Sordo'),
        ('m', 'Mudo'),
        ('i', 'Inválido'),
    ],
        string='Tipo de discapacidad', )
    # Datos personales
    datos_estado_civil = fields.Selection([
        ('c', 'Casado'),
        ('s', 'Soltero'),
    ],
        string='Estado civil', )
    datos_hijos = fields.Integer('Cantidad de hijos')
    datos_huerfano = fields.Selection([
        ('p', 'Padre'),
        ('m', 'Madre'),
        ('a', 'Ambos'),
    ],
        string='Huérfano', )
    datos_id_expediente = fields.Char('Id de expediente')
    datos_telefono_p = fields.Char('Teléfono fijo')
    datos_correo = fields.Char('Correo')
    datos_solapin = fields.Char('Solapín')
    datos_telefono_c = fields.Char('Teléfono celular')
    datos_fax = fields.Char('Fax')
    datos_organizaciones_p = fields.Selection([
        ('pcc', 'PCC'),
        ('ujc', 'UJC'),
        ('a', 'Ambos'),
    ],
        string='Organizaciones políticas', )
    datos_organizaciones_m = fields.Selection([
        ('fmc', 'FMC'),
        ('cdr', 'CDR'),
        ('a', 'Ambos'),
    ],
        string='Organizaciones de masa', )
    # Datos de superación
    super_nivel_escolar = fields.Selection([
        ('bachiller', 'Bachiller'),
        ('universitario', 'Universitario'),
        ('master', 'Máster'),
        ('doctor', 'Doctor'),
    ],
        string='Nivel escolar', )
    super_categoria_docente = fields.Selection([
        ('rga', 'RGA'),
        ('queseyo', 'Que se yo'),
        ('duro', 'Esta duro'),
    ],
        string='Categoría docente', )
    super_profesion = fields.Selection([
        ('ing', 'Ingeniero en Ciencias Informáticas'),
        ('bio', 'Ingeniero en Bioinformática'),
        ('algo', 'Algo mas'),
    ],
        string='Profesión', )
    super_grado = fields.Selection([
        ('9no', '9no grado'),
        ('12mo', '12mo grado'),
        ('universitario', 'universitario'),
    ],
        string='Grado académico')
    super_categoria_investigativa = fields.Selection([
        ('1', 'Lasdjsa'),
        ('2', '1asrdsdfds'),
        ('3', 'dsfdsfdsf'),
    ],
        string='Grado académico')
    # Herencias
    apartment_id = fields.Many2one('hotel.apartment', string="Apartamento")
    request_ids = fields.Many2many('hotel.request', string="Solicitudes")
    register_number = fields.Integer("Numero de Registro")
    carpetera = fields.Char("Nombre de la Carpetera")