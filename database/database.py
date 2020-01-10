import sqlite3


def open_connection():
    connection = sqlite3.connect("exercise.db")
    cursor = connection.cursor()
    return connection, cursor


def close_connection(connection, cursor):
    connection.close()


def db_query(query, params=None):
    try:
        connection, cursor = open_connection()
        if params:
            cursor.execute(query)
            connection.commit()
        else:
            for row in cursor.execute(query):
                print(row)
    except sqlite3.DatabaseError as error:
        print(error)
    finally:
        close_connection(connection, cursor)


def exercise1_1():
    query = "SELECT first_name, last_name, salary FROM employees WHERE salary BETWEEN 10000 AND 15000"
    db_query(query)


def exercise1_2():
    query = "SELECT first_name, last_name, department_id FROM employees ORDER BY department_id ASC LIMIT 30"
    db_query(query)


def exercise1_3():
    query = "SELECT first_name, last_name, salary FROM employees WHERE salary BETWEEN 10000 AND 15000 LIMIT 30"
    db_query(query)


def exercise1_4():
    query = "SELECT first_name FROM employees WHERE first_name LIKE '%b%c%'"
    db_query(query)


def exercise1_5():
    query = "SELECT last_name, job_id, salary FROM employees WHERE job_id LIKE '%Clerk' "
    db_query(query)


def exercise1_6():
    query = "SELECT first_name, last_name FROM employees WHERE LENGTH(Last_name)= 6"
    db_query(query)


def exercise1_7():
    query = """SELECT last_name FROM employees 
               WHERE last_name LIKE '__e%' """
    db_query(query)


def exercise2_1():
    query = """SELECT DISTINCT job_id FROM employees """
    db_query(query)


def exercise2_2():
    query = """SELECT SUM(salary) as total_salary FROM employees"""
    db_query(query)


def exercise2_3():
    query = """SELECT salary FROM employees
                ORDER by salary ASC
                LIMIT 1"""
    db_query(query)


def exercise2_4():
    query = """SELECT salary FROM employees
            ORDER by salary DESC
            LIMIT 1"""
    db_query(query)


def exercise2_5():
    query = """SELECT AVG(salary) as avg_salary, COUNT(employee_id) FROM employees
            WHERE department_id = 90"""
    db_query(query)


def exercise2_6():
    query = """SELECT MIN(salary), MAX(salary), SUM(salary), AVG(salary) FROM employees"""
    db_query(query)


def create_name_view():
    query = """CREATE VIEW IF NOT EXISTS name
                   AS SELECT 
                   first_name,                 
                   last_name,
                   FROM employees"""
    query_database(query)
    query_database("SELECT * FROM name")


def subquery_exercise1():
    query = """SELECT first_name, last_name, salary
            FROM employees
            WHERE salary > (SELECT salary
                            FROM employees
                            WHERE last_name='Bull')"""

query_with_in = """SELECT first name, last_name, employee_id, manager_id
                FROM employees 
                WHERE (emloyee_id IN (SELECT manager_id FROM employees))"""

db_query("PRAGMA table__info(departments)")
subquery_exercise1()


def subquery_exercise2():
    query = """SELECT first_name, last_name




