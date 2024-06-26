"""
Rename product table to products
"""

from yoyo import step

__depends__ = {"20240626_01_b7ZRk-create-product-table"}

steps = [
    step(
        "ALTER TABLE product RENAME TO products;",
        "ALTER TABLE products RENAME TO product;",
    ),
]
