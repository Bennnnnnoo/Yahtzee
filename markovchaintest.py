# ai player for yahtzee
import random, numpy as np

dice = [1, 1, 3, 4, 5]

# count how many of each dice there are

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
    
    state =  max(dice_count.values())
    return states[state]

   

        
        
       # 
states = {
    1: [1,0,0,0,0], # 1 matching dice
    2: [0,1,0,0,0], # 2 matching dice
    3: [0,0,1,0,0], # 3 matching dice
    4: [0,0,0,1,0], # 4 matching dice
    5: [0,0,0,0,1], # 5 matching dice
    
}
  
probabilities_graph = [
    [120/1296, 900/1296, 250/1296, 25/1296, 1/1296], # 1 matching dice
    [None, 120/216, 80/216, 15/216, 1/216], # 2 matching dice
    [None, None, 25/36, 10/36, 1/36], # 3 matching dice
    [None, None, None, 5/6, 1/6],   # 4 matching dice
    [None, None, None, None, 1]    # 5 matching dice
]


def reroll(dice, keep):
    for i in range(5):
        if i not in keep:
            dice[i] = random.randint(1, 6)
    return dice

expected_values = [calculate_probability(dice, state) for state in states.values()]

def calculate_probability(dice, state):
    probabilities = np.multiply(state, probabilities_graph)

    S1 = probabilities[0] # probability of getting to state 1
    S2 = probabilities[1] # probability of getting to state 2
    S3 = probabilities[2] # probability of getting to state 3
    S4 = probabilities[3] # probability of getting to state 4
    S5 = probabilities[4] # probability of getting to state 5
     

    return




print(count_dice_values(dice))

    