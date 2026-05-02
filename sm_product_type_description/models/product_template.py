# -*- coding: utf-8 -*-

from odoo import fields, models


class ProductTemplate(models.Model):
    _inherit = "product.template"

    type_description = fields.Text(
        string="Type Description",
        translate=True,
        tracking=True,
        help="Additional description for the product type or product classification.",
    )
