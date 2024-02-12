## Yahtzee game code ##

import random, math, PySimpleGUI as sg, re, numpy as np



class Player:           # Player class
    def __init__(self):
        
        self.name = None
        self.scorecard = Scorecard() # players have a scorecard object

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
    
    def get_upper_score(self):
        return sum([self.scorecard[key] for key, value in self.scorecard.items() if (key in ["1.ones", "2.twos", "3.threes", "4.fours", "5.fives", "6.sixes"] and value != None)])
    
    # turns scorecard to list of tuples
    def genlist(self):
        dictlist = []
        for key, value in self.scorecard.items():
            dictlist.append([key,value])
        return dictlist
    
    def bonus_calc(self):
        if self.get_upper_score() >= 63:
            return '35'
        else:
            return f'0, ({self.get_upper_score() - 63})'
            

        
########################
# COMPLEX USE OF OOP #
########################
        
class EZBoard(Scorecard): # player assistance board
    def __init__(self, player):
        super().__init__()
        self.scorecard = {    # take out later as not needed?
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
        

    def play(self):
        self.scorecard.score_roll(self.dice, self.__choosecategory(self.dice))

    # merge sort algorithm to sort the dictionary by value
        
    #################################
    # USE OF RECURSION + MERGE SORT #
    #################################
        
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
        
    
    # choose category function
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

        # check if exp score is zero, and if there are rerolls left then reroll all dice
        if expscore == 0 and self.rerolls > 0:
            self.dice.roll()
            self.rerolls -= 1
            return self.__choosecategory(self.dice)


        
        else:
            self.rerolls = 2
            return chosen_category
        
#####################
# COMPLEX USE OF OOP #
#####################
        
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
        self.upperscores = {} # dict for holding scores during calculation
        self.upperscorecard = { # copy of scorecard for finding available categories
            1: None,
            2: None,
            3: None,
            4: None,
            5: None,
            6: None,
            

        }
        self.lowerscores = {}
        self.lowerscorecard = {
            7: None, # 3OAK
            8: None, # 4OAK
            9: None, # Full House
            10: None, # Small Straight
            11: None, # Large Straight
            12: None, # Yahtzee
            13: None # Chance
        }
        self.target = None # target category variable

    
    



    def count_dice_values(self, dice_list):
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
    
    # find the most common dice value
    def __findmaxdice(self):
        return sorted(list(self.count_dice_values(self.dice.get_dice()).items()), key=lambda x: x[1]).pop()

    # find the state of the dice
    def find_state(self, dice_count):
        for dice, count in dice_count.items():
            if count != 0:
                self.dice_states[dice] = [count, self.states[count]]
        return self.dice_states
    
    # distance of a point to Yahtzee line of best fit
    def distance_point_to_line(self, X0, Y0):
        dist = abs((-1.4163)*X0 - Y0 + 0.3332)/math.sqrt(((-1.4163)**2)+1)
        return dist

    ###########################################################
    # USE OF MATRIX ALGEBRA + COMPLEX USER DEFINED ALGORITHMS #
    ###########################################################

    # calculate expected value of a category (upper section)
    def expectedvalue(self, dicevalue, state, rerollsleft):
        if rerollsleft == 2:
            probability = self.TransitionMatrix.dot(self.TransitionMatrix.dot(state[1]))[2]

        elif rerollsleft == 1:
            probability = self.TransitionMatrix.dot(state[1])[2]
    
        payoff = ((dicevalue*3)/375)+(((dicevalue*3)/63)*(35/375))

        return self.distance_point_to_line(payoff, probability)
    
    # calculate expected value of a category (lower section)
    def threeOAKexpectedvalue(self, dicevalue, state, rerollsleft):
        if rerollsleft == 2:
            probability = self.TransitionMatrix.dot(self.TransitionMatrix.dot(state[1]))[2]
        elif rerollsleft == 1:
            probability = self.TransitionMatrix.dot(state[1])[2]
        payoff = ((dicevalue*3)/375)
        return self.distance_point_to_line(payoff, probability)
    
    def fourOAKexpectedvalue(self, dicevalue, state, rerollsleft):
        if rerollsleft == 2:
            probability = self.TransitionMatrix.dot(self.TransitionMatrix.dot(state[1]))[3]
        elif rerollsleft == 1:
            probability = self.TransitionMatrix.dot(state[1])[3]
        payoff = ((dicevalue*4)/375)
        return self.distance_point_to_line(payoff, probability)
    
    def YahtzeeExpectedvalue(self, state, rerollsleft):
        if rerollsleft == 2:
            probability = self.TransitionMatrix.dot(self.TransitionMatrix.dot(state[1]))[4]
        elif rerollsleft == 1:
            probability = self.TransitionMatrix.dot(state[1])[4]
        payoff = (50/375)
        return self.distance_point_to_line(payoff, probability)
    
    # find the indices of a given value in a list - used for rerolling
    def __find_instances(self, dice, value):
        indices = []
        index = -1
        
        while True:
            try:
                index = dice.index(value, index+1)
                indices.append(index)
            except ValueError:
                break
        
        return indices

    ###################################
    # COMPLEX USER DEFINED ALGORITHMS #
    ###################################

    def __choosemove(self): # get dice to reroll 
        self.upperscores.clear()
        if self.scorecard.score_full_house(self.dice) != 0 and self.lowerscorecard[9] == None:
            self.target = 9
            return 9
        
        elif self.scorecard.score_large_straight(self.dice) != 0 and self.lowerscorecard[11] == None:
            self.target = 11
            return 11
        
        elif self.scorecard.score_small_straight(self.dice) != 0 and self.lowerscorecard[10] == None:
            self.target = 10
            return 10
        
        
        
        optmovefoundtoken = False  # flag to indicate whether non-zero expected value move has been found
        gamedicestate = self.find_state(self.count_dice_values(self.dice.get_dice()))
        
        # clalculate expectedvalues for top section
        for dicekey, state in gamedicestate.items():

            self.upperscores[dicekey] = self.expectedvalue(dicekey, state, self.rerolls)
        
        # calculate expected values in lower section
        for category in self.lowerscorecard:
            highnumdice = self.__findmaxdice()
            if self.lowerscorecard[category] == None:
                if category == 7:
                    self.lowerscores[category] = self.threeOAKexpectedvalue(highnumdice[0], gamedicestate[highnumdice[0]], self.rerolls)
                elif category == 8:
                    self.lowerscores[category] = self.fourOAKexpectedvalue(highnumdice[0], gamedicestate[highnumdice[0]], self.rerolls)
                elif category == 12:
                    self.lowerscores[category] = self.YahtzeeExpectedvalue(gamedicestate[highnumdice[0]], self.rerolls)
                else:
                    continue

        mergedscores = {**self.upperscores, **self.lowerscores}
        mergedscorecard = {**self.upperscorecard, **self.lowerscorecard}
        sorted_scores = sorted(list(mergedscores.items()), key=lambda x: x[1], reverse=True)
        #check that the category has not been scored yet
        for score in sorted_scores:
            if mergedscorecard[score[0]] == None: 
                optmovefoundtoken = True # category found that is unscored
                self.target = score[0] # category number
                return score[0] # exp value
            
            else:
                continue
        if not optmovefoundtoken:
            return (-1) # if all scoreable categories with current roll have been scored
        
    def reroll_stage(self, dice, aicatchoice):
        

        highnumdice = self.__findmaxdice()
        rerolllist = []
        if aicatchoice == -1: # reroll all dice
            self.dice.roll()
            self.rerolls -= 1
        else:
            if aicatchoice in range(1, 7):
            # reroll all dice that are not the category number dice
                for die in dice:
                        if die != aicatchoice:
                            for index in self.__find_instances(dice, die):
                                if index not in rerolllist:
                                    rerolllist.append(index)
            elif aicatchoice == 9:
                rerolllist.clear()
            
            elif aicatchoice == 10:
                rerolllist.clear()

            elif aicatchoice == 11:
                rerolllist.clear()

            else:
                # reroll all dice that are not the highest number dice
                for die in dice:                        
                    if die != highnumdice[0]:
                        for index in self.__find_instances(dice, die):
                            if index not in rerolllist:
                                rerolllist.append(index)

            rerolllist = [num+1 for num in rerolllist]
                    
            self.dice.reroll(rerolllist)
            self.rerolls -= 1
        self.dice_states.clear()
        
        

    def play(self):
        self.dice.roll()
        self.rerolls = 2
        self.reroll_stage(self.dice.get_dice(), self.__choosemove())
        self.reroll_stage(self.dice.get_dice(), self.__choosemove())
        if self.target != None:
            if self.target in range(1, 7):
                self.upperscorecard[self.target] = 'scored' # mark category as scored
                self.scorecard.score_roll(self.dice, self.target) # score the roll

            else:
                if self.target == 7: # 3OAK

                    if self.scorecard.score_three_of_a_kind(self.dice) != 0: 
                        # if the roll is a 3OAK
                        self.lowerscorecard[self.target] = 'scored'
                        self.scorecard.score_roll(self.dice, self.target)

                    elif self.upperscorecard[self.__findmaxdice()[0]] == None: 
                            # if the highest number dice has not been scored
                            self.upperscorecard[self.__findmaxdice()[0]] = 'scored'
                            self.scorecard.score_roll(self.dice, self.__findmaxdice()[0])
                    else:
                        # if all else fails, score the first available category
                        for key, value in {**self.upperscorecard, **self.lowerscorecard}.items(): 
                            if value == None:
                                self.scorecard.score_roll(self.dice, key)
                                if key in range(1, 7):
                                    self.upperscorecard[key] = 'scored'
                                else:
                                    self.lowerscorecard[key] = 'scored'
                                break
                            else:
                                continue

                elif self.target == 8:
                    if self.scorecard.score_four_of_a_kind(self.dice) != 0:
                        # if the roll is a 4OAK
                        self.lowerscorecard[self.target] = 'scored'
                        self.scorecard.score_roll(self.dice, self.target)
                    else:
                        if self.lowerscorecard[7] == None and self.scorecard.score_three_of_a_kind(self.dice) != 0:
                            # if the roll is a 3OAK
                            self.lowerscorecard[7] = 'scored'
                            self.scorecard.score_roll(self.dice, 7)
                        elif self.upperscorecard[self.__findmaxdice()[0]] == None:
                            # if the highest number dice has not been scored
                            self.upperscorecard[self.__findmaxdice()[0]] = 'scored'
                            self.scorecard.score_roll(self.dice, self.__findmaxdice()[0])
                        else:
                            # if all else fails, score the first available category
                            for key, value in {**self.upperscorecard, **self.lowerscorecard}.items():
                                if value == None:
                                    self.scorecard.score_roll(self.dice, key)
                                    if key in range(1, 7):
                                        self.upperscorecard[key] = 'scored'
                                    else:
                                        self.lowerscorecard[key] = 'scored'
                                    break

                                    
                                else:
                                    continue
                
                elif self.target == 9:
                    self.scorecard.score_roll(self.dice, 9)
                    self.lowerscorecard[9] = 'scored'

                elif self.target == 10:
                    self.scorecard.score_roll(self.dice, 10)
                    self.lowerscorecard[10] = 'scored'

                elif self.target == 11:
                    self.scorecard.score_roll(self.dice, 11)
                    self.lowerscorecard[11] = 'scored'

                elif self.target == 12:
                    if self.scorecard.score_yahtzee(self.dice) != 0:
                        # if the roll is a Yahtzee
                        self.lowerscorecard[self.target] = 'scored'
                        self.scorecard.score_roll(self.dice, self.target)
                    else:
                        if self.lowerscorecard[8] == None and self.scorecard.score_four_of_a_kind(self.dice) != 0:
                            # if the roll is a 4OAK
                            self.lowerscorecard[8] = 'scored'
                            self.scorecard.score_roll(self.dice, 8)
                        elif self.lowerscorecard[7] == None and self.scorecard.score_three_of_a_kind(self.dice) != 0:
                            # if the roll is a 3OAK
                            self.lowerscorecard[7] = 'scored'
                            self.scorecard.score_roll(self.dice, 7)
                        elif self.upperscorecard[self.__findmaxdice()[0]] == None:
                            # if the highest number dice has not been scored
                            self.upperscorecard[self.__findmaxdice()[0]] = 'scored'
                            self.scorecard.score_roll(self.dice, self.__findmaxdice()[0])
                        else:
                            # if all else fails, score the first available category
                            mergedlist = {**self.upperscorecard, **self.lowerscorecard}
                            for key, value in mergedlist.items():
                                if value == None:
                                    self.scorecard.score_roll(self.dice, key)
                                    if key in range(1, 7):
                                        self.upperscorecard[key] = 'scored'
                                    else:
                                        self.lowerscorecard[key] = 'scored'
                                    break

                                    
                                else:
                                    continue
                
                
        # score chance or first available category if no target        
        elif self.target == None:
            if self.lowerscorecard[13] == None:
                self.scorecard.score_roll(self.dice, 13)
                self.lowerscorecard[13] = 'scored'
            else:
                for key, value in {**self.upperscorecard, **self.lowerscorecard}.items():
                    if value == None:
                        self.scorecard.score_roll(self.dice, key)
                        break
                    else:
                        continue

        self.dice_states.clear()
        self.target = None

        
            
           





        

