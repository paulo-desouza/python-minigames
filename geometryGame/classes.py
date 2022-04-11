import math
from random import randint


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def falls_in_rectangle(self, rectangle):
        if rectangle.point1.x < self.x < rectangle.point2.x \
                and rectangle.point1.y < self.y < rectangle.point2.y:
            return True
        else:
            return False

    def distance_from_point(self, point):
        distanceX = self.x - point.x
        distanceY = self.y - point.y
        totalDistance = (distanceX ** 2 + distanceY ** 2) ** 0.5
        return totalDistance


class Rectangle:

    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def calculates_area(self):
        return (self.point2.x - self.point1.x) * (self.point2.y - self.point1.y)


rectangle = Rectangle(
    Point(randint(0, 9), randint(0, 9)),
    Point(randint(10, 19), randint(10, 19))
)

print(f'Rectangle coordinates: ({rectangle.point1.x}, {rectangle.point1.y})'
      f' and ({rectangle.point2.x}, {rectangle.point2.y}) ')

user_point = Point(float(input('Guess coordinate X: ')),
                   float(input('Guess coordinate Y:')))

if user_point.falls_in_rectangle(rectangle):
    print('Your point falls into the rectangle! Congratulations. ')
else:
    print('You lose . . . ')

user_area = float(input('What would the area of this rectangle be?'))
if rectangle.calculates_area() == user_area:
    print('Correct. Here is a cookie.')
else:
    print('No dice. Better luck next time.')

