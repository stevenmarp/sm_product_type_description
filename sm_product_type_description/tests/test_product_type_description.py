# -*- coding: utf-8 -*-

from odoo.tests.common import TransactionCase, tagged


@tagged("post_install", "-at_install")
class TestProductTypeDescription(TransactionCase):

    def test_type_description_is_stored_on_product_template(self):
        product = self.env["product.template"].create({
            "name": "Type Description Test Product",
            "type_description": "Industrial spare part",
        })

        self.assertEqual(product.type_description, "Industrial spare part")

    def test_type_description_is_available_on_variant(self):
        template = self.env["product.template"].create({
            "name": "Type Description Variant Test",
            "type_description": "Serialized service kit",
        })

        self.assertEqual(template.product_variant_id.type_description, "Serialized service kit")

    def test_type_description_is_searchable_on_product_template(self):
        product = self.env["product.template"].create({
            "name": "Type Description Search Test",
            "type_description": "checkpoint",
        })

        self.assertIn(product, self.env["product.template"].search([("type_description", "ilike", "checkpoint")]))

    def test_type_description_is_searchable_on_product_variant(self):
        template = self.env["product.template"].create({
            "name": "Type Description Variant Search Test",
            "type_description": "checkpoint variant",
        })

        self.assertIn(template.product_variant_id, self.env["product.product"].search([("type_description", "ilike", "checkpoint")]))
