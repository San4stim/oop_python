class Employee(object):

    def __init__(self, name, email, salary):
        self.name = name
        self.email = email
        self.salary = salary

    def work(self):
        return 'I come to the office '

    def check_salary(self, worked_days):
        payment_days = self.salary * worked_days
        return 'Worker have a {} payment'.format(payment_days)


class Programmer(Employee):
    def work(self):
        return 'I come to the office and start to coding'

    def __str__(self):
        return 'This is {} he/she is {}'.format(self.name, self.__class__.__name__)


class Recruiter(Employee):
    def work(self):
        return 'I come to the office and start to hiring'

    def __str__(self):
        return 'This is {} he/she is {}'.format(self.name, self.__class__.__name__)


programmer = Programmer(name='Vasya', email='slish@rambler.ru', salary=100)
print(programmer)
print(programmer.check_salary(50))

recruiter = Recruiter(name='masha', email='kisa666@mail.ru', salary=20)
print(recruiter)
print(recruiter.check_salary(8))
