class Tower:
    """ Tower Object
    """

    def __init__(self, start_coord, height, width):
        """Initialization of the Tower Object

        Arguments:
            start_coord {tuple} -- bottom left hand corner of the tower's coverage
            height {int} -- height of the tower's coverage
            width {int} -- width of the tower's coverage
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

    @property
    def area(self):
        """Area of the tower's coverage
        """
        return self.height*self.width

