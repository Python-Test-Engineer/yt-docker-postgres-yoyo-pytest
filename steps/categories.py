steps = [
    step(
        "CREATE TABLE categories (id SERIAL PRIMARY KEY, cat_code varchar(10), cat_name varchar(50), is_active boolean DEFAULT true);",
        "DROP TABLE categories;",
    ),
    step(
        """
        INSERT INTO categories (cat_code,cat_name, is_active) values
            ('HRD','hardware',true),
            ('SFT','software',true),
            ('ACC','accessories',false)
          
        ;
        """,
        "DELETE FROM categories;",
    ),
]
