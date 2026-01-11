from odoo import models

class Website(models.Model):
    _inherit = "website"

    def _get_product_extra_field_domain(self):
        """Permite mostrar todos los tipos de campos del modelo product.template
        en la configuración de Campos adicionales del producto.
        Excluye únicamente Binary y Html, que podrían romper la renderización.
        """
        return [("ttype", "not in", ["binary", "html"])]
