# import SQLAlchemy
# import psycopg2

class Employees:
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message

    def get_employees(self):
        raise FileNotFoundError('файл со списком сотрудников не найден')



if __name__ == '__main__':
    e = Employees(None)
    e.get_employees()
