from random import randint

categories = ['1', '2', '3', '4', '5', '6']

class dice:
    def __init__(self):
        self.dice = [randint(1,6) for i in range(5)]

    def roll(self, keep):
        self.dice = [randint(1,6) if i not in keep else i for i in range(5)]


    def count(self, num):
        return self.dice.count(num)

    def get_dice(self):
        return self.dice
    


class Ai_player:
    def __init__(self):
        self.dice = dice()
        self.score = 0

    def calculate_expected_value(dice, category):
        target_number = int(category)
        number_of_dice = dice.count(target_number)

        p = 1/6
        q = 1 - p


        probability = (p**number_of_dice)*(q**(5-number_of_dice))
        expected_value = probability * target_number

        return expected_value
    
    def choose_category(self):
        expected_values = [self.calculate_expected_value(self.dice, category) for category in categories]
        max_value = max(expected_values)
        max_index = expected_values.index(max_value)
        return categories[max_index]
    
    


class game:
    def __init__(self):
        self.player = Ai_player()
        self.turn = 0
        self.score = 0

    def play(self):
        while self.turn < 13:
            self.player.dice.roll([])
            print(self.player.dice.get_dice())
            category = self.player.choose_category()
            print(category)
            self.turn += 1

