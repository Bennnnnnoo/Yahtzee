#Yahtzee game code
import random
#Game code

class Game:             # Game class
    def __init__(self):
        self.dice = Dice()
        self.scorecard = Scorecard()
        self.roundnum = 0

    def round(self):
        self.roundnum += 1
        print(self.dice.roll())
        self.scorecard.show_scorecard()
        (self.dice.reroll())*3
        self.scorecard.score_roll(self.dice)

    def run(self):
        while self.roundnum < 13:
            self.round()


class Scorecard:        # Scorecard class - built in scoring methods
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

        print("How would you like to score this roll?")
        print("1. Ones")
        print("2. Twos")
        print("3. Threes")
        print("4. Fours")
        print("5. Fives")
        print("6. Sixes")
        print("7. Three of a kind") 
        print("8. Four of a kind")
        print("9. Full house")  # Add in validation later
        print("10. Small straight") # Add in validation later
        print("11. Large straight") # Add in validation later
        print("12. Yahtzee") # Add in validation later
        print("13. Chance")
        choice = int(input("Enter the number of your choice: "))
        if choice == 1:
            self.scorecard["ones"] = self.score_ones(dice)
        elif choice == 2:
            self.scorecard["twos"] = self.score_twos(dice)
        elif choice == 3:
            self.scorecard["threes"] = self.score_threes(dice)
        elif choice == 4:
            self.scorecard["fours"] = self.score_fours(dice)
        elif choice == 5:
            self.scorecard["fives"] = self.score_fives(dice)
        elif choice == 6:
            self.scorecard["sixes"] = self.score_sixes(dice)
        elif choice == 7:
            self.scorecard["three of a kind"] = self.score_three_of_a_kind(dice)
        elif choice == 8:
            self.scorecard["four of a kind"] = self.score_four_of_a_kind(dice)
        elif choice == 9:
            self.scorecard["full house"] = self.score_full_house(dice)
        elif choice == 10:
            self.scorecard["small straight"] = self.score_small_straight(dice)
        elif choice == 11:
            self.scorecard["large straight"] = self.score_large_straight(dice)
        elif choice == 12:
            self.scorecard["yahtzee"] = self.score_yahtzee(dice)
        elif choice == 13:
            self.scorecard["chance"] = self.score_chance(dice)
        else:
            print("Invalid choice")

    def score_ones(self, dice):
        return dice.count(1)
    
    def score_twos(self, dice):
        return dice.count(2) * 2
    
    def score_threes(self, dice):
        return dice.count(3) * 3
    
    def score_fours(self, dice):
        return dice.count(4) * 4
    
    def score_fives(self, dice):
        return dice.count(5) * 5
    
    def score_sixes(self, dice):
        return dice.count(6) * 6
    
    # def score_three_of_a_kind(self, dice):
        
    # def score_four_of_a_kind(self, dice):

    # def score_full_house(self, dice):

    # def score_small_straight(self, dice):

    # def score_large_straight(self, dice):
    
    # def score_yahtzee(self, dice):

    def score_chance(self, dice):
        return sum(dice)
    

class Dice:         # Dice class
    def __init__(self):
        self.dice = [0, 0, 0, 0, 0]

    def roll(self):
        for item in self.dice:
            item = random.randint(1, 6)
        return self.dice
        
    def reroll(self):
        for item in self.dice:
            choice = input("Would you like to reroll this die? {item} (y/n)")
            if choice == "y":
                item = random.randint(1, 6)
            else:
                pass

    def count(self, number):
        return self.dice.count(number)
    
if __name__ == "__main__":    # Main function
    game = Game()
    game.run()