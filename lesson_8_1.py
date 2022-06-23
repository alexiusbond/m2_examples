import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn


def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


def create_student(conn, student):
    """
    Create a new student into the students table
    :param conn:
    :param student:
    :return: student id
    """
    sql = ''' INSERT INTO students(full_name, mark, hobby, birth_date, is_married)
              VALUES(?, ?, ?, ?, ?); '''
    cur = conn.cursor()
    cur.execute(sql, student)
    conn.commit()
    return cur.lastrowid


def update_student_mark(conn, student):
    """
    update mark of a student
    :param conn:
    :param student:
    :return:
    """
    sql = ''' UPDATE students SET mark = ? WHERE id = ?; '''
    cur = conn.cursor()
    cur.execute(sql, student)
    conn.commit()


def delete_student(conn, id):
    """
    Delete a student by student id
    :param conn:  Connection to the SQLite database
    :param id: id of the student
    :return:
    """
    sql = ''' DELETE FROM students WHERE id = ?; '''
    cur = conn.cursor()
    cur.execute(sql, (id,))
    conn.commit()


def select_all_students(conn):
    """
    Query all rows in the students table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM students")

    rows = cur.fetchall()

    for row in rows:
        print(row)


def select_students_by_mark(conn, mark):
    """
    Query students by mark
    :param conn: the Connection object
    :param priority:
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM students WHERE mark >= ?", (mark,))

    rows = cur.fetchall()

    for row in rows:
        print(row)


database = r'example.db'
sql_create_students_table = ''' 
CREATE TABLE students (
id INTEGER PRIMARY KEY AUTOINCREMENT,
full_name VARCHAR (200) NOT NULL,
mark DOUBLE (5, 2) NOT NULL DEFAULT 0.0,
hobby TEXT DEFAULT NULL,
birth_date DATE NOT NULL,
is_married BOOLEAN DEFAULT FALSE
); '''

conn = create_connection(database)

# create tables
if conn is not None:
    print("Connected successfully!")

    create_table(conn, sql_create_students_table)

    create_student(conn, ("Mark Daniels", 77.12, "Football", "1999-01-02", False))
    create_student(conn, ("Alex Brilliant", 77.12, None, "1989-12-31", True))
    create_student(conn, ("Diana Julls", 99.3, "Tennis", "2005-01-22", True))
    create_student(conn, ("Michael Corse", 100.0, "Diving", "2001-09-17", True))
    create_student(conn, ("Jack Moris", 50.2, "Fishing and cooking", "2001-07-12", True))
    create_student(conn, ("Viola Manilson", 41.82, None, "1991-03-01", False))
    create_student(conn, ("Joanna Moris", 100.0, "Painting and arts", "2004-04-13", False))
    create_student(conn, ("Peter Parker", 32.0, "Travelling and bloging", "2002-11-28", False))
    create_student(conn, ("Paula Parkerson", 77.09, None, "2001-11-28", True))
    create_student(conn, ("George Newel", 93.0, "Photography", "1981-01-24", True))
    create_student(conn, ("Miranda Alistoun", 87.55, "Playing computer games", "1997-12-22", False))
    create_student(conn, ("Fiona Giordano", 66.12, "Driving fast", "1977-01-15", True))

    # update_student_mark(conn, (99.2, 2))

    # delete_student(conn, 4)

    select_all_students(conn)

    # select_students_by_mark(conn, 90.0)
    conn.close()
else:
    print("Error! cannot create the database connection.")
