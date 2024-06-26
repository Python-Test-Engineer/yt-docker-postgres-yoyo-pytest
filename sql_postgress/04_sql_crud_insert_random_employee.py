import psycopg2

import string
import random


def get_random_string(length):
    letters = string.ascii_lowercase
    letters = string.ascii_uppercase + string.digits
    result_str = "".join(random.choice(letters) for i in range(length))
    return result_str


try:
    connection = psycopg2.connect(
        database="postgres",
        user="postgres",
        password="postgres",
        host="host.docker.internal",
    )
    cursor = connection.cursor()
    for _ in range(40):
        postgres_insert_query = """ INSERT into employee(name, state) VALUES (%s, %s)"""
        record_to_insert = (
            get_random_string(random.randint(5, 10)),
            get_random_string(random.randint(5, 10)),
        )
        cursor.execute(postgres_insert_query, record_to_insert)
        connection.commit()
        count = cursor.rowcount
        print(count, "Record inserted successfully into employee table")

except (Exception, psycopg2.Error) as error:
    print("Failed to insert record into mobile table", error)

finally:
    # closing database connection.
    if connection:
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")
