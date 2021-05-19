from human import Human
from computer import Computer
from gestures import Gestures


class Play:
    def __init__(self):
        self.player_one = Human(input("Enter Player 1 Name:"))
        self.player_two = Computer()
        self.round = 1

    def start_game(self):
        multiplayer = self.multiplayer()
        rounds_to_win = self.rounds()
        if multiplayer:
            self.player_two = Human("Player 2")
        while self.player_one.number_of_wins < rounds_to_win and self.player_two.number_of_wins < rounds_to_win:
            self.player_choice(self.player_one)
            if self.player_two.name == "Player 2":
                self.player_choice(self.player_two)
            else:
                self.comp_turn()
            self.results()
        self.show_winner()

    def multiplayer(self):
        try:
            user_input = int(input("Play Against Computer or Another Human\n"
                                   "1:Computer\n"
                                   "2:Human\n"))
            if user_input == 1:
                return False
            else:
                return True
        except:

            print("Pick 1 or 2")
            return self.multiplayer()

    def rounds(self):
        try:
            number = int(input("How many rounds must a player win?"))
            if number < 2:
                print("Player Must Win at Least 2 Rounds")
                return self.rounds()
            return number
        except:
            print("Please Enter the Number of Rounds")
            return self.rounds()

    def comp_turn(self):
        self.player_two.throw_gesture()

    def player_choice(self, player_turn):
        try:
            user_input = int(input(f"Round {self.round}\n"
                                   f"Score: {self.player_one.number_of_wins} to {self.player_two.number_of_wins}\n"
                                   f"{player_turn.name}: Make your choice!\n"
                                   f"1: rock\n"
                                   f"2: paper\n"
                                   f"3: scissors\n"
                                   f"4: lizard\n"
                                   f"5: spock\n")) - 1
            player_turn.choice = player_turn.gestures[user_input]
            assert user_input >= 0
        except:
            print("Pick a number 1 - 5 please.")
            self.player_choice(player_turn)
        print("\n" * 100)

    def results(self):
        print(f"{self.player_one.name} chooses: {self.player_one.choice}\n"
              f"{self.player_two.name} chooses: {self.player_two.choice}")
        if self.player_one.choice == self.player_two.choice:
            print("Draw! Go again!")
        else:
            self.compare_results()
            self.round += 1

    def compare_results(self):
        gesture_one = Gestures(self.player_one.choice)
        gesture_two = Gestures(self.player_two.choice)
        word = gesture_one.result(self.player_one.choice, self.player_two.choice)
        if word != "None":
            self.player_one.number_of_wins += 1
            self.display_results(self.player_one.name, self.player_one.choice, self.player_two.name,
                                 self.player_two.choice, word)
        else:
            self.player_two.number_of_wins += 1
            word = gesture_two.result(self.player_two.choice, self.player_one.choice)
            self.display_results(self.player_two.name, self.player_two.choice, self.player_one.name,
                                 self.player_one.choice, word)

    def display_results(self, winner, winner_choice, loser, loser_choice, word):
        print(f"{winner}'s {winner_choice} {word} {loser}'s {loser_choice}")

    def show_winner(self):
        if self.player_one.number_of_wins > self.player_two.number_of_wins:
            print(f"{self.player_one.name} is the winner!")
        else:
            print(f"{self.player_two.name} is the winner!")
