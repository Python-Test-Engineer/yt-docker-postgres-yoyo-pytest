"""
Add check constraint product name
"""

from yoyo import step

__depends__ = {'20240627_05_0TvHD-add-email-unique-constraint'}

steps = [
    step("""
        ALTER TABLE products
        ADD CONSTRAINT name_more_three
        CHECK ( LENGTH(TRIM(name)) >= 3);
         """, 
         """
        ALTER TABLE products
        DROP CONSTRAINT name_more_three;
         """)
]
