#Yahtzee game code
import random


class Game:             # Game class


    REROLLS = 2
    DICE = 5

    def __init__(self):
        self.dice = Dice()
        self.scorecard = Scorecard()
        self.roundnum = 0
        self.rerolls = 0        
        #allow multiple players
        self.players = []

        

    def round(self):
        self.roundnum += 1
        self.dice.roll()
        
        
        while self.rerolls < Game.REROLLS:
            self.dice.reroll()
            self.rerolls += 1
        
        self.scorecard.score_roll(self.dice)
        self.scorecard.show_scorecard()
        self.rerolls = 0 

    def run(self):
        print ("Welcome to Yahtzee!")
        players = int(input("Enter the number of players: "))
        for player in range(players):
            self.players.append(Player())
        while self.roundnum < 13*len(self.players):
            self.round()

class Player:           # Player class
    def __init__(self):
        self.name = input("Enter your name: ")
        self.scorecard = Scorecard()
        self.score = 0
        self.bonus = 0
        self.upper_score = 0
        self.lower_score = 0
        self.total_score = 0
    
    def get_name(self):
        return self.name
    
    def get_scorecard(self):
        return self.scorecard
    
    def get_score(self):
        return self.score
    
    def get_bonus(self):
        return self.bonus
    
    def get_upper_score(self):
        return self.upper_score
    
    def get_lower_score(self):
        return self.lower_score
    
    def get_total_score(self):
        return self.total_score
 


class Scorecard:        # Scorecard class - built in scoring methods
    def __init__(self):
        self.scorecard = {
            "1.ones": None,
            "2.twos": None,
            "3.threes": None,
            "4.fours": None,
            "5.fives": None,
            "6.sixes": None,
            "7.three of a kind": None,
            "8.four of a kind": None,
            "9.full house": None,
            "10.small straight": None,
            "11.large straight": None,
            "12.yahtzee": None,
            "13.chance": None
        }
        self.score = 0
        self.bonus = 0
        self.upper_score = 0
        self.lower_score = 0
        self.total_score = 0
        self.keylist = [key for key in self.scorecard.keys()]

# add in choice validation, prevent user from choosing same option twice



    def get_choice(self):
        try:
            choice = (input("Enter your choice: "))
            if choice not in range(1, 14):
                choice = self.get_choice()
            #prevent user from choosing same option twice
            if self.scorecard[self.keylist[choice-1]] != None:
                choice = self.get_choice()
        except ValueError or TypeError:
            print("Invalid choice")
            choice = self.get_choice()
        return choice
    
    def show_scorecard(self):
        print("Scorecard")
        for key, value in self.scorecard.items():
            print(f"{key}: {value}")

    def score_roll(self, dice):

        print("Enter the number of the category you would like to score")
        self.show_scorecard()
        choice = self.get_choice()



        if choice == 1:
            self.scorecard["1.ones"] = self.score_ones(dice)
        elif choice == 2:
            self.scorecard["2.twos"] = self.score_twos(dice)
        elif choice == 3:
            self.scorecard["3.threes"] = self.score_threes(dice)
        elif choice == 4:
            self.scorecard["4.fours"] = self.score_fours(dice)
        elif choice == 5:
            self.scorecard["5.fives"] = self.score_fives(dice)
        elif choice == 6:
            self.scorecard["6.sixes"] = self.score_sixes(dice)
        elif choice == 7:
            self.scorecard["7.three of a kind"] = self.score_three_of_a_kind(dice)
        elif choice == 8:
            self.scorecard["8.four of a kind"] = self.score_four_of_a_kind(dice)
        elif choice == 9:
            self.scorecard["9.full house"] = self.score_full_house(dice)
        elif choice == 10:
            self.scorecard["10.small straight"] = self.score_small_straight(dice)
        elif choice == 11:
            self.scorecard["11.large straight"] = self.score_large_straight(dice)
        elif choice == 12:
            self.scorecard["12.yahtzee"] = self.score_yahtzee(dice)
        elif choice == 13:
            self.scorecard["13.chance"] = self.score_chance(dice)
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
    
    def score_three_of_a_kind(self, dice):
        for die in dice.get_dice():
            if dice.count(die) >= 3:
                return sum(dice.get_dice())
            else:
                return 0
    
    
    def score_four_of_a_kind(self, dice):
        for die in dice.get_dice():
            if dice.count(die) >= 4:
                return sum(dice.get_dice())
            else:
                return 0
       


  
        
      

    def score_full_house(self, dice):
        countlist = []
        for die in dice.get_dice():
            countlist.append(dice.count(die))
        if 3 in countlist and 2 in countlist:
            return 25
        else:
            return 0


    def score_small_straight(self, dice):
        sortedlist = []
        for die in sorted(dice.get_dice()):
            if die not in sortedlist:
                sortedlist.append(die)
        if sortedlist == [1, 2, 3, 4] or sortedlist == [2, 3, 4, 5] or sortedlist == [3, 4, 5, 6] or sortedlist == [1, 2, 3, 4, 5] or sortedlist == [2, 3, 4, 5, 6]:
            return 30
        else:
            return 0
       
        # check quicker using regex?
        
     


    def score_large_straight(self, dice):
        if sorted(dice.get_dice()) == [2, 3, 4, 5, 6] or sorted(dice.get_dice()) == [1, 2, 3, 4, 5]:
            return 40
        else:
            return 0
    
    def score_yahtzee(self, dice):
        for die in dice.get_dice():
            if dice.count(die) == 5:
                return 50
            else:
                return 0

    def score_chance(self, dice):
        return sum(dice.get_dice())
    
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
    #    self.dice = [5,2,1,4,3]     #test case
        self.dice = [0 for i in range(Game.DICE)]
        

    #def __repr__(self) -> str:
        #return f"{self.dice}"

    def get_dice(self):
        return self.dice

    def get_reroll_choice(self,dice):

        # validate user input for reroll choice
        
        try:
            choice = input(f"Would you like to reroll {dice} : (y/n)")
            if choice not in ["y", "n"]:
                print("Invalid choice")
                choice = self.get_reroll_choice(dice)

        except ValueError or TypeError:
            print("Invalid choice")
            choice = self.get_reroll_choice(dice)
    
        return choice
    
    def roll(self):
        # roll each of the dice in self.dice for a random number between 1 and 6
        for index in range(len(self.dice)):
            self.dice[index] = random.randint(1, 6)
        return print(self.dice)


    
                   
    def reroll(self):
        for index in range(len(self.dice)):
            
            choice = self.get_reroll_choice(self.dice[index])
            if choice == "y":
                self.dice[index] = random.randint(1, 6)
            else:
                pass
        return print(self.dice)
    
    #counts the instances of a given number in the dice list
    def count(self, number):
        return self.dice.count(number)
    


# User interface for yahtzee
#class Ui:
    #def __init__(self):
     #   pass

    #def get_choice(self):
     #   choice = input("Enter choice: ")
      #  return int(choice)
    


if __name__ == "__main__":    # Main function
    game = Game()
    game.run()