"""
Create product table
"""

from yoyo import step

__depends__ = {"20240604_04_Qqsgz-change-departments-to-fk"}


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
        "DELETE FROM products;",
    )
]
