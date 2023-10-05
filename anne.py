import math

def distance(x1, y1, x2, y2):
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)

def next_location(posX, posY, locations):
    min_distance = float('inf')
    next_x, next_y = None, None
    
    for x, y in locations:
        d = distance(posX, posY, x, y)
        if d < min_distance:
            min_distance = d
            next_x, next_y = x, y
            
    return next_x, next_y

posX, posY = map(int, input().split())
z = int(input())

locations = []
for i in range(z):
    x, y = map(int, input().split())
    locations.append((x, y))

next_x, next_y = next_location(posX, posY, locations)

print(next_x,next_y)
