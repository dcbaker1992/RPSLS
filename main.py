from play import Play

if __name__ == '__main__':
    again = True
    while again:
        game = Play()
        game.start_game()
        user_input = input("\n\n\nWould you like to play again? y/n")
        if user_input != "y":
            again = False
