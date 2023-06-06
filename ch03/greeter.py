# Class with somewhat unrelated methods
from datetime import datetime


class Greeter:
    def __init__(self, name):
        self.name = name

    def _day(self):  # <1>
        return datetime.now().strftime('%A')

    def _part_of_day(self):  # <2>
        current_hour = datetime.now().hour

        if current_hour < 12:
            return 'morning'
        elif 12 <= current_hour < 17:
            return 'afternoon'
        else:
            return 'evening'

    def greet(self, store):  # <3>
        print(f'Hi, my name is {self.name}, and welcome to {store}!')
        print(f'How\'s your {self._day()} {self._part_of_day()} going?')
        print('Here\'s a coupon for 20% off!')

    ...


# Methods extracted as functions outside the class
def day():
    return datetime.now().strftime('%A')


def part_of_day():
    current_hour = datetime.now().hour

    if current_hour < 12:
        return 'morning'
    elif 12 <= current_hour < 17:
        return 'afternoon'
    else:
        return 'evening'


# Referencing extracted functions inside the class
class Greeter:
    ...

    def greet(self, store):
        print(f'Hi, my name is {self.name}, and welcome to {store}!')
        print(f'How\'s your {day()} {part_of_day()} going?')
        print('Here\'s a coupon for 20% off!')
