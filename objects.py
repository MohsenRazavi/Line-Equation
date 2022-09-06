from math import sqrt


class Point:
    name = 'Point'

    def __init__(self, **kwargs):
        """
        pass x=  and y=
        """
        if 'name' in kwargs:
            self.name = kwargs['name']
        self.x = kwargs['x']
        self.y = kwargs['y']

    def __str__(self):
        return f'{self.name}({self.x}, {self.y})'


class Line:
    name = 'Line'

    def __init__(self, **kwargs):
        """
        pass start_point=  and end_point=  to the constructor
        these arguments should be instants of Point class
        """
        if 'name' in kwargs:
            self.name = kwargs['name']
        self.s_point = kwargs['start_point']
        self.e_point = kwargs['end_point']
        self.length = self.__len__()
        self.equation = self.get_equation()

    def __str__(self):
        return f'Line {self.equation} | length {self.length}'

    def __len__(self):
        yy = (self.e_point.y - self.s_point.y) ** 2
        xx = (self.e_point.x - self.s_point.x) ** 2
        return sqrt(yy + xx)

    def get_equation(self):
        self.m = (self.e_point.y -
                  self.s_point.y) / (self.e_point.x - self.s_point.x)
        self.y_intercept = self.s_point.y - self.m*self.s_point.x
        if self.y_intercept > 0:
            return f'y = {self.m}x + {self.y_intercept}'
        return f'y = {self.m}x {self.y_intercept}'

    def is_point_on_line(self, point):
        if point.x > self.e_point.x or point.x < self.s_point.x :
            return False

        status = point.y == self.m*point.x + self.y_intercept
        if status:
            return True
        return False

    def area_between_line_and_x_axis(self):
        area = (self.m/2)*((self.e_point.x**2) - (self.s_point.x**2)) + \
            self.y_intercept*(self.e_point.x - self.s_point.x)
        return area

    def get_gradient(self):
        return self.m
