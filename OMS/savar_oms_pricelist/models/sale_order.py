from odoo import models, fields, api
import logging
_logger = logging.getLogger(__name__)

class SaleOrder(models.Model):
    _inherit = 'sale.order'
    
    oms_pricelist_id = fields.Many2one('oms.pricelist', string='Tarifa')
    
    @api.onchange('oms_pricelist_id')
    def _onchange_oms_pricelist_id(self):
        pass
        # for line in self.order_line:
        #     line._onchange_pricelist_fields()
    
    

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'
    
    product_service_subservices = fields.Many2many(string='SubServicios',related='product_id.product_service_subservices') 
    subservice_id = fields.Many2one('fsm.order.service', string='SubServicio')
    
    size_id = fields.Many2one('product.size', string='Talla')
    warehouse_id = fields.Many2one('stock.warehouse', string='Local')
    district_id = fields.Many2one('res.district', string='Zona')    
    size_quant = fields.Integer(string='Cantidad Talla') 

    @api.onchange('product_id')
    def _onchange_oms_product_id(self):
        self.subservice_id = None
