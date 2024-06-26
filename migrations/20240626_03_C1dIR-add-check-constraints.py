"""
Add check constraints
"""

from yoyo import step

__depends__ = {"20240626_02_drUkq-add-foreign-keys"}

steps = [
    step(
        """
        ALTER TABLE products
        ADD CONSTRAINT price_non_zero_check
        CHECK ( regular_price > 0 );
        """,
        """
        ALTER TABLE products
        DROP CONSTRAINT price_non_zero_check;
        """,
    ),
]
