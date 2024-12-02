import sys
import random

titanium = 0
default_names_locations = ['high street', 'Green park', 'Destroyed Arch']
locations = []
my_list = []
collect_titanium = []
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
            print('Coming SOON! Thanks for playing!')
            return False
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
                print('Coming SOON! Thanks for playing!')
                return False
        # elif choice.lower() == 'menu':  # exit
        #     break

def play_game():
    name = input('Enter your name:\n')
    print(f'Greetings, commander {name}!')

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
    print('[Play]')
    print('[High] Scores')
    print('[Help]')
    print('[Exit]')

def main():
    menu()

    while True:
        choice = get_input("Your command: ", ['play','high', 'help', 'exit'])

        if choice.lower() == 'play':
            if not play_game():
                break
            menu()
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