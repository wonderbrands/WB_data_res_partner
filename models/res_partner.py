# -*- coding: utf-8 -*-
from odoo import models, fields, api

class ResPartner(models.Model):
    _inherit = "res.partner"

    
    # Campos en desuso, comentado por si se requieren en un futuro.
    '''
    monto_minimo = fields.Char(string='Mínimo de compra', help='Mínimo de compra por proveedor')
    dias_credito = fields.Integer(string='Días de crédito', help='Días de crédito que da el proveedor')
    dias_compra = fields.Char(string='Días de compra', help='Días en los que se le puede enviar pedido al proveedor')

    unidad = fields.Selection([('pza', 'Piezas'),
                               ('doc', 'Docenas'),
                               ('caj', 'Cajas'),
                               ('pes', 'Pesos')], string='Unidad')

    leadtime = fields.Integer(string='Leadtime', help='Tiempo de entrega estimado del proveedor')
    '''
    #Claves
    data_wb_supplier = fields.Boolean(string='¿Es proveedor?', help='Marca si el usuario de compra es un Proveedor')
    data_provider_key = fields.Char(string='Clave de proveedor', help='Clave de Proveedor asignada')
    
    # Campos de res_partner_extend
    data_advance_payment_date = fields.Integer(string='Días de financiamiento', help='Cantidad de días de financiamiento')
    data_percent_supplier_advance = fields.Float(string='% Anticipo proveedor', help='Muestra el porcentaje de anticipo al proveedor')
    data_lt_ag_channel = fields.Integer(string='LT Producción', help='LT Producción')
