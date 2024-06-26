"""
Add check constraint to products
"""

from yoyo import step

__depends__ = {"20240626_06_fonqd-run-constraints-ecommerce"}

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
