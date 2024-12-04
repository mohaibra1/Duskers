import datetime
import os.path
import re
import sys
import random

titanium = 0
default_names_locations = ['high street', 'Green park', 'Destroyed Arch']
locations = []
my_list = []
collect_titanium = []
player_name = ''
def welcome_note():
    welcome = r"""      ######*   ##*   ##*  #######*  ##*  ##*  #######*  ######*   #######*
     ##*  ##*  ##*   ##*  ##*       ##* ##*   ##*       ##*  ##*  ##*
     ##*  ##*  ##*   ##*  #######*  #####*    #####*    ######*   #######*
     ##*  ##*  ##*   ##*       ##*  ##* ##*   ##*       ##*  ##*       ##*
     ######*    ######*   #######*  ##*  ##*  #######*  ##*  ##*  #######*
                         (Survival ASCII Strategy Game)"""

    print('+================================================================+')
    print(welcome)
    print('+================================================================+')
def highscore():
    print('No Scores to display')
    print('     [Back]')
    while True:
        choice = input('Your command:\n')
        if choice.lower() == 'back':
            break
        else:
            print('Invalid input')
def help_duskters():
    print('Coming SOON! Thanks for playing!')

def get_input(prompt, valid_options):
    while True:
        choice = input(prompt).lower()
        if choice in valid_options:
            return choice
        print("Invalid input")

def generator(n):
    index = 1
    while index <= n:
        my_list.append(random.choice(locations))
        collect_titanium.append(random.randint(10, 100))
        yield index
        index += 1

def explore():
    global titanium
    count = 0
    print('Searching...')
    random_int = random.randint(1, 9)
    # for _ in range(random_int):
    my_generator = generator(random_int)
    count = next(my_generator)
    print(f"[1] {my_list[0]}")
    print()
    print('[S] to continue searching...')
    #my_generator = generator(random_int)
    #collect_titanium.append(random.randint(10, 100))
    while True:
        print()
        choice = input('Your command: ')
        if choice == 's':
            if count < random_int:
                count = next(my_generator)
                print(count)
                print('Searching...')
                for i in range(count):
                    print(f"[{i+1}] {my_list[i]}")
                print()
                print('[S] to continue searching...')
            else:
                print("Nothing more in sight.")
                print("        [Back]")
        elif choice == 'back':
            return False
        elif choice.isdigit():
            choice = int(choice) - 1
            if choice > len(my_list) or choice < 0:
                print('Invalid input')
                continue
            print()
            print("Deploying robots")
            print(f"{my_list[choice]} explored successfully, with no damage taken.")
            #random.seed(seed if seed else '')
            t = collect_titanium[choice]
            titanium += t
            print(f"Acquired {t} lumps of titanium")
            return False
        else:
            print('Invalid input')


def save_game():
    print("""select save slot: 
    [1] empty
    [2] empty
    [3] empty""")
    while True:
        choice = input('Your command: ')
        if choice.isdigit():
            if 0 < int(choice) < 4:
                date = datetime.datetime.now()
                str_game = f"{player_name} Titanium: {titanium} Robots: 3 Last save: {date}"
                with open('save_file.txt', 'a') as save_file:
                    save_file.write(str_game + '\n')

                print("""           
                |==============================|
                |    GAME SAVED SUCCESSFULLY   |
                |==============================|""")
                break
        elif choice == 'back':
            robot_display()
            break
        else:
            print('Invalid input')
def robot_display():
    while True:
        print(f"""
+==============================================================================+
  $   $$$$$$$   $  |  $   $$$$$$$   $  |  $   $$$$$$$   $
  $$$$$     $$$$$  |  $$$$$     $$$$$  |  $$$$$     $$$$$
      $$$$$$$      |      $$$$$$$      |      $$$$$$$
     $$$   $$$     |     $$$   $$$     |     $$$   $$$
     $       $     |     $       $     |     $       $
+==============================================================================+
| Titanium: {titanium}                                                                   |
+==============================================================================+
|                  [Ex]plore                          [Up]grade                |
|                  [Save]                             [M]enu                   |
+==============================================================================+""")
        choice = get_input("Your command: ", ['ex', 'up','save','m'])

        if choice.lower() == 'ex':
            my_list.clear()
            explore()
            collect_titanium.clear()
        elif choice.lower() == 'up':
            print('Coming SOON! ', end='')
            return False
        elif choice.lower() =='save':
            save_game()
        elif choice.lower() =='m':
            print("""    
              |==========================|
              |            MENU          |
              |                          |
              | [Back] to game           |
              | Return to [Main] Menu    |
              | [Save] and exit          |
              | [Exit] game              |
              |==========================|""")
            choice = get_input("Your command: ", ['back', 'main', 'save', 'exit'])
            if choice.lower() == 'back':
                continue
            elif  choice.lower() == 'main':
                return True
            elif choice.lower() =='exit':
                return False
            elif choice.lower() =='save':
                save_game()
                return False
        # elif choice.lower() == 'menu':  # exit
        #     break

def play_game():
    global player_name
    name = input('Enter your name:\n')
    print(f'Greetings, commander {name}!')
    player_name = name

    while True:
        print('Are you ready to begin?')
        print('[Yes] [No] Return to Main[Menu]')
        choice = get_input("Your command: ", ['yes', 'no', 'menu'])

        if choice.lower() == 'yes':
           if not robot_display():
                return False
           else:
               return True
        elif choice.lower() == 'no':
            print("How about now.")
        elif choice.lower() == 'menu':
            return True
        else:  # exit
            return False

def menu():
    welcome_note()
    print('[New] Game')
    print('[Load] Game')
    print('[High] Scores')
    print('[Help]')
    print('[Exit]')


def saved_game():
    global titanium, player_name
    save_lines = []
    print('Select save slot: ')
    if os.path.isfile('save_file.txt'):
        with open('save_file.txt', 'r') as save_file:
            index = 1
            for line in save_file.readlines():
                print(f"    [{index}] {line.strip()}")
                save_lines.append(line.strip())
                index += 1
    subtract = 3 - len(save_lines)
    if subtract < 3 or subtract == 3:
        for i in range(subtract):
            print(f"    [{i+1}] empty")

    while True:
        command = input('Your command: ')
        if command.isdigit():
            if len(save_lines) > 0:
                command = int(command) - 1
                match = re.search(r'Titanium:\s*(\d+)', save_lines[int(command)])
                parts = save_lines[int(command)].split("Titanium:")
                player_name = parts[0].strip()
                if match:
                    titanium = int(match.group(1))
                print("""
                        |==============================|
                        |    GAME LOADED SUCCESSFULLY  |
                        |==============================|""")
                print(f"Welcome back, commander {player_name}!")
                break
            else:
                print("Empty slot!")
                print("      Select save slot: ")
                for i in range(3):
                    print(f"{i+1} empty")
        elif command.lower() == 'back':
            break
        else:
            print('Invalid input')

def main():
    menu()

    while True:
        choice = get_input("Your command: ", ['new','load', 'high', 'help', 'exit'])

        if choice.lower() == 'new':
            if not play_game():
                break
            menu()
        elif choice.lower() == 'load':
            saved_game()
            robot_display()
        elif choice.lower() == 'high':
            highscore()
            menu()
        elif choice.lower() == 'help':
            help_duskters()
            break
        else:  # exit
            break
    print("Thanks for playing, bye!")


if __name__ == "__main__":
    if len(sys.argv) == 5:
        seed = sys.argv[1]
        min_duration_animation = sys.argv[2]
        max_duration_animation = sys.argv[3]
        names_locations = sys.argv[4]

        locations = names_locations.split(',')
        locations = [loc.replace('_', ' ') for loc in locations]

        random.seed(seed)
    else:
        random.seed('12')
        locations = default_names_locations

    main()