from models import Employee
from models import Recruiter
from models import Programmer

programmer = Programmer(name='Vasya', email='slish@rambler.ru', salary=100)
print(programmer)
print(programmer.check_salary(50))

recruiter = Recruiter(name='masha', email='kisa666@mail.ru', salary=20)
print(recruiter)
print(recruiter.check_salary(8))
