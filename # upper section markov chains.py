# upper section markov chains

import numpy as np
from Yahtzeegamecode import Scorecard

game_dice = [3, 5, 5, 5, 6]
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


TransitionMatrix = np.array([[120/1296, 0, 0, 0, 0],
                             [900/1296, 120/216, 0, 0, 0],
                             [250/1296, 80/216, 25/36, 0, 0],
                             [25/1296, 15/216, 10/36, 5/6, 0],
                             [1/1296, 1/216, 1/36, 1/6, 1]])
    

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
        self.value = self.probability * (((self.dicevalue*self.state)/375)+(((self.dicevalue*self.state)/63)*(35/375)))
        return self.value


    


# make game graph for each dice roll
        
def make_dice_graph(currentstate, category):
    dgraph = DiceGraph(currentstate, category)
    dgraph.populate_graph()
    return dgraph
    


    


gamedicestate = find_state(count_dice_values(game_dice))
graphlist = []

for dice, state in gamedicestate.items():
    graphlist.append(make_dice_graph(state[0], dice))

for graph in graphlist:
    for node in graph.root.children:
        node.calculate_probability()
        node.calculate_value()
        print(node.state, node.dicevalue, node.probability, node.value)



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
            



