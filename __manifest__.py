# -*- coding: utf-8 -*-
{
    'name': "Modificaciones Formulario de Contacto",

    'summary': """
        Modificaciones al formulario de contacto para uso general e interno""",

    'description': """
        Este módulo agrega diferentes modificaciones y campos al formulario de contacto que servirán al registro e identificación de proveedores
        
        -Monto mínimo
        -Días de crédito
        -Días de Compra
        -Unidad de compra
        -Leadtime
    """,

    'author': "Wonderbrands",
    'website': "https://www.wonderbrands.co",
    'license': 'LGPL-3',
    'category': 'Inventory',
    'version': '18.0',

    'depends': ['base',
                'product',
                'sale',
                'stock',
                ],

    'data': [
        'views/res_partner_views.xml',
    ],
   
}
