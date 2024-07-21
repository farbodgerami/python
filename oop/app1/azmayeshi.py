from random import randint
from geometry import Point, Rectangle

# point5=Point(2,3)
# print(point5.x)
# print(Point(34,65))
# print(Point(6,3).x)

# Point(3,6).abc()

p1 = Point(0, 0)
# print(p1)
# voroodie tupple:
# print(p1.fallsinrectangle((1,2),(3,4)))
# p2=Point(0,0)
# distance=p2.distancefrompoint(1,1)
# print(distance)

# p2=PPoint(1,1)
# distance=p2.distancefrompoint(p1)
# print(distance)

poinx = Point(6, 7)
# pass natige inke yek kelas mitoone object
# haii az kelashaye dge begire va rooshoon kar kone
# voroodie object:
# rectanglex=Rectangle(Point(5,6),Point(7,9))
rectanglex = Rectangle(Point(randint(0, 9), randint(0, 9)),
                       Point(randint(10, 19), randint(10, 19)))
# print(poinx)
j = poinx.fallsinrectangle(rectanglex)
print(j)

print(rectanglex.lowleft.x,  rectanglex.lowleft.y,rectanglex.upright.x,rectanglex.upright.y)

userpoint = Point(float(input("guess x: ")), float(input("guess y: ")))
print("False or tru?", userpoint.fallsinrectangle(rectanglex))

userarea=float(input("area ro hads bezan:"))
print("your area was off by: ",rectanglex.area()-userarea)