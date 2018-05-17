import random as rnd
from TowerClass import Tower

def create_rand_tower(desired_height, desired_width):
    """Returns a new random tower with coordinates within the desired coverage area

    Arguments:
        desired_height {int} -- Height of the desired coverage footprint
        desired_width {int} -- Width of the desired coverage footprint
    """
    assert isinstance(desired_height,int), "Coverage area height is not an int"
    assert isinstance(desired_width,int), "Coverage area width is not an int"

    # Width is the x coord and height is the y coord. Cannot be the top right corner.
    start_coord = (rnd.randint(0, desired_width-1), rnd.randint(0, desired_height-1))
    # Width and height must remain within the coverage area
    height = rnd.randint(1, desired_height-start_coord[1])
    width = rnd.randint(1, desired_width-start_coord[0])
    return Tower(start_coord, height, width)

def create_max(new_tower, cur_towers):
    """Returns a tower with the maximum remaining coverage area of a trimmed tower. Returns None if tower
    with unique coverage cannot be created.

    Arguments:
        new_tower {Tower} -- tower to be trimmed
        cur_towers {list} -- list of towers currently placed within the coverage area
    """
    assert isinstance(new_tower, Tower), "Input is not a Tower object"
    assert isinstance(cur_towers, list), "Current Towers is not a list"

    sub_towers = [new_tower]
    # Creates new sub_towers and trims according to each currently placed tower
    for cur in cur_towers:
        assert isinstance(cur, Tower), "Element in list of current towers is not a Tower"
        temp = []
        for sub in sub_towers:
            temp = temp + trim(sub, cur)
            print temp
        if not temp:
            return None
        print "____________________________________________"
        sub_towers = temp

    #return sub_towers
    return find_max(sub_towers)

def trim(new_tower, placed):
    """Returns a list of all possible trimmings of the new tower's coverage in accordance to the placed tower's coverage

    Arguments:
        new_tower {Tower} -- tower coverage to be trimmed
        placed {Tower} -- tower coverage that will perform the trimming
    """
    assert isinstance(new_tower, Tower), "Tower to be trimmed is not a Tower"
    assert isinstance(placed, Tower), "Already placed tower is not a Tower"

    # check if the towers intersect
    if new_tower == placed: # true if intersects
        temp = []
        if new_tower < placed: # x-axis
            temp.append(Tower(new_tower.start_coord, new_tower.height, placed.start_coord[0]-new_tower.start_coord[0]))
        if new_tower > placed: # x-axis
            new_coord = (placed.right, new_tower.start_coord[1])
            temp.append(Tower(new_coord, new_tower.height, new_tower.right-placed.right))
        if new_tower <= placed: # y-axis
            temp.append(Tower(new_tower.start_coord, placed.start_coord[1]-new_tower.start_coord[1], new_tower.width))
        if new_tower >= placed:# y-axis
            new_coord = (new_tower.start_coord[0], placed.top)
            temp.append(Tower(new_coord, new_tower.top-placed.top, new_tower.width))
        return temp
    else:
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