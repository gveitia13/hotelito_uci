# -*- coding: utf-8 -*-
{
    'name': "Hotel UCI",

    'summary': """
        Modulo para gestionar la gestion del hotelito""",

    'description': """
        En este modulo se gestionaran los procesos de hospedaje en el hotel de la UCI
    """,

    'author': "Alex Zaldivar",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['contacts', 'mail', 'crm'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/menuViews.xml',
        'views/requestViews.xml',
        'views/apartmentViews.xml',
        'views/guestViews.xml',
        'views/buildingViews.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
