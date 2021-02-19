from datetime import datetime


class GameOver(Exception):

    @staticmethod
    def scores(player_obj):
        with open('scores.txt', 'a') as scores:
            scores.write('{player_obj.score} {player_obj.name} '
                         '{str(datetime.now().replace(microsecond=0))}\n')
            print('\nSee you letter {player_obj.name}!\n'
                  'Your scores: {player_obj.score}\n')


class EnemyDown(Exception):
    pass


class InvalidLiteral(Exception):
    pass
