#Yahtzee game code
import random
#Game code

class Game:             # Game class


    REROLLS = 2
    DICE = 5

    def __init__(self):
        self.dice = Dice()
        self.scorecard = Scorecard()
        self.roundnum = 0
        self.rerolls = 0        

    def round(self):
        self.roundnum += 1
        self.dice.roll()
        
        while self.rerolls < Game.REROLLS:
            self.dice.reroll()
            self.rerolls += 1
        
        self.scorecard.score_roll(self.dice)
        self.scorecard.show_scorecard()

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
        self.score = 0
        self.bonus = 0
        self.upper_score = 0
        self.lower_score = 0

    
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
        return self.dice.count(6) * 6
    
    def score_three_of_a_kind(self, dice):
        for die in dice:
            if dice.count(die) >= 3:
                return sum(dice)
            else:
                return 0
        
    def score_four_of_a_kind(self, dice):
        for die in dice:
            if dice.count(die) >= 4:
                return sum(dice)
            else:
                return 0

    def score_full_house(self, dice):
        for die in self.dice:
            if dice.count(die) == 3:
                for die in dice:
                    if dice.count(die) == 2:
                        return 25
            else:
                return 0

    def score_small_straight(self, dice):
        if sorted(dice) == [1, 2, 3, 4, 5]:
            return 30
        else:
            return 0

    def score_large_straight(self, dice):
        if sorted(dice) == [2, 3, 4, 5, 6]:
            return 40
        else:
            return 0
    
    def score_yahtzee(self, dice):
        for die in dice:
            if dice.count(die) == 5:
                return 50
            else:
                return 0

    def score_chance(self, dice):
        return sum(dice)
    
    def count_score(self):
        for key, value in self.scorecard.items():
            if key in ["ones", "twos", "threes", "fours", "fives", "sixes"]:
                self.upper_score += value
            else:
                self.lower_score += value
        if self.upper_score >= 63:
            self.bonus = 35
        self.score = self.upper_score + self.lower_score + self.bonus
        return self.score
    
    
class Dice:         # Dice class
    def __init__(self):
        self.dice = [0, 0, 0, 0, 0]

    def roll(self):
        # roll each of the dice in self.dice for a random number between 1 and 6
        for index in range(len(self.dice)):
            self.dice[index] = random.randint(1, 6)
        return print(self.dice)

                   
    def reroll(self):
        for index in range(len(self.dice)):
            choice = input(f"Would you like to reroll this die? :{self.dice[index]} (y/n)")
            if choice == "y":
                self.dice[index] = random.randint(1, 6)
            else:
                pass
        return print(self.dice)
    
    #counts the instances of a given number in the dice list
    def count(self, number):
        return self.dice.count(number)
    

if __name__ == "__main__":    # Main function
    game = Game()
    game.run()