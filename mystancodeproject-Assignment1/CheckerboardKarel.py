"""
File: CheckerboardKarel.py
Name: Jessie
----------------------------
When finished, this program should
draw a checkerboard pattern using
beepers, as described in Assignment 1.

The solution should work correctly
for all of the sample worlds provided
in the starter folder.
"""

from karel.stanfordkarel import *


def main():
    """
    Pre-condition: Karel is facing east,at (1,1)
    Post-condition:Even
                   Odd Karel is facing east, at
    """

    while left_is_clear():
        checkerboard_row()
        up1()
        checkerboard_row()
        if right_is_clear():
            up2()
        else:
            turn_around()
    turn_right()
    move()
    if not on_beeper():
        turn_around()
        move()
        turn_right()
        checkerboard_row()

def checkerboard_row():
    while front_is_clear():
        put_beeper()
        move()
        if front_is_clear():
            move()
    obob()


def obob():
    turn_around()
    move()
    if on_beeper():
        turn_around()
        move()
    else:
        turn_around()
        move()
        put_beeper()


def up1():
    if not on_beeper():
        turn_left()
        move()
        turn_left()
    else:
        turn_left()
        move()
        turn_left()
        move()


def up2():
    turn_right()
    move()
    turn_right()


def turn_around():
    turn_left()
    turn_left()

def turn_right():
    turn_left()
    turn_left()
    turn_left()


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    execute_karel_task(main)
