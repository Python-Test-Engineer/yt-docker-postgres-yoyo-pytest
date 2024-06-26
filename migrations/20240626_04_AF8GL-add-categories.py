"""
Add categories
"""

from yoyo import step

__depends__ = {"20240626_03_hK8wD-create-categories-table"}


steps = [
    step(
        """
        INSERT INTO categories (cat_code,cat_name, is_active) values
            ('HRD','hardware',true),
            ('SFT','software',true),
            ('ACC','accessories',false)
          
        ;
        """,
        "DELETE FROM categories;",
    )
]
