import random

class Dice:

    def __init__(self, dice_count):
        self.dice_count = dice_count
    

    def roll_dice(self):

        dice_value = 0
        for i in range(self.dice_count):
            dice_num = random.randint(1,6)
            dice_value += dice_num
        
        return dice_value