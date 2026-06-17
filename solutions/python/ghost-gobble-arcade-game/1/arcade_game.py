"""Functions for implementing the rules of the classic arcade game Pac-Man."""


def eat_ghost(power_pellet_active, touching_ghost):
    if power_pellet_active == True:
        if touching_ghost == True:
            return True
        elif not touching_ghost:
            return False
    else:
        return False


def score(touching_power_pellet, touching_dot):
   if touching_power_pellet or touching_dot == True:
       return True
   else:
       return False


def lose(power_pellet_active, touching_ghost):
   if power_pellet_active == False and touching_ghost == True:
       return True
   else: 
       return False


def win(has_eaten_all_dots, power_pellet_active, touching_ghost):
    if has_eaten_all_dots == True:
        if touching_ghost and not power_pellet_active:
            return False
        return True
    return False