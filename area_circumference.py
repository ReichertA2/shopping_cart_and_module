import math

def area():
    area = ""
    l = int(input('What is the length of the house in ft?'))
    w = int(input('What is the width of the house in ft?'))
    area = l*w
    print(f'The area of the house is {area} sqft.')

area()


def circumference():
    circumference = ""
    r = int(input('What is the radius of the circle? '))
    circumference = 2*math.pi*r
    print(f'The circumference of the circe is {circumference}.')


circumference()
