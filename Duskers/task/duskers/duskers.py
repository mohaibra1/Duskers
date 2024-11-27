def welcome_note():
    print('+================================================================+')
    welcome = r"""   _____         .__                              .___
      /     \   ____ |  |__ _____    _____   ____   __| _/
     /  \ /  \ /  _ \|  |  \\__  \  /     \_/ __ \ / __ | 
    /    Y    (  <_> )   Y  \/ __ \|  Y Y  \  ___// /_/ | 
    \____|__  /\____/|___|  (____  /__|_|  /\___  >____ | 
            \/            \/     \/      \/     \/     \/ """

    print(welcome)
    print('+================================================================+')

def main():
    welcome_note()
    print('[Play]')
    print('[Exit]')
    play = True
    while play:
        choice  = input("your command: ")
        choice = choice.lower()
        if choice == 'play':
            name = input('Enter your name:\n ')
            print(f'Greetings, commander {name}!')
            print('Are you ready to begin?')
            print('        [Yes] [No]      ')
            start = True
            while start:
                choice = input("your command: ")

                if choice.lower() == 'yes':
                    print("Great, now let's go code some more ;)")
                    play = False
                    break
                elif choice.lower() == 'no':
                    while True:
                        print("How about now.")
                        print('Are you ready to begin?')
                        print('        [Yes] [No]      ')
                        choice = input("your command: ")
                        if choice.lower() == 'yes':
                            print("Great, now let's go code some more ;)")
                            start = False
                            play = False
                            break
                        elif choice.lower() == "exit":
                            print("Goodbye!")
                            start = False
                            play = False
                            break
                        else:
                            print("Invalid input")
                elif choice.lower() == 'exit':
                    print("Goodbye!")
                    play = False
                    break
                else:
                    print("Invalid input")
        elif choice.lower()== 'exit':
            print("Goodbye!")
            break
        else:
            print("Invalid input")
if __name__ == "__main__":
    main()
