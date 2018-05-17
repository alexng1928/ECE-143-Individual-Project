import random as rnd
from TowerClass import Tower

def create_rand_tower(desired_height, desired_width):
    """Returns a new random tower within the desired coverage area

    Arguments:
        desired_height {int} -- Height of the desired coverage footprint
        desired_width {int} -- Width of the desired coverage footprint
    """
    # Width is the x coord and height is the y coord. Cannot be the top right corner.
    start_coord = (rnd.randint(0, desired_width-1), rnd.randint(0, desired_height-1))
    # Width and height must remain within the coverage area
    height = rnd.randint(1, desired_height-start_coord[1])
    width = rnd.randint(1, desired_width-start_coord[0])
    return Tower(start_coord, height, width)