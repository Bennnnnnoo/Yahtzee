# markov chain test 2
import numpy as np

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
    
    return dice_count

def find_state(dice_count):
    if 5 in dice_count.values():
        return np.array([0,0,0,0,1]) # state 5
        
    elif 4 in dice_count.values():
        return np.array([0,0,0,1,0]) # state 4
    elif 3 in dice_count.values():
        return np.array([0,0,1,0,0]) # state 3
    elif 2 in dice_count.values():
        return np.array([0,1,0,0,0]) # state 2
    elif 1 in dice_count.values():
        return np.array([1,0,0,0,0]) # state 1
    else:
        raise Exception("Invalid dice count")
    



TransitionMatrix = np.array([[120/1296, 0, 0, 0, 0],
                             [900/1296, 120/216, 0, 0, 0],
                             [250/1296, 80/216, 25/36, 0, 0],
                             [25/1296, 15/216, 10/36, 5/6, 0],
                             [1/1296, 1/216, 1/36, 1/6, 1]])
    

def get_probabilities(dice):
    dice_count = count_dice_values(dice)
    state = find_state(dice_count)
    return TransitionMatrix.dot(TransitionMatrix.dot(state)) # TransitionMatrix.dot(TransitionMatrix.dot(state)) is the probability of being in each state after two rolls


print(get_probabilities(dice))

# if in state 1, the probability of remaining in state 1 after rerolling four dice is 120/1296, the probability of transitioning to state 2 is 900/1296, the probability of transitioning to state 3 is 250/1296, the probability of transitioning to state 4 is 25/1296, and the probability of transitioning to state 5 is 1/1296
# etc with the other states

'''def calculate_probability(state):
    dice_count = count_dice_values(dice)
    state = find_state(dice_count)
    return TransitionMatrix[state]

# if you have two rolls remaining, you can calculate the probability of state transition by squaring the transition matrix

def calculate_probability_two_rolls(dice):
    dice_count = count_dice_values(dice)
    state = find_state(dice_count)
    return [a*b for a,b in zip(TransitionMatrix[state], TransitionMatrix[state])]

print (calculate_probability_two_rolls(dice))'''
