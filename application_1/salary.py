class Salary:
    def __init__(self, messege):
        self.messege = messege

    def __str__(self):
        return self.messege

    def calculate_salary(self):
        self.messege = ("Функция расчета зароботной платы не реализована")
        print(self.messege)

if __name__ == '__main__':
    s = Salary(None)
    s.calculate_salary()

