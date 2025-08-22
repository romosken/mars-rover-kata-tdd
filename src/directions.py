from enum import Enum

class Directions(Enum):
    N = {'L':'W', 'R':'E', 'axis': 'y', 'increment': 1}
    E = {'L':'N', 'R':'S', 'axis': 'x', 'increment': 1}
    S = {'L':'E', 'R':'W', 'axis': 'y', 'increment': -1}
    W = {'L':'S', 'R':'N', 'axis': 'x', 'increment': -1}
