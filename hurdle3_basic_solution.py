# Hurdle 3 - Basic Solution
# Reeborg moves forward if the path is clear.
# If blocked, he jumps over the wall using simple steps.


def turn_right():
    turn_left()
    turn_left()
    turn_left()
while not at_goal():
    if front_is_clear():
       move()
    else:
      turn_left()
      move()
      turn_right()
      move()
      turn_right()
      move()
      turn_left()