# This is where we should go back to reeborg and figure out how to stop him going
# in squares.

def turn_right():
    turn_left()
    turn_left()
    turn_left()
    move()


while not at_goal():
    if right_is_clear() and wall_in_front():
        turn_right()
    elif front_is_clear() and not wall_on_right():
        turn_right()
    elif front_is_clear() and wall_on_right():
        move()
    elif wall_in_front():
        turn_left()



