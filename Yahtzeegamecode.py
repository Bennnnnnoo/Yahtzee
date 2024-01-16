#Yahtzee game code
import random, math, PySimpleGUI as sg



class Player:           # Player class
    def __init__(self):
        
        self.name = None
        self.scorecard = Scorecard()

    def get_name(self):
        return self.name
    
    def get_scorecard(self):
        return self.scorecard
    
    def get_score(self):
        return self.scorecard.score
    
    def get_bonus(self):
        return self.scorecard.bonus
    
    def get_upper_score(self):
        return self.scorecard.upper_score
    
    def get_lower_score(self):
        return self.scorecard.lower_score


    def get_total_score(self):
        return self.scorecard.total_score
 


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

    
    def show_scorecard(self):
        print("Scorecard")
        for key, value in self.scorecard.items():
            print(f"{key}: {value}")

    def score_roll(self, dice, choice):

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
            
        return 0
    
    
    def score_four_of_a_kind(self, dice):
        for die in dice.get_dice():
            if dice.count(die) >= 4:
                return sum(dice.get_dice())
        
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
            if value == None:
                    value = 0
            if key in ["ones", "twos", "threes", "fours", "fives", "sixes"]:
                
                self.upper_score += value
            else:
                self.lower_score += value
        if self.upper_score >= 63:
            self.bonus = 35
        self.score = self.upper_score + self.lower_score + self.bonus
        return self.score
    
    def get_scorecard(self):
        return self.scorecard
    
    def get_score(self):
        return self.score
    
class Dice:         # Dice class
    def __init__(self):
        #self.dice = [1,3,1,4,2]     #test case
        self.dice = [0 for i in range(Game.DICE)]
        

   

    def get_dice(self):
        return self.dice

   
    
    def roll(self):
        # roll each of the dice in self.dice for a random number between 1 and 6
        for index in range(len(self.dice)):
            self.dice[index] = random.randint(1, 6)
        return self.dice


    
                   
    def reroll(self, rerollchoice):
        # reroll the dice in self.dice that the user chooses

        for choice in rerollchoice:
            self.dice[int(choice)-1] = random.randint(1, 6)

       
    
    #counts the instances of a given number in the dice list
    def count(self, number):
        return self.dice.count(number)
    
        
    


class Game:             # Game class


    #initialise constants
    REROLLS = 2
    DICE = 5
    NUM_ROUNDS = 13
    

    def __init__(self):
        
        self.AIplayers = 0
        self.dice = Dice()
        self.scorecard = Scorecard()
        self.roundnum = 0
        self.rerolls = 0        
        #allow multiple players
        self.players = []
        self.winner = None
        self.takennames = []
        

    def get_winner(self):
        
        current_score = 0
    
        for player in self.players:
            score = player.get_scorecard().count_score()
            if score >= current_score:
                current_score = score
                self.winner = player
            
        return self.winner   
      


class EasyAI(Player):

    def __init__(self):
        super().__init__()
        self.name = "Easy AI"
        self.scorecard = Scorecard()

    def play(self, dice):
        self.scorecard.score_roll(dice, self.__choosecategory(dice))


    def __merge_sort(self, alist):
        if len(alist) <= 1:
            return alist
        else:
            left = self.__merge_sort(alist[:len(alist)//2])
            right = self.__merge_sort(alist[len(alist)//2:])
            return self.__merge(left, right)
        
    def __merge(self, left, right):
        result = []
        while len(left) > 0 and len(right) > 0:
            if left[0] <= right[0]:
                result.append(left.pop(0))
            else:
                result.append(right.pop(0))
        if len(left) > 0:
            result.extend(left)
        else:
            result.extend(right)
        return result

# count how many of each dice there are

    def FindDiceState(self,dice_list):
        # Initialize a dictionary to store the count of each dice value
        dice_count = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}

        # Iterate through the dice_list and update the counts
        for value in dice_list:
            # Check if the value is a valid dice value
            if value in dice_count:
                # Increment the count for the respective dice value
                dice_count[value] += 1
            else:
                print(f"Illegal dice value: {value}")

        return dice_count
        
    

    def __choosecategory(self, dice):
        #dicestates = self.FindDiceState(dice)
        
        # make dictionary of scorable categories

        scoreablecategories = self.scorecard.get_scorecard()
        for key, value in scoreablecategories.items():
            if value != None:
                del scoreablecategories[key]

        predicted_scores = {}

        for key, value in scoreablecategories.items():
            if key == "1.ones":
                predicted_scores[key] = self.scorecard.score_ones(dice)
            elif key == "2.twos":
                predicted_scores[key] = self.scorecard.score_twos(dice)
            elif key == "3.threes":
                predicted_scores[key] = self.scorecard.score_threes(dice)
            elif key == "4.fours":
                predicted_scores[key] = self.scorecard.score_fours(dice)
            elif key == "5.fives":
                predicted_scores[key] = self.scorecard.score_fives(dice)
            elif key == "6.sixes":
                predicted_scores[key] = self.scorecard.score_sixes(dice)
            elif key == "7.three of a kind":
                predicted_scores[key] = self.scorecard.score_three_of_a_kind(dice)
            elif key == "8.four of a kind":
                predicted_scores[key] = self.scorecard.score_four_of_a_kind(dice)
            elif key == "9.full house":
                predicted_scores[key] = self.scorecard.score_full_house(dice)
            elif key == "10.small straight":
                predicted_scores[key] = self.scorecard.score_small_straight(dice)
            elif key == "11.large straight":
                predicted_scores[key] = self.scorecard.score_large_straight(dice)
            elif key == "12.yahtzee":
                predicted_scores[key] = self.scorecard.score_yahtzee(dice)
            elif key == "13.chance":
                predicted_scores[key] = self.scorecard.score_chance(dice)
            else:
                raise NotImplementedError
            
        # sort the dictionary by value
        
        sorted_scores = dict(self.__merge_sort(predicted_scores.items(), key=lambda x: x[1]))
        chosen_category =sorted_scores.popitem()

        return chosen_category[0]
        







        

