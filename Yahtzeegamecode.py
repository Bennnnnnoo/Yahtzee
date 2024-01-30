## Yahtzee game code ##

import random, math, PySimpleGUI as sg, re, numpy as np



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
        
        
    # use regex to check for small straight
    def score_small_straight(self, dice):
        match = re.search(r'1234|2345|3456|12345|23456', ''.join(str(die) for die in sorted(list(set(dice.get_dice())))))
        if match:
            return 30
        else:
            return 0

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
        # add bonus if applicable
        if self.upper_score >= 63:
            self.bonus = 35
        self.score = self.upper_score + self.lower_score + self.bonus
        return self.score
    
    def get_scorecard(self):
        return self.scorecard
    
    def get_score(self):
        return self.score
    
    def genlist(self):
        dictlist = []
        for key, value in self.scorecard.items():
            dictlist.append([key,value])
        return dictlist

        
    
class EZBoard(Scorecard): # player assistance board
    def __init__(self, player):
        super().__init__()
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
        self.player = player

    def update_scorecard(self, dice):
        #calculate expected value for each category
        for key in self.scorecard:
            
                if key == "1.ones":
                    self.scorecard[key] = self.score_ones(dice)
                elif key == "2.twos":
                    self.scorecard[key] = self.score_twos(dice)
                elif key == "3.threes":
                    self.scorecard[key] = self.score_threes(dice)
                elif key == "4.fours":
                    self.scorecard[key] = self.score_fours(dice)
                elif key == "5.fives":
                    self.scorecard[key] = self.score_fives(dice)
                elif key == "6.sixes":
                    self.scorecard[key] = self.score_sixes(dice)
                elif key == "7.three of a kind":
                    self.scorecard[key] = self.score_three_of_a_kind(dice)
                elif key == "8.four of a kind":
                    self.scorecard[key] = self.score_four_of_a_kind(dice)
                elif key == "9.full house":
                    self.scorecard[key] = self.score_full_house(dice)
                elif key == "10.small straight":
                    self.scorecard[key] = self.score_small_straight(dice)
                elif key == "11.large straight":
                    self.scorecard[key] = self.score_large_straight(dice)
                elif key == "12.yahtzee":
                    self.scorecard[key] = self.score_yahtzee(dice)
                elif key == "13.chance":
                    self.scorecard[key] = self.score_chance(dice)
                else:
                    raise NotImplementedError

            
          
            
        return self.scorecard
    
    def bonus_calc(self):
        if self.player.get_upper_score() >= 63:
            return '35'
        else:
            return f'0, ({self.player.get_upper_score() - 63})'
            
    
    
        

    

    
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
        
    # find winner
    def get_winner(self):
        
        current_score = 0
    
        for player in self.players:
            score = player.get_scorecard().count_score()
            if score >= current_score:
                current_score = score
                self.winner = player
            
        return self.winner   
    
    
      

# Easy AI class
class EasyAI(Player):

    def __init__(self):
        super().__init__()
        self.name = "Easy AI"
        self.scorecard = Scorecard()
        self.rerolls = 2
        self.dice = Dice()
        

    def play(self, dice):
        self.scorecard.score_roll(dice, self.__choosecategory(dice))

    # merge sort algorithm to sort the dictionary by value
    def __merge_sort(self, alist):
        if len(alist) <= 1:
            return alist
        mid = len(alist) // 2
        left = alist[:mid]
        right = alist[mid:]

        self.__merge_sort(left)
        self.__merge_sort(right)

        i = 0
        j = 0
        k = 0

        while i < len(left) and j < len(right):
            if left[i][1] < right[j][1]:
                alist[k] = left[i]
                i += 1
            else:
                alist[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            alist[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            alist[k] = right[j]
            j += 1
            k += 1

        return alist
        

            

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
        
        
        # make dictionary of scorable categories
        scored = []
        scoreablecategories = self.scorecard.get_scorecard().copy()
        for key, value in scoreablecategories.items():
            if value != None:
                scored.append(key)
        for key in scored:
            scoreablecategories.pop(key, None)

        predicted_scores = {
        }

        for key, value in scoreablecategories.items():
            if key == "1.ones":
                predicted_scores[1] = self.scorecard.score_ones(dice)
            elif key == "2.twos":
                predicted_scores[2] = self.scorecard.score_twos(dice)
            elif key == "3.threes":
                predicted_scores[3] = self.scorecard.score_threes(dice)
            elif key == "4.fours":
                predicted_scores[4] = self.scorecard.score_fours(dice)
            elif key == "5.fives":
                predicted_scores[5] = self.scorecard.score_fives(dice)
            elif key == "6.sixes":
                predicted_scores[6] = self.scorecard.score_sixes(dice)
            elif key == "7.three of a kind":
                predicted_scores[7] = self.scorecard.score_three_of_a_kind(dice)
            elif key == "8.four of a kind":
                predicted_scores[8] = self.scorecard.score_four_of_a_kind(dice)
            elif key == "9.full house":
                predicted_scores[9] = self.scorecard.score_full_house(dice)
            elif key == "10.small straight":
                predicted_scores[10] = self.scorecard.score_small_straight(dice)
            elif key == "11.large straight":
                predicted_scores[11] = self.scorecard.score_large_straight(dice)
            elif key == "12.yahtzee":
                predicted_scores[12] = self.scorecard.score_yahtzee(dice)
            elif key == "13.chance":
                predicted_scores[13] = self.scorecard.score_chance(dice)
            else:
                raise NotImplementedError
            
        # sort the dictionary by value
        
        sorted_scores = self.__merge_sort(list(predicted_scores.items()))
        category = sorted_scores.pop()
        chosen_category = category[0]
        expscore = category[1]
        if expscore == 0 and self.rerolls > 0:
            self.dice.roll()
            self.rerolls -= 1
            return self.__choosecategory(self.dice)


        
        else:
            self.rerolls = 2
            return chosen_category
        

class HardAI(Player):
    def __init__(self):
        super().__init__()
        self.name = "Hard AI"
        self.scorecard = Scorecard()
        self.rerolls = 2
        self.dice = Dice()
        self.states = {

        1: np.array([1,0,0,0,0]), # 1 matching dice
        2: np.array([0,1,0,0,0]), # 2 matching dice
        3: np.array([0,0,1,0,0]), # 3 matching dice
        4: np.array([0,0,0,1,0]), # 4 matching dice
        5: np.array([0,0,0,0,1]), # 5 matching dice


        }
        self.dice_states = {}
        self.TransitionMatrix = np.array([  [120/1296, 0, 0, 0, 0],
                                            [900/1296, 120/216, 0, 0, 0],
                                            [250/1296, 80/216, 25/36, 0, 0],
                                            [25/1296, 15/216, 10/36, 5/6, 0],
                                            [1/1296, 1/216, 1/36, 1/6, 1]])
        self.gamedicestate = None
        self.upperscores = {}
        self.upperscorecard = {
            1: None,
            2: None,
            3: None,
            4: None,
            5: None,
            6: None,
            
        }
        self.target = None

    
    



    def count_dice_values(dice_list):
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

    def find_state(self, dice_count):
        for dice, count in dice_count.items():
            if count != 0:
                self.dice_states[dice] = [count, self.states[count]]
        return self.dice_states
    
    def distance_point_to_line(X0, Y0):
        dist = abs((-1.4163)*X0 - Y0 + 0.3332)/math.sqrt(((-1.4163)**2)+1)
        return dist

    def expectedvalue(self, dicevalue, state, rerollsleft):
        if rerollsleft == 2:
            probability = self.TransitionMatrix.dot(self.TransitionMatrix.dot(state[1]))[2]
        elif rerollsleft == 1:
            probability = self.TransitionMatrix.dot(state[1])[2]
        payoff = ((dicevalue*state[0])/375)+(((dicevalue*state[0])/63)*(35/375))
        return self.distance_point_to_line(payoff, probability)

    def __choosemove(self, dice): # get dice to reroll 
        optmovefoundtoken = False  # flag to indicate whether non-zero expected value move has been found
        gamedicestate = self.find_state(self.count_dice_values(self.dice.get_dice()))
    
        for dice, state in gamedicestate.items():

            self.upperscores[dice] = self.expectedvalue(dice, state, self.rerolls)
        sorted_scores = sorted(list(self.upperscores.items()))

        #check that the category has not been scored yet
        for score in sorted_scores:
            if self.upperscores[score[0]] == None:
                optmovefoundtoken = True
                self.target = score[0]
                return score[0]
            
            else:
                continue
        if not optmovefoundtoken:
            return (-1)
        
    def reroll_stage(self, dice, aicatchoice):
        if aicatchoice == -1:
            self.dice.roll()
            self.rerolls -= 1
        else:
            for die in dice.get_dice():
                if die != aicatchoice:
                    self.dice.reroll([die])
            self.rerolls -= 1

            



    def play(self, dice):
        self.dice.roll()
        self.rerolls = 2
        self.reroll_stage(dice, self.__choosemove(dice))
        self.reroll_stage(dice, self.__choosemove(dice))
        if self.target != None:
            return self.scorecard.score_roll(dice, self.target)
        elif self.target == None:
            if self.scorecard.get_scorecard()["13.chance"] == None:
                self.scorecard.score_roll(dice, 13)
            else:
                for key, value in self.scorecard.get_scorecard().items():
                    if value == None:
                        self.scorecard.score_roll(dice, key)
                        break
                    else:
                        continue

        
            
            #self.scorecard.score_roll(dice, self.__choosecategory(dice))

    class bing():
        pass





        

