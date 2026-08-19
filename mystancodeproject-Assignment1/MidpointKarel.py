"""
File: MidpointKarel.py
Name: Jessie
----------------------------
When finished, this program should leave a beeper
on the corner closest to the midpoint of 1st Street.

If 1st Street has an even number of corners,
either of the two central corners is acceptable.
Karel may use additional beepers while searching
for the midpoint, but must remove them before stopping.

The world can be of any size, and you may assume
that it is at least as tall as it is wide.
"""

from karel.stanfordkarel import *

def x1():
    while left_is_clear():
        put_beeper()
        move()
        turn_left()
        move()
        turn_right()


def x2():
    put_beeper()
    turn_right()
    go_down()
    turn_right()
    while right_is_clear():
        put_beeper()
        move()
        turn_right()
        move()
        turn_left()
    put_beeper()
    turn_around()


def x3():
    while front_is_clear():
        pick_beeper()
        if on_beeper():
            turn_right()
            go_down()
        else:
            turn_right()
            move()
            turn_left()
            move()


def x4():
    while left_is_clear():
        pick_beeper()
        move()
        turn_left()
        move()
        turn_right()
    pick_beeper()
    turn_right()
    go_down()
    pick_beeper()


def x5():
    turn_right()
    move()
    turn_right()
    move()
    pick_beeper()
    turn_left()
    move()
    turn_left()
    move()
    turn_left()


def main():
    """
    Pre-condition: Karel is facing east,at (1,1)
    Post-condition: Karel is facing east on beeper, at (1,3)
    """
    x1()
    x2()
    x3()
    put_beeper()
    turn_right()
    move()
    move()
    turn_around()
    x4()
    x5()


def turn_right():
    turn_left()
    turn_left()
    turn_left()


def turn_around():
    turn_left()
    turn_left()


def go_down():
    while front_is_clear():
        move()

# DO NOT EDIT CODE BELOW THIS LINE #


if __name__ == '__main__':
    execute_karel_task(main)