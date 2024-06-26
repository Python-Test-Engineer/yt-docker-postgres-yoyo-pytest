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
    ),
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
    ),
    step(
        """
        ALTER TABLE products
        ADD CONSTRAINT regular_price_non_zero CHECK (regular_price > 0);
        );
        """,
        """
        ALTER TABLE products
        DROP CONSTRAINT regular_price_non_zero;
        """,
    ),
]
