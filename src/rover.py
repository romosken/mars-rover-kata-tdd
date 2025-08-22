from .grid import Grid
from .directions import Directions

class Rover():

    def __init__(self):
        self.direction = 'N'
        self.x = 0
        self.y = 0

    def execute(self, commands):
        for command in commands:
            if command in ('R', 'L'):
                self.change_direction(command)
            if command == 'M':
                self.move()
        
        return f"{self.x}:{self.y}:{self.direction}"

    def change_direction(self, command):
        current_direction_mapping = Directions[self.direction].value
        self.direction = current_direction_mapping[command]

    
    def move(self):
        if self.direction == 'E':
            self.x = self.next_position(self.x, 1)
        elif self.direction == 'W':
            self.x = self.next_position(self.x, -1)
        elif self.direction == 'N':
            self.y = self.next_position(self.y, 1)
        else:
            self.y = self.next_position(self.y, -1)



    def next_position(self, current, increment):
        
        new_position = current + increment
        if new_position > Grid.MAX.value:
            return Grid.MIN.value
        if new_position < Grid.MIN.value:
            return Grid.MAX.value
        return new_position