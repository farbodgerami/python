class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


# pazirandeye topple
# def fallsinrectangle(self,lowleft,upright):
#     if lowleft[0] < self.x < upright[0] \
#         and lowleft[1] < self.y < upright[1]:
#         return True
#     else:
#         return False

# pazirandeye object:

    def fallsinrectangle(self, rectangle):
        if rectangle.lowleft.x < self.x <  rectangle.upright.x \
            and  rectangle.lowleft.y < self.y <  rectangle.upright.y:
            return True
        else:
            return False

    def distancefrompoint(self, point):
        return ((self.x - point.x)**2 + (self.y - point.y)**2)**0.5


class Rectangle:
    def __init__(self, lowleft, upright):
        self.lowleft = lowleft
        self.upright = upright
    
    def area(self):
        return (self.upright.x-self.lowleft.x)*(self.upright.y-self.lowleft.y)
