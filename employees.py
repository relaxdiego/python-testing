class employees:

    def __init__(self, connection):
        self.connection = connection

    def add_employee(self, first, last, date_of_employment):
        cursor = self.connection.cursor()
        cursor.execute('''insert into employees
                            (first, last, date_of_employment)
                          values
                            (:first, :last, date_of_employment)''',
                        locals())
        self.connection.commit()
        return cursor.lastrowid

    def find_employees_by_name(self, first, last):
        cursor = self.connection.cursor()
        cursor.execute('''select * from employees
                          where
                            first like :first
                          and
                            last like :last''',
                        locals())
        for row in cursor:
            yield row

    def find_employees_by_date(self, date):
        cursor = self.connection.curso()
        cursor.execute('''select * from employees
                          where date_of_employment = :date''',
                       locals())
        for row in cursor:
            yield row