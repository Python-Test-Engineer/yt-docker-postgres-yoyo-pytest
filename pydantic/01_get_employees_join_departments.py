"""Example 3"""

from pydantic import BaseModel, ConfigDict, Field
import psycopg2


class Employee(BaseModel):
    model_config = ConfigDict(extras="ignore")

    employee_id: int = Field(alias="id")
    first_name: str
    last_name: str
    nickname: str | None = None


# Connect to existing database
conn = psycopg2.connect(
    database="postgres",
    user="postgres",
    password="postgres",
    host="host.docker.internal",
)
if conn:
    print(f"Conn: {conn}")
else:
    print("NO CONNECTION")
# Open cursor to perform database operation
cur = conn.cursor()


# sql = "SELECT * FROM employees;"
sql = """
        SELECT employees.*, departments.name
        FROM employees
        INNER JOIN departments on employees.department_id=departments.id
        ORDER BY last_name;
    """

cur.execute(sql)
print(f"SQL: {sql}")
print("============")
rows = cur.fetchall()
if not len(rows):
    print("empty")
for row in rows:
    print(row)
print("============")

# Close communications with database
cur.close()
conn.close()
