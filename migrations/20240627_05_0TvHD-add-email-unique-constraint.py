"""
Add email unique constraint
"""

from yoyo import step

__depends__ = {"20240627_04_ylF9y-add-unique-constraints"}


steps = [
    step(
        """
        ALTER TABLE users
        ADD CONSTRAINT email_unique_check UNIQUE (email);""",
        """
        ALTER TABLE users
        DROP CONSTRAINT email_unique_check;
        """,
    )
]
