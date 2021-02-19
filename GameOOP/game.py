import settings as settings
from exceptions import GameOver, EnemyDown, InvalidLiteral
from models import Player, Enemy, Scores

# import names
names = ''


def play():
    level = 1
    player_name = input('Enter your name Player! \n')
    print("Welcome to The Hunger Games. And may luck always be on your side! {player_name}\n")
    player = Player(player_name)
    enemy_name = 'Vasya'  # names.get_first_name(gender='male')
    enemy = Enemy(enemy_name, level)

    while True:
        command = input(f"{player_name}, Please enter \"START\" to start the game\n").lower()

        if command == "start":
            print(f'Your enemy name is {enemy_name}!')
            while True:

                try:

                    player.allowed_attack = input('Please make a choice for attack: '
                                                  '\'1\' - Wizard, \'2\' - Warrior,'
                                                  ' \'3\' - Rogue \n')
                    player.attack(enemy)
                    print(f'Your lives: {player.lives} | {enemy_name} lives: {enemy.lives}\n')
                    player.allowed_attack = input('Please make a choice for defence: '
                                                  '\'1\' - Wizard, \'2\' - Warrior,'
                                                  ' \'3\' - Rogue \n')
                    player.defence(enemy)
                    print(f'Your lives: {player.lives} | {enemy_name} lives: {enemy.lives}\n')
                except EnemyDown:
                    player.score += 5
                    player.level += 1
                    level += 1
                    print(f'\n---------------------------------------------------------\n'
                          f' You killed {enemy_name}. Your score: '
                          f'{player.score}. Level: {player.level}.\n'
                          f'---------------------------------------------------------\n')  # format(self.enemy_name, ))
                    enemy_name = 'goga'
                    enemy = Enemy(enemy_name, level)
                    print(f'\nYour enemy name is {enemy_name}!\n')
                except InvalidLiteral:
                    print('\nONLY 3 classes of fighters!!! 1-2-3\n')

        if command == "show scores":
            print('\n')
            Scores.show_score()
            print('\n')

        # if command == "help":
        #     print(f'\nAllowed commands: {", ".join(settings.ALLOWED_COMMANDS)}.\n')

        if command == "exit":
            raise KeyboardInterrupt


if __name__ == '__main__':
    try:
        play()
    except GameOver:
        print('GAME OVER')
    except KeyboardInterrupt:
        pass
    finally:
        print('Good bye')
