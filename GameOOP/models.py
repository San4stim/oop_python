from random import randint
from exceptions import EnemyDown, GameOver, InvalidLiteral
from settings import DEFAULT_LIVES_COUNT, ALLOWED_MOVES


class Enemy:
    lives = 1
    level = 1

    def __init__(self, name, level):
        self.name = name
        self.lives = level

    @staticmethod  # статикметод может вызывать без селф в качестве начального аргумента
    def select_attack():
        return randint(1, 3)  # рандомное число от 1 до 3

    def decrease_lives(self, player_obj):  # отбираем хп у врага и добавляем себе
        self.lives -= 1
        if self.lives <= 0:
            self.level += 1
            raise EnemyDown
        player_obj.score += 1


class Player:
    allowed_attack = 0
    score = 0
    lives = DEFAULT_LIVES_COUNT
    level = 1

    def __init__(self, name):
        self.name = name

    @staticmethod
    def fight(attack, defense):  # возврат результата боя
        if attack == defense:
            return 0
        if ((defense - attack) == 1) or ((attack - defense) == 2):
            return 1
        if ((defense - attack) == -1) or ((attack - defense) == -2):
            return -1

    def decrease_lives(self):  # здесь уменьшаем хп при уроне по нам
        self.lives -= 1
        if self.lives <= 0:  # если урона нанесли оч много то геймовер
            GameOver.scores(self)
            raise GameOver

    def attack(self, enemy_obj):  # здесь выводим результаты атаки в раунде прошел дамаг или нет
        if self.allowed_attack in ALLOWED_MOVES:
            result = self.fight(int(self.allowed_attack), enemy_obj.select_attack())

            if result == 0:
                print("Deadheat bro!")  # ничья
            elif result == 1:
                print("You attacked successfully!")  # атака прошла
                enemy_obj.decrease_lives(self)
            else:
                print("You missed!")  # когда промазал
        else:
            raise InvalidLiteral

    def defence(self, enemy_obj):  # тут когда дамаг проходит наоборот
        if self.allowed_attack in ALLOWED_MOVES:
            result = Player.fight(enemy_obj.select_attack(), int(self.allowed_attack))
            if result == 0:
                print("Deadhead from enemy")

            elif result == 1:
                print("Enemy attacked successfully!")
                self.decrease_lives()
            else:
                print("Enemy missed!")
        else:
            raise InvalidLiteral


class Scores:

    @staticmethod
    def show_score():
        with open('scores.txt', 'a+') as scores:
            sort_scores = sorted(scores.readlines(), reverse=True, key=lambda score: int(score[:2]))
            scores = [i.split() for i in sort_scores]
            scores_table = range(1, 11 if len(scores) > 10 else len(scores) + 1)
            for i in zip(scores_table, scores):
                print(f'{i[0]}. {i[1][1]} : {i[1][0]} | {i[1][2]} {i[1][3]}')
