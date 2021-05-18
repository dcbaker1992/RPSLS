from play import Play

if __name__ == '__main__':
    again = True
    while again:
        game = Play()
        game.start_game()
        user_input = input("\nPlay again? yes or no")
        if user_input != "yes":
            again = False
