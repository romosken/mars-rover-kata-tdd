from enum import Enum

class Directions(Enum):
    N = {'L':'W', 'R':'E', 'increment': 1}
    E = {'L':'N', 'R':'S'}
    S = {'L':'E', 'R':'W'}
    W = {'L':'S', 'R':'N'}
