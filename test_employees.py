from unittest import TestCase, main
from sqlite3 import connect, PARSE_DECLTYPES
from datetime import date
from employees import employees

class test_employees(TestCase):

    def setUp(self):
        connection = connect(':memory:',
                             detect_types=PARSE_DECLTYPES)
        cursor = connection.cursor()
        cursor.execute('''create table employees
                            (first text,
                             last test,
                             date_of_employment date)''')
        cursor.execute('''insert into employees
                            (first, last, date_of_employment)
                          values
                            ("Test1", "Employee", :date)''',
                       {'date': date(year = 2003,
                                     month = 7,
                                     day = 12)})
        cursor.execute('''insert into employees
                            (first, last, date_of_employment)
                          values
                            ("Test2", "Employee", :date)''',
                       {'date': date(year = 2001,
                                     month = 3,
                                     day = 18)})
        self.connection = connection

    def tearDown(self):
        self.connection.close()