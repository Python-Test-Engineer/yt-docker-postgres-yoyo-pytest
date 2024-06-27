"""
Add unique constraints
"""

from yoyo import step

__depends__ = {"20240626_03_C1dIR-add-check-constraints"}

steps = [
    step(
        """
        ALTER TABLE categories
        ADD CONSTRAINT name_unique_check UNIQUE (name);""",
        """
        ALTER TABLE categories
        DROP CONSTRAINT name_unique_check;
        """,
    )
]
