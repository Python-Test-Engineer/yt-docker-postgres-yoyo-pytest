"""
Add email unique constraint users
"""

from yoyo import step

__depends__ = {"20240626_04_fVp1c-add-unique-constraints"}

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
