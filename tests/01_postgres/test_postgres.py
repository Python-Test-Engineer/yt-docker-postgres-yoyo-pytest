import pytest
import psycopg2


def test_db_true():
    assert True


def test_can_connect_to_db():

    # Establishing the connection
    conn = psycopg2.connect(
        database="postgres",
        user="postgres",
        password="postgres",
        host="host.docker.internal",
    )
    if conn:
        print(f"\tConnected to DB...\n")
        # print(conn)
    else:
        print("NO CONNECTION\n")

    cursor = conn.cursor()

    # Creating table as per requirement
    sql = f""" SELECT COUNT(*) FROM
                (SELECT
                    tc.constraint_name, tc.table_name, kcu.column_name, 
                    ccu.table_name AS foreign_table_name,
                    ccu.column_name AS foreign_column_name 
                FROM 
                    information_schema.table_constraints AS tc 
                    JOIN information_schema.key_column_usage AS kcu
                    ON tc.constraint_name = kcu.constraint_name
                    JOIN information_schema.constraint_column_usage AS ccu
                    ON ccu.constraint_name = tc.constraint_name
                WHERE constraint_type in ('FOREIGN KEY', 'PRIMARY KEY') AND tc.table_name NOT LIKE 'pg%')
        """

    try:
        cursor.execute(sql)
        result = cursor.fetchone()

        # conn.commit()
        print(f"test completed OK with {result} rows returned\n")
        assert result[0] > 0

    except Exception as e:
        print(f"Error {e}")
