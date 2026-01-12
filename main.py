# Iterator = An object that returns elements one at a time from a sequence (or data stream)
#            and remembers its position between calls.
#            A Python object is an iterator if it has:
#            __iter__() → Returns the iterator object itself
#            __next__() → Returns the next item in the sequence
#                         (raises StopIteration when no more items)
import random


class Dice:
    def __init__(self, rolls):
        self.rolls = rolls
        self.count = 0

    def __iter__(self):
        return self

    # in charge of returning the next item in a sequence
    def __next__(self):
        if self.count < self.rolls:
            self.count += 1

            # when the method is called,
            # return a random number between 1 - 6
            return random.randint(1,6)
        else:
            raise StopIteration

# Higher level operations are being translated in the python interpreter
# into lower level operations

# FOR LOOP METHOD:
'''
dice = Dice(3)

for die in dice:
    print(die)
'''

# LIST COMPREHENSION METHOD:
'''
# return each die for every die in Dice
dice = [die for die in Dice(4)]
print(dice)
'''




# When running the program this is happening behind the scenes,
# DOES NOT NEED TO BE WRITTEN THIS WAY:
'''
dice = Dice(3)

iterator = iter(dice)

while True:
    try:
        roll = next(iterator)
        print(roll)
    except StopIteration:
        break
'''