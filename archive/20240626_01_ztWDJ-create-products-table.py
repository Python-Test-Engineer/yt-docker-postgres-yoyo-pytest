"""
Create products table
"""

from yoyo import step

__depends__ = {}

steps = [
    step(
        """
        CREATE TABLE products (
            id SERIAL PRIMARY KEY,
            product_name varchar(50) NOT NULL,
            price decimal NOT NULL,
            category varchar(50) NOT NULL
        );
        """,
        "DROP TABLE products;",
    )
]
