#1  Point Class

class Point:
    """
    Representation of a single Point, which is composed of
    an arbitary number of coordinates.
    """
    
    def __init__(self, coords):
        """
        Initializer for a Point; coords must be a list of coordinates.
        """
        self._coords = coords        
    
    def __str__(self):
        """
        Returns a string representation of this Point.
        """
        result = "["
        for coord in self._coords:
            result += str(coord) + ", "
        result = result[:-2]
        result += "]"
        return result
        
    def get_coord(self, index):
        """
        Returns the index-th coordinate within this Point.
        """
        return self._coords[index]
    
    def set_coord(self, index, value):
        """
        Sets the index-th coordinate of this Point to 'value'.
        """
        self._coords[index] = value
        
    def get_coords(self):
        """
        Returns the list of coordinates comprising this Point.
        """
        return self._coords
        
    def set_coords(self, coords):
        """
        Sets the coordinates comprising this Point to 'coords'.
        """
        self._coords = coords

#2  Shape Class (Bonus)

class Shape:
    def __init__(self, points=[]):
        """
        Initializer for a Shape, which is composed of a list
        of Points.

        Implementation note:  __str__ relies on that list being
        named "self._points".
        """
        self._points = points
        
    def __str__(self):
        """
        Returns a string representation of this Shape.
        """
        result = "["
        for point in self._points:
            result += str(point) + ", "
        result = result[:-2]
        result += "]"
        return result
   
    def get_point(self, index):
        """
        Given an index, returns the index-th Point in this shape.
        """
        return self._points[index]
         
    def set_point(self, index, point):
        """
        Given an index and a Point ('point'), sets the index-th 
        Point in this shape to 'point'.
        """
        self._points[index] = point
       
    def get_points(self):
        """
        Returns the list of Points comprising this Shape.
        """
        return self._points
    
    def set_points(self, points):
        """
        Sets the list of Points comprising this Shape.
        """
        self._points = points
    
    def add_point(self, point):
        """
        Adds the given Point to this shape.
        """
        self._points.append(point)


"""
print(Shape([Point([1, 2]), Point([3, 4])]))
Should print: [[1, 2], [3, 4]]
"""