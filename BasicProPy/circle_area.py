import math

def circle_area(radius):
    pi = math.pi
    area = math.pow(radius, 2) * pi
    return area

def main():
    radius = 2.0
    print(circle_area(radius))

main()