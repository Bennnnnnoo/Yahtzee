#Yahtzee game code
import random


class Game:
    def __init__(self):
        self.dice = Dice()
        self.scorecard = Scorecard()
        self.round = 0

    def round(self):
        self.round += 1
        self.dice.roll()
        self.scorecard.show_scorecard()
        self.scorecard.score_roll(self.dice)

    def run(self):
        while self.round < 13:
            self.round()


class Scorecard:
    def __init__(self):
        self.scorecard = {
            "ones": None,
            "twos": None,
            "threes": None,
            "fours": None,
            "fives": None,
            "sixes": None,
            "three of a kind": None,
            "four of a kind": None,
            "full house": None,
            "small straight": None,
            "large straight": None,
            "yahtzee": None,
            "chance": None
        }

    def show_scorecard(self):
        print("Scorecard")
        for key, value in self.scorecard.items():
            print(f"{key}: {value}")

    def score_roll(self, dice):
        pass


class Dice:
    def __init__(self):
        self.dice = [0, 0, 0, 0, 0]

    def roll(self):
        for item in self.dice:
            item = random.randint(1, 6)
        


if __name__ == "__main__":
    game = Game()
    game.run()