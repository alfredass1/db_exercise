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


def create_view():
    query = """CREATE VIEW IF NOT EXISTS names
            as
            SELECT
                first_name,
                last_name
            FROM employees"""
    db_query(query)
    db_query(query)("SELECT * FROM names")


# create_view()

def get_all():
    query = "SELECT * FROM employees"
    db_query(query)


def get_3_1():
    query = """SELECT first_name, last_name, salary  FROM employees
    WHERE salary > (SELECT salary FROM employees WHERE last_name="Bull")"""
    db_query(query)


def get_3_2():
    query = """SELECT first_name, last_name, job_id, manager_id  FROM employees
    WHERE employee_id IN (SELECT manager_id FROM employees)"""
    db_query(query)


def get_3_3():
    query = """SELECT first_name, last_name, salary FROM employees
    WHERE salary > (SELECT AVG(salary) FROM employees)"""
    db_query(query)


def get_3_4():
    query = """SELECT first_name, last_name, salary 
    FROM employees
      WHERE salary = (SELECT min_salary FROM jobs WHERE employees.job_id = jobs.job_id)"""

    db_query(query)

def get_3_5():
    query = """SELECT first_name, last_name, salary, job_id FROM employees
        WHERE depatment_id IN (SELECT department_id FROM departments WHERE department_name LIKE "IT")"""
    db_query(query)

def get_3_6():
    query = """SELECT salary FROM employees
        WHERE salary IN (SELECT salary FROM employees ORDER BY salary DESC LIMIT 3)"""
    db_query(query)


def get_3_7():
    query = """SELECT first_name, last_name, FROM employees
        WHERE salary IN (SELECT salary FROM employees ORDER BY salary DESC LIMIT 3)"""
    db_query(query)





# get_3_2()
# get_all()
# get_3_1()
# get_3_3()
# get_3_4()
get_3_5()
# get_3_6()
# get_3_7()

