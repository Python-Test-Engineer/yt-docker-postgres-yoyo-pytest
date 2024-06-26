# YoYo
 
From docs https://ollycope.com/software/yoyo/latest/#
 
## yoyo new
Start a new migration. yoyo new will create a new migration file and opens it your configured editor.

By default a Python formation migration will be created. To use the simpler SQL format, specify --sql.

https://ollycope.com/software/yoyo/latest/#yoyo-new

```
yoyo new -m "Add column to foo"
yoyo new --sql
```

Produces a file in migrations `20240626_01_GBjEm-add-column-to-foo.py`

alternatively create a python file:

migrations/0001.create-foo.py

This contains:

```
from yoyo import step

__depends__ = {'20240604_04_Qqsgz-change-departments-to-fk'}

steps = [
    step("SQL", "rollback SQL)
]
```
and one can then add 
```
steps = [
    step(
        """
        CREATE TABLE employee (
            id SERIAL PRIMARY KEY,
            first_name text NOT NULL,
            last_name text NOT NULL,
            nickname text,
            department text NOT NULL
        );
        """,
        "DROP TABLE employee;" # this is the rollback
    )
]
```

One can create ones own .py file and add steps but it may be better to let YoYo manage the versioning.

```
from yoyo import step
steps = [
   step(
       "CREATE TABLE foo (id INT, bar VARCHAR(20), PRIMARY KEY (id))",
       "DROP TABLE foo"
   )
]
```
## yoyo list
List available migrations. Each migration will be prefixed with one of U (unapplied) or A (applied).

## yoyo apply

Apply migrations to the target database. By default this will prompt you for each unapplied migration. To turn off prompting use --batch or specify batch_mode = on in yoyo.ini.

## yoyo rollback
By default this will prompt you for each applied migration, starting with the most recently applied.

If you wish to rollback a single migration, specify the migration with the -r/--revision flag. Note that this will also cause any migrations that depend on the selected migration to be rolled back.