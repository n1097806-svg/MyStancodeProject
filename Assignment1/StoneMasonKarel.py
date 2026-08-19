"""
File: StoneMasonKarel.py
Name: Jessie
--------------------------------
At the start, this program does nothing.

Your task is to add the necessary code to guide Karel
to build stone columns that are five beepers tall
on each appropriate avenue, as described in Assignment 1.

Karel should finish on the last avenue at 1st Street, facing east.
"""

from karel.stanfordkarel import *


def main():
    """
    Pre-condition: Karel is facing east,at (1,1)
    Post-condition: Karel is facing north,at (13,5)
    """
    while front_is_clear():
        fix_pillar()
        go_down()
        next_pillar()
    fix_pillar()


def fix_pillar():
    """
    Pre-condition: Karel is on the bottom of the pillar, facing east
    Post-condition: Karel back to the bottom of the pillar, facing south
    """
    turn_left()
    for i in range(4):
        if on_beeper():
            move()
        else:
            put_beeper()
            move()
    if not on_beeper():
        put_beeper()


def next_pillar():
    """
    Pre-condition: Karel is on the bottom of the pillar, facing south
    Post-condition: Karel on the bottom of the next pillar, facing east
    """
    turn_left()
    for i in range(4):
        move()


def turn_around():
    """
    Karel will turn left twice.
    """
    turn_left()
    turn_left()


def go_down():
    """
    Karel was facing north, and will go back to street 1.
    """
    turn_around()
    for i in range(4):
        move()


def turn_right():
    """
    Karel will turn left 3 times.
    """
    turn_left()
    turn_left()
    turn_left()

# DO NOT EDIT CODE BELOW THIS LINE #
if __name__ == '__main__':
    execute_karel_task(main)
