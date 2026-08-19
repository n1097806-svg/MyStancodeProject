"""
File: CollectNewspaperKarel.py
Name: Make Karel pick up the news paper and return
--------------------------------

Your will need to guide Karel to walk out of the door of its house,
pick up the newspaper (represented by a beeper),
and then return to its original position
in the upper-left corner of the house,
and put down the beeper.
"""

from karel.stanfordkarel import *


def main():
    """
    pre-condition: Karel is at street 4, avenue 3, facing east.
    post-condition: Karel is at street 4, avenue 3, facing east, with a beeper.
    """
    move()
    turn_right()
    move()
    turn_left()
    move()
    move()
    pick_beeper()
    turn_around()
    move()
    move()
    move()
    turn_right()
    move()
    turn_right()
    put_beeper()


def turn_right():
    turn_left()
    turn_left()
    turn_left()


def turn_around():
    turn_left()
    turn_left()

# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    execute_karel_task(main)
