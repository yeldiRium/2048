#game_field = GameField.BasicField()
#game_controller = GameController(game_field)


def input_invalid(user_input: str):
    return user_input not in ['n', 'e', 's', 'w', 'q']


while True:
    user_input = input('Wohin swipen? n/e/s/w | q for exit')
    if input_invalid(user_input):
        print('Ungültiger Input, bitte wiederholen.')
        continue
    else:
        if user_input == 'n':
            print("swiping north")
            # game_controller.swipeNorthAction()
        elif user_input == 'e':
            print("swiping east")
            # game_controller.swipeEastAction()
        elif user_input == 's':
            print("swiping south")
            # game_controller.swipeSouthAction()
        elif user_input == 'w':
            print("swiping west")
            # game_controller.swipeWestAction()
        else:
            exit()