from player import Player
import random


class Computer:
    def __init__(self):
        self.name = "Computer"
        super().__init__()

    def throw_gesture(self):
        self.choice = self.gestures[random.randint(0, 5)]
