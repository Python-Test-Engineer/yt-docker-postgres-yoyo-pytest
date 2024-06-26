"""
Generate products
"""

from yoyo import step

__depends__ = {"20240626_01_8laEZ-create-products-table"}

steps = [
    step(
        """
        INSERT INTO products (product_name, price, category) values
            ('AMD Computer', 299.99, 'Hardware'),
            ('M2 Computer', 399.99, 'Hardware'),
            ('Norton Anti-Virus', 99.99, 'Software'),
            ('Asus Laptop', 299.99, 'Hardware')
          
        ;
        """,
        "DELETE FROM products;",
    )
]
