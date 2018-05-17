class Tower:
    """ Tower Object
    """

    def __init__(self, start_coord, width, height):
        """Initialization of the Tower Object

        Arguments:
            start_coord {tuple} -- bottom left hand corner of the tower's coverage (x,y)
            width {int} -- width of the tower's coverage (x-axis)
            height {int} -- height of the tower's coverage (y-axis)
        """
        assert isinstance(start_coord,tuple) and len(start_coord) == 2, "Starting Coordinate has incorrect structure"
        assert start_coord[0] >= 0 and start_coord[1] >= 0, "Starting Coordinates must both be >= 0"
        assert isinstance(height,int) and height > 0, "Height must be a positive integer"
        assert isinstance(width, int) and width > 0, "Width must be a positive integer"

        self.start_coord = start_coord
        self.height = height
        self.width = width

    def __repr__(self):
        """Representation of the Tower Object
        """
        return "Starting Coord:%s, Width :%s, Height:%s" % (self.start_coord, self.width, self.height)

    def __eq__(self, other):
        """Returns true if the starting coordinate, height, and width are the same
        """
        assert isinstance(other,Tower), "Tower not being compared to another Tower"
        return self.start_coord == other.start_coord and self.height == other.height and self.width == other.width

    def __lt__(self,other):
        """Returns true if there is coverage to the left of other's coverage
        """
        assert isinstance(other,Tower), "Tower not being compared to another Tower"
        return self.start_coord[0] < other.start_coord[0]

    def __gt__(self,other):
        """Returns true if there is coverage to the right of other's coverage
        """
        assert isinstance(other,Tower), "Tower not being compared to another Tower"
        return self.right > other.right

    def __le__(self,other):
        """Returns true if there is coverage below other's coverage
        """
        assert isinstance(other,Tower), "Tower not being compared to another Tower"
        return self.start_coord[1] < other.start_coord[1]

    def __ge__(self,other):
        """Returns true if there is coverage above other's coverage
        """
        assert isinstance(other,Tower), "Tower not being compared to another Tower"
        return self.top > other.top

    @property
    def area(self):
        """Returns area of the tower's coverage
        """
        return self.height*self.width

    # Left and bottom unneeded because they are easily accessed through the start_coord
    @property
    def right(self):
        """Returns the "coordinate" of the right most edge of the rectangle
        """
        return self.start_coord[0] + self.width

    @property
    def top(self):
        """Returns the "coordinate" of the top most edge of the rectangle
        """
        return self.start_coord[1] + self.height

    def intersects(self,other):
        """Returns true if the tower's coverage intersects with another's coverage, otherwise returns false
        """
        assert isinstance(other,Tower), "Tower not being compared to another Tower"
        if ((self.start_coord[0]+self.width) <= other.start_coord[0]) or \
            (self.start_coord[0] >= (other.start_coord[0]+other.width)) or \
            (self.start_coord[1] >= (other.start_coord[1]+other.height)) or \
            ((self.start_coord[1]+self.height) <= other.start_coord[1]):
            return False
        return True