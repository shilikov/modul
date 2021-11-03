from datetime import datetime
from application.salary import Salary
from application.db.people import Employees


if __name__ == '__main__':
    print(f'По состоянию на: - {datetime.now(tz=None).date()}')
    s= Salary(None)
    s.calculate_salary()
    e = Employees(None)
    e.get_employees()


