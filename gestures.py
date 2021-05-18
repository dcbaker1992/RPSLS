class Gestures:
    def __init__(self, gesture):
        self.gesture = gesture
        self.defeats = {}
        if self.gesture == "rock":
            self.defeats.update({"scissors": "crushes"})
            self.defeats.update({"lizard": "crushes"})
        elif self.gesture == "paper":
            self.defeats.update({"rock": "covers"})
            self.defeats.update({"spock": "disproves"})
        elif self.gesture == "scissors":
            self.defeats.update({"paper": "cuts"})
            self.defeats.update({"lizard": "decapitates"})
        elif self.gesture == "lizard":
            self.defeats.update({"paper": "eats"})
            self.defeats.update({"spock": "poisons"})
        elif self.gesture == "spock":
            self.defeats.update({"scissors": "smashes"})
            self.defeats.update({"rock": "vaporizes"})

    def result(self, player_one_choice, player_two_choice):
        if player_two_choice in self.defeats.keys():
            return self.defeats[player_two_choice]
        else:
            return "None"