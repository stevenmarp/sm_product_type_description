# -*- coding: utf-8 -*-
{
    "name": "Product Type Description",
    "version": "18.0.1.0.0",
    "category": "Inventory/Inventory",
    "summary": "Searchable type description field on products",
    "description": """
SM Product Type Description
===========================

Adds a dedicated type description field to product templates, visible on
product forms and optionally available in list and search views.
    """,
    "author": "Steven Marp",
    "website": "https://apps.odoo.com/apps/browse?repo_maintainer_id=512936",
    "license": "OPL-1",
    "price": 1.36,
    "currency": "USD",
    "depends": ["stock"],
    "data": [
        "views/product_template_views.xml",
    ],
    "images": [
        "static/description/banner.gif",
    ],
    "installable": True,
    "application": False,
    "auto_install": False,
}
