import matplotlib.patches as patches
from TowerClass import Tower
from Modules import create_rand_tower, create_max

# Modules specifically for the Jupyter Notebook documentation and visualization

def coverage(desired_width, desired_height, num_towers, replace = True):
    """Returns a specificed number of towers within the region of interest defined by the desired width and
    the desired height. Ends early if the region of interest is completely covered.

    Arguments:
        desired_width {int} -- Width of the desired coverage footprint
        desired_height {int} -- Height of the desired coverage footprint
        num_towers {int} -- Number of towers to be placed inside the region of interest

    Keyword Arguments:
        replace {bool} -- Determines whether a tower will be replaced or not if the tower does not provide
                          unique coverage. Unused in actual project (default: {True})
    """
    assert isinstance(desired_height,int) and desired_height > 0, "Coverage area height is not a positive int"
    assert isinstance(desired_width,int) and desired_width > 0, "Coverage area width is not a positve int"
    assert isinstance(num_towers, int) and num_towers > 0, "Number of towers is not a  positive int"
    assert isinstance(replace, bool), "Not a boolean"

    placed = []
    original = []
    new_tower = create_rand_tower(desired_width, desired_height)
    # Never need to check if the first tower provides unique coverage
    original.append(new_tower)
    placed.append(new_tower)
    if replace:
        count = 1
        while count < num_towers:
            if coverage_area(placed) == desired_height*desired_width:
                break
            new_tower = create_rand_tower(desired_width, desired_height)
            trim_tower = create_max(new_tower, placed)
            # Checks if the tower provides unique coverage to the region of interest
            if trim_tower is not None:
                original.append(new_tower)
                placed.append(trim_tower)
                count += 1

    # Below is unused in actual jupyter notebook writeup
    else:
        for _ in range(1,num_towers):
            new_tower = create_rand_tower(desired_width, desired_height)
            original.append(new_tower)
            trim_tower = create_max(new_tower, placed)
            placed.append(trim_tower)
    return [placed, original]

def string_gaps(desired_width, desired_height, tower_list):
    """Returns a statement about gaps in the total coverage...It's pretty useless

    Arguments:
        desired_width {int} -- Width of the desired coverage footprint
        desired_height {int} -- Height of the desired coverage footprint
        tower_list {list} -- list of towers already placed; the pre-existing composite footprint
    """
    assert isinstance(desired_height,int) and desired_height > 0, "Coverage area height is not a positive int"
    assert isinstance(desired_width,int) and desired_width > 0, "Coverage area width is not a positve int"
    assert isinstance(tower_list, list), "List of towers is not a list"

    if coverage_area(tower_list) != desired_width*desired_height:
        return "There are gaps in the coverage"
    else:
        return "There are no gaps in the coverage"

def coverage_area(tower_list):
    """Returns the amount of area covered by the towers in the list

    Arguments:
        tower_list {list} -- list of towers whose area is added up
    """
    assert isinstance(tower_list, list), "List of towers is not a list"

    total_area = 0
    for i in tower_list:
        if i != None:
            total_area = total_area + i.area
    return total_area

def get_rects(tower_list):
    """Returns a list of rectangle actor representations of towers from the provided list of towers

    Arguments:
        tower_list {list} -- list of towers to be turned into rectangles
    """
    # These colors are RGBA 0-1 normalized. The "colors" list has aplha values of 0.5 to be transparent
    # More colors can be added, but must be added to both lists to maintain color consistency between a ractangle's face and edge
    colors = [(0,0,1,0.5), (0,0.5,0,0.5), (1,0,0,0.5), (0,0.5,0.5,0.5), (0.3,0,0.51,0.5), (1,0.65,0,0.5), (0.80,0.52,0.25,0.5), \
            (0.5,0,0,0.5), (0,0.98,0.6,0.5), (0.5,0.5,0.5,0.5), (1,0.87,0.68,0.5)]
    edges = [(0,0,1,1), (0,0.5,0,1), (1,0,0,1), (0,0.5,0.5,1), (0.3,0,0.51,1), (1,0.65,0,1), (0.80,0.52,0.25,1), \
            (0.5,0,0,1), (0,0.98,0.6,1), (0.5,0.5,0.5,1), (1,0.87,0.68,1)]
    assert isinstance(tower_list, list), "List of towers is not a list"

    count = 0
    rect_list = []
    for i in tower_list:
        if i != None:
            # patches.Rectangle((x,y) tuple, width, height) which works perfectly with the Tower object
            rect = patches.Rectangle(i.start_coord,i.width,i.height, fc=colors[count%len(colors)] ,ec=edges[count%len(edges)])
            rect_list.append(rect)
        else:
            rect_list.append(None)
        count += 1
    return rect_list

def full_coverage(desired_width,desired_height):
    """Returns number of towers required to completely cover the region of interest defined by the desired width
    and the desired height. Also returns a list of the original random towers and a list of the trimmed towers.

    Arguments:
        desired_width {int} -- Width of the desired coverage footprint
        desired_height {int} -- Height of the desired coverage footprint
    """
    assert isinstance(desired_height,int) and desired_height > 0, "Coverage area height is not a positive int"
    assert isinstance(desired_width,int) and desired_width > 0, "Coverage area width is not a positve int"

    placed = []
    original = []
    new_tower = create_rand_tower(desired_width, desired_height)
    # Never need to check if the first tower provides unique coverage
    original.append(new_tower)
    placed.append(new_tower)
    count = 1
    while True:
        if coverage_area(placed) == desired_height*desired_width:
            break
        new_tower = create_rand_tower(desired_width, desired_height)
        trim_tower = create_max(new_tower, placed)
        # Checks if the tower provides unique coverage to the region of interest
        if trim_tower is not None:
            original.append(new_tower)
            placed.append(trim_tower)
            count += 1
    return [placed, original, count]