from src.rover import Rover

import pytest


@pytest.mark.parametrize("command, expected", [
    ("R", "0:0:E"),
    ("RR", "0:0:S"),
    ("RRR", "0:0:W"),
    ("RRRR", "0:0:N"),
    ("L", "0:0:W"),
    ("LL", "0:0:S"),
    ("LLL", "0:0:E"),
    ("LLLL", "0:0:N"),

])
def test_rover_turn(command, expected):
    rover = Rover()
    result = rover.execute(command)
    assert result == expected


@pytest.mark.parametrize("command, expected", [
    ("M", "0:1:N"),
    ("MMMMMMMMMM", "0:0:N"),
])
def test_rover_move(command, expected):
    rover = Rover()
    result = rover.execute(command)
    assert result == expected

@pytest.mark.parametrize("command, expected", [
    ("RM", "1:0:E"),
    ("RMMMMMMMMMM", "0:0:E"),
    ("LM", "9:0:W"),
    ("LMMMMMMMMMM", "0:0:W"),
    ("RRM", "0:9:S"),
    ("RRMMMMMMMMMM", "0:0:S"),
    ('MMRMMLM', '2:3:N')
])
def test_rover_turn_move(command, expected):
    rover = Rover()
    result = rover.execute(command)
    assert result == expected