import matplotlib.patches as patches
from TowerClass import Tower
from Modules import create_rand_tower, create_max

# Modules specifically for the Jupyter Notebook documentation and visualization
def coverage(desired_width, desired_height, num_towers, replace = True):
    placed = []
    original = []
    new_tower = create_rand_tower(desired_width, desired_height)
    original.append(new_tower)
    placed.append(new_tower)
    if replace:
        count = 1
        while count < num_towers:
            if coverage_area(placed) == desired_height*desired_width:
                break
            new_tower = create_rand_tower(desired_width, desired_height)
            trim_tower = create_max(new_tower, placed)
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
    if coverage_area(tower_list) != desired_width*desired_height:
        return "There are gaps in the coverage"
    else:
        return "There are no gaps in the coverage"

def coverage_area(tower_list):
    total_area = 0
    for i in tower_list:
        if i != None:
            total_area = total_area + i.area
    return total_area

def get_rects(tower_list):
    colors = [(0,0,1,0.5), (0,0.5,0,0.5), (1,0,0,0.5), (0,0.5,0.5,0.5), (0.3,0,0.51,0.5), (1,0.65,0,0.5), (0.80,0.52,0.25,0.5), \
            (0.5,0,0,0.5), (0,0.98,0.6,0.5), (0.5,0.5,0.5,0.5), (1,0.87,0.68,0.5)]
    edges = [(0,0,1,1), (0,0.5,0,1), (1,0,0,1), (0,0.5,0.5,1), (0.3,0,0.51,1), (1,0.65,0,1), (0.80,0.52,0.25,1), \
            (0.5,0,0,1), (0,0.98,0.6,1), (0.5,0.5,0.5,1), (1,0.87,0.68,1)]
    count = 0
    rect_list = []
    for i in tower_list:
        if i != None:
            rect = patches.Rectangle(i.start_coord,i.width,i.height, fc=colors[count%len(colors)] ,ec=edges[count%len(edges)])
            rect_list.append(rect)
        else:
            rect_list.append(None)
        count += 1
    return rect_list
