from datetime import datetime


class GameOver(Exception):

    @staticmethod
    def scores(player_obj):
        with open('scores.txt', 'a') as scores:
            scores.write(f'{player_obj.score} {player_obj.name} '
                         f'{str(datetime.now().replace(microsecond=0))}\n')
            print(f'\nSee you letter {player_obj.name}!\n'
                  f'Your scores: {player_obj.score}\n')


class EnemyDown(Exception):
    pass


class InvalidLiteral(Exception):
    pass
