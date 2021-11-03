from datetime import datetime
from application_1.salary import *
from db_1.people import *


if __name__ == '__main__':
    print(f'По состоянию на: -  {datetime.now(tz=None).date()}')
    s= Salary(None)
    s.calculate_salary()
    e = Employees(None)
    e.get_employees()