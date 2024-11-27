
def welcome_note():
    welcome = r"""   _____         .__                              .___
      /     \   ____ |  |__ _____    _____   ____   __| _/
     /  \ /  \ /  _ \|  |  \\__  \  /     \_/ __ \ / __ | 
    /    Y    (  <_> )   Y  \/ __ \|  Y Y  \  ___// /_/ | 
    \____|__  /\____/|___|  (____  /__|_|  /\___  >____ | 
            \/            \/     \/      \/     \/     \/ """
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

def robot_display():
    while True:
        print("""
+==============================================================================+
  $   $$$$$$$   $  |  $   $$$$$$$   $  |  $   $$$$$$$   $
  $$$$$     $$$$$  |  $$$$$     $$$$$  |  $$$$$     $$$$$
      $$$$$$$      |      $$$$$$$      |      $$$$$$$
     $$$   $$$     |     $$$   $$$     |     $$$   $$$
     $       $     |     $       $     |     $       $
+==============================================================================+
|                  [Ex]plore                          [Up]grade                |
|                  [Save]                             [M]enu                   |
+==============================================================================+""")
        choice = get_input("Your command: ", ['ex', 'up','save','m'])

        if choice.lower() == 'ex':
            return False
        elif choice.lower() == 'up':
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

    print("Goodbye!")


if __name__ == "__main__":
    main()