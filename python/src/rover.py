from .grid import Grid
from .directions import Directions

class Rover():

    def __init__(self):
        self.direction = Directions.N
        self.coordinate = {'x': 0, 'y': 0}
        self.command_method_mapping = {
            'R': self.turn_right,
            'L': self.turn_left,
            'M': self.move
        }

    def execute(self, commands):
        for command in commands:
           self.command_method_mapping[command]()
        
        return f"{self.coordinate['x']}:{self.coordinate['y']}:{self.direction.name}"

    def turn_right(self):
        self.turn('R')

    def turn_left(self):
        self.turn('L')

    def turn(self, side):
        next_direction_value = self.direction.value[side]
        self.direction = Directions[next_direction_value]

    def move(self):
        increment = self.direction.value['increment']
        axis = self.direction.value['axis']
        self.coordinate[axis] = self.next_position(self.coordinate[axis], increment)

    def next_position(self, current, increment):
        
        new_position = current + increment

        if new_position > Grid.MAX.value:
            return Grid.MIN.value
        
        if new_position < Grid.MIN.value:
            return Grid.MAX.value
        
        return new_position