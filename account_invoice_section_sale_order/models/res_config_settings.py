# Copyright 2025 Patryk Pyczko (APSL-Nagarro)<ppyczko@apsl.net>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models


class SaleConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    show_sale_order_date_in_invoice = fields.Boolean(
        string="Show Sale Order Date in Invoice Section",
        config_parameter="sale.show_sale_order_date_in_invoice",
        help="If enabled, the sale order date will be included in the invoice section title.",
    )

    show_client_order_ref_in_invoice = fields.Boolean(
        string="Show Client Reference in Invoice Section",
        config_parameter="sale.show_client_order_ref_in_invoice",
        help="If enabled, the client's reference from the sale order "
        "will be included in the invoice section title.",
    )
