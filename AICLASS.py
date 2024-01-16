#AI class 

import Yahtzeegamecode as game

class Ai_player(game.Player):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.name = "AI"

    def calculate_expected_value(self, dice, category):
        target_number = int(category)
        number_of_dice = dice.count(target_number)

        p = 1/6
        q = 1 - p


        probability = (p**number_of_dice)*(q**(5-number_of_dice))
        expected_value = probability * target_number

        return expected_value
    
    def choose_category(self):
        expected_values = [self.calculate_expected_value(self.dice, category) for category in self.categories]
        max_value = max(expected_values)
        max_index = expected_values.index(max_value)
        return self.categories[max_index]
    
    def play(self):
        self.dice.roll([])
        category = self.choose_category()
        self.score = self.score_category(category)
        self.categories.remove(category)
        self.turn += 1
        return self.score                       
    

    