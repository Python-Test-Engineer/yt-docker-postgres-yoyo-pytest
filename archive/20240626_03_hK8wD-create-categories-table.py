"""
Create categories table
"""

from yoyo import step

__depends__ = {"20240626_02_WOcVI-add-products"}

step(
    "CREATE TABLE categories (id SERIAL PRIMARY KEY, cat_code varchar(10), cat_name varchar(50), is_active boolean DEFAULT true);",
    "DROP TABLE categories;",
),
