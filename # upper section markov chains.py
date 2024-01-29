# upper section markov chains

import numpy as np, math
from Yahtzeegamecode import Scorecard

game_dice = [1, 3, 2, 6, 6]
states = {
    
    1: np.array([1,0,0,0,0]), # 1 matching dice
    2: np.array([0,1,0,0,0]), # 2 matching dice
    3: np.array([0,0,1,0,0]), # 3 matching dice
    4: np.array([0,0,0,1,0]), # 4 matching dice
    5: np.array([0,0,0,0,1]), # 5 matching dice

    
}

dice_states = {
    
}

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

def find_state(dice_count):
    for dice, count in dice_count.items():
        if count != 0:
            dice_states[dice] = [count, states[count]]
    return dice_states

def categorize_small_straight(roll):
    # Step 1: Sort the roll
    sorted_roll = sorted(roll)
    
    # Step 2: Determine distinct consecutive numbers
    consecutive_count = 1
    distinct_consecutive_count = 1
    for i in range(1, len(sorted_roll)):
        if sorted_roll[i] == sorted_roll[i - 1] + 1:
            consecutive_count += 1
            distinct_consecutive_count = max(distinct_consecutive_count, consecutive_count)
        elif sorted_roll[i] != sorted_roll[i - 1]:
            consecutive_count = 1
    
    # Step 3: Categorize based on distinct consecutive count
    if distinct_consecutive_count >= 2:
        return "2 dice in a small straight"
    elif distinct_consecutive_count == 1 and 6 in sorted_roll and 2 in sorted_roll:
        return "2 dice in a small straight"
    elif distinct_consecutive_count == 1 and (1 in sorted_roll and 3 in sorted_roll and 4 in sorted_roll) or (3 in sorted_roll and 4 in sorted_roll and 5 in sorted_roll):
        return "3 dice in a small straight"
    elif distinct_consecutive_count == 1 and (1 in sorted_roll and 2 in sorted_roll and 3 in sorted_roll and 4 in sorted_roll) or (2 in sorted_roll and 3 in sorted_roll and 4 in sorted_roll and 5 in sorted_roll) or (3 in sorted_roll and 4 in sorted_roll and 5 in sorted_roll and 6 in sorted_roll):
        return "Complete small straight"
    else:
        return "1 dice in a small straight"


TransitionMatrix = np.array([[120/1296, 0, 0, 0, 0],
                             [900/1296, 120/216, 0, 0, 0],
                             [250/1296, 80/216, 25/36, 0, 0],
                             [25/1296, 15/216, 10/36, 5/6, 0],
                             [1/1296, 1/216, 1/36, 1/6, 1]])

StraightTransitionMatrix = np.array([[108/1296, 0, 0, 0],
                                     [525/1296, 64/216, 0, 0],
                                     [582/1296, 122/216, 25/36, 0],
                                     [108/1296, 30/216, 11/36, 1]])

  
'''

class DiceGraph():
    def __init__(self, state, dicevalue):
        self.root = Node(state, dicevalue)
        self.graph = None
        self.expected_value = None


    def populate_graph(self):
        for state in states.keys():
            self.root.add_child(Node(state, self.root.get_dice_value(), self.root))
        
    




class Node():
    def __init__(self, state, dicevalue, parent = None): # use 1-5 instead of state vector
        self.value = 0 # node value
        self.parent = parent
        self.children = []
        self.probability = 0
        self.expected_value = 0
        self.state = state # number of target state 1-5
        self.dicevalue = dicevalue

    def add_child(self, child):
        self.children.append(child)

    def set_probability(self, probability):
        self.probability = probability

    def calculate_expected_value(self):
        self.expected_value = self.probability * self.reward

    def set_reward(self, reward):
        self.reward = reward

    def get_state(self):
        return self.state
    
    def get_state_matrix(self):
        return states[self.state]
    
    def calculate_probability(self):
        problist = list(TransitionMatrix.dot(TransitionMatrix.dot(self.parent.get_state_matrix())))
        return self.set_probability(problist[self.state-1])

    def get_dice_value(self):
        return self.dicevalue
    
 #   def calculate_reward(self):

    
    def calculate_value(self):
        self.value = self.distance_point_to_line((((self.dicevalue*self.state)/375)+(((self.dicevalue*self.state)/63)*(35/375))), self.probability)
        return self.value
    
    def distance_point_to_line(self, X0, Y0):
        dist = abs((-1.4163)*X0 - Y0 + 0.3332)/math.sqrt(((-1.4163)**2)+1)
        return dist
    
'''


    


# make game graph for each dice roll
        
def make_dice_graph(currentstate, category):
    dgraph = DiceGraph(currentstate, category)
    dgraph.populate_graph()
    return dgraph
    


    


gamedicestate = find_state(count_dice_values(game_dice))
graphlist = []
'''
for dice, state in gamedicestate.items():
    graphlist.append(make_dice_graph(state[0], dice))

for graph in graphlist:
    for node in graph.root.children:
        node.calculate_probability()
        node.calculate_value()
        #print(node.state, node.dicevalue, node.probability, node.value)
'''
basescorecard = {
    
}

def distance_point_to_line(X0, Y0):
        dist = abs((-1.4163)*X0 - Y0 + 0.3332)/math.sqrt(((-1.4163)**2)+1)
        return dist

def expectedvalue(dicevalue, state):
    probability = TransitionMatrix.dot(TransitionMatrix.dot(state[1]))[2]
    payoff = ((dicevalue*state[0])/375)+(((dicevalue*state[0])/63)*(35/375))
    return distance_point_to_line(payoff, probability)

def fourofakindexpectedvalues(dicevalue, state):
    probability = TransitionMatrix.dot(TransitionMatrix.dot(state[1]))[3]
    payoff = ((dicevalue*state[0])/375)+(((dicevalue*state[0])/63)*(35/375))
    return distance_point_to_line(payoff, probability)

def Yahtzeeexpectedvalues(dicevalue, state):
    probability = TransitionMatrix.dot(TransitionMatrix.dot(state[1]))[4]
    payoff = ((dicevalue*state[0])/375)+(((dicevalue*state[0])/63)*(35/375))
    return distance_point_to_line(payoff, probability)






    





for dice, state in gamedicestate.items():

        basescorecard[dice] = expectedvalue(dice, state)

print(basescorecard)

'''scorecard = Scorecard()

dicenums = count_dice_values(game_dice)

def calculate_payoff(dice, dicenum):
    return ((dice*dicenum)/375)+(((dice*dicenum)/63)*(35/375))

for key in scorecard.scorecard.keys():
    if key == '1.ones':
        onesprobabilitiesdict = {
            1: [],
            2: [],
            3: [],
            4: [],
            5: []
           
        }
        for key, value in onesprobabilitiesdict.items():
            if dicenums[1] >= key:
                onesprobabilitiesdict[key].append(1)
            else:
                onesprobabilitiesdict[key].append((1/6)**(key-dicenums[1]))
    

print(onesprobabilitiesdict)'''
            

#print(categorize_small_straight(game_dice))


