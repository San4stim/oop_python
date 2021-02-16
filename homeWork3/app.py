from models import Programmer, Recruiter, Vacancy, Candidate


def main():
    recruiter_1 = Recruiter('Bon Jovi', 'some@gmail.com', 20)
    programmer_1 = Programmer('Jason Stathem', 'zbs@mail.ru', 50)
    programmer_2 = Programmer('Vin Diesel', 'lisiy.iz.brazzers@rambler.ru', 60)
    candidate_1 = Candidate('John Snow', 'iamalive@got.usa', 'Jaba-Java', 'trainee')
    candidate_2 = Candidate('Hodor', 'hodor@hodor.hodor', 'Hodor', 'hodor')
    candidate_3 = Candidate('Groot', 'iamgroot@groot', '01001101 programmer', 'guardian of senior')
    vacancy_1 = Vacancy('Python')
    vacancy_2 = Vacancy('01001101 programmer')


if __name__ == '__main__':
    main()
