import random as rnd
from TowerClass import Tower

# Modules for the tower placing problem

def create_rand_tower(desired_width, desired_height):
    """Returns a new random tower with a random uniformly distributed coverage area inside the desired coverage area
    defined by the desired width and desired height of the region of interest

    Arguments:
        desired_width {int} -- Width of the desired coverage footprint
        desired_height {int} -- Height of the desired coverage footprint
    """
    assert isinstance(desired_height,int) and desired_height > 0, "Coverage area height is not a positive int"
    assert isinstance(desired_width,int) and desired_width > 0, "Coverage area width is not a positve int"

    # Width and height must remain within the coverage area
    height = rnd.randint(1, desired_height)
    width = rnd.randint(1, desired_width)
    # Width is the x coord and height is the y coord.
    start_coord = (rnd.randint(0, desired_width - width), rnd.randint(0, desired_height - height))

    return Tower(start_coord, width, height)

def create_max(new_tower, cur_towers):
    """Returns a tower with the maximum possible coverage area after trimming, in accordance with the pre-existing composite
    footprint (current towers). Returns None if a tower with a unique coverage area cannot be created.

    Arguments:
        new_tower {Tower} -- tower to be trimmed
        cur_towers {list} -- list of towers already placed; the pre-existing composite footprint
    """
    assert isinstance(new_tower, Tower), "Input is not a Tower object"
    assert isinstance(cur_towers, list), "Current Towers is not a list"

    sub_towers = [new_tower]
    # Creates new sub_towers and trims according to each currently placed tower
    for cur in cur_towers:
        if cur is not None:
            assert isinstance(cur, Tower), "Element in list of current towers is not a Tower"
            temp = []
            # Trims every tower in the list with one of the currently placed towers
            for sub in sub_towers:
                temp = temp + trim(sub, cur)
            if not temp:
                return None
        sub_towers = temp # Results of the previous trimming become the towers that need to be trimmed

    #return sub_towers
    return find_max(sub_towers)

def trim(new_tower, placed):
    """Returns a list of all possible subtowers whose coverage area does not intersect with the coverage area of
    the already placed tower

    Arguments:
        new_tower {Tower} -- tower whose coverage needs to be trimmed
        placed {Tower} -- tower whose coverage is locked into the region of interest
    """
    assert isinstance(new_tower, Tower), "Tower to be trimmed is not a Tower"
    assert isinstance(placed, Tower), "Already placed tower is not a Tower"

    # Check if the towers intersect
    if new_tower.intersects(placed): # True if intersects
        temp = []
        if new_tower < placed: # Creates a new trimmed tower to the left of the placed tower, if possible
            temp.append(Tower(new_tower.start_coord, placed.start_coord[0]-new_tower.start_coord[0], new_tower.height))
        if new_tower > placed: # Creates a new trimmed tower to the right of the placed tower, if possible
            new_coord = (placed.right, new_tower.start_coord[1])
            temp.append(Tower(new_coord, new_tower.right-placed.right, new_tower.height))
        if new_tower <= placed: # Creates a new trimmed tower below the placed tower, if possible
            temp.append(Tower(new_tower.start_coord, new_tower.width, placed.start_coord[1]-new_tower.start_coord[1]))
        if new_tower >= placed: # Creates a new trimmed tower above the placed tower, if possible
            new_coord = (new_tower.start_coord[0], placed.top)
            temp.append(Tower(new_coord, new_tower.width, new_tower.top-placed.top))
        return temp
    else: # If the tower doesn't intersect the placed tower, there are no trimmed subtowers and returns the original tower
        return [new_tower]

def find_max(towers):
    """Returns the tower with the maximum coverage area from the list of towers supplied

    Arguments:
        towers {Tower} -- list of towers to inspect
    """
    assert isinstance(towers, list), "Not given a list of towers"
    assert len(towers) > 0, "List of towers is empty"
    max_area = 0
    max_tow = None
    for tow in towers:
        assert isinstance(tow, Tower), "Element in list is not a Tower"
        if tow.area > max_area:
            max_area = tow.area
            max_tow = tow
    return max_tow