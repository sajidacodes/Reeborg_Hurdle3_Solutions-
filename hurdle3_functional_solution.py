# Hurdle 3 - Functional Solution
# Uses functions (jump, think) for cleaner and organized code.
# Reeborg moves or jumps until he reaches the goal.

def turn_right():
    turn_left()
    turn_left()
    turn_left()
def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
def think():
    if front_is_clear():
        move()
    else:
        jump()
while not at_goal():
    think()