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

    # all __iter__() does is return itself
    def __iter__(self):
        return self

    # __next__() in charge of returning next item in a sequence
    # in this case, when we call __next__() we return a random number
    def  __next__(self):
        if self.count < self.rolls:
            self.count += 1
            return random.randint(1, 6)
        else:
            raise StopIteration

# FOR LOOP METHOD:
'''
dice = Dice(3)
for die in dice:
    print(die)
'''

# LIST COMPREHENSION METHOD:
dice = [die for die in Dice(4)]
print(dice)


'''
# When running the program this is happening behind the scenes:
dice  = Dice(3)
# iter(dice) same as dice.__iter__()
iterator = iter(dice)

while True:
    try:
        # next(iterator) same as iterator.__next__()
        roll = next(iterator)
        print(roll)
    except StopIteration:
        break
'''