from typing import Optional

import data

# Write your functions for each part in the space below.

# Part 1
#Function creates a logical rectangle based on given points
#It takes two Point objects as input
#Returns a Rectangle object
def create_rectangle(pA: data.Point, pB: data.Point) -> data.Rectangle:
    LX = min(pA.x, pB.x)
    LY = min(pA.y, pB.y)
    RX = max(pA.x, pB.x)
    RY = max(pA.y, pB.y)

    nPL = data.Point(LX, RY)
    nPR = data.Point(RX, LY)

    rect = data.Rectangle(nPL, nPR)

    return rect

# Part 2
#Function compares two Duration objects, returns True only if first is lesser than second,
#and False otherwise
#Takes two Duration objects as input
#Returns bool (Boolean) value as output
def shorter_duration_than(a: data.Duration, b: data.Duration) -> bool:
    sA = a.minutes * 60 + a.seconds
    sB = b.minutes * 60 + b.seconds

    if sA < sB:
        return True
    else:
        return False

# Part 3
#Function goes through a list of songs and returns a new list of songs
#(selected from original list) which are of lesser duration than a given upper bound
#Takes list of Song objects, and a Duration object as input
#Returns a new list of Song objects
def songs_shorter_than(songs: list[data.Song], upper: data.Duration) -> list[data.Song]:

    L = []
    upperS = upper.minutes * 60 + upper.seconds

    for song in songs:
        v = song.duration.minutes * 60 + song.duration.seconds
        if v < upperS:
            L.append(song)

    return L

# Part 4
#Function calculates the runtime of a list of songs in a given order
#Takes list of Song objects, and a list of integers (the order) as input
#Returns a Duration object
def running_time(songs: list[data.Song], order: list[int]) -> data.Duration:
    secL = []

    for song in songs:
        secL.append(song.duration.seconds + song.duration.minutes * 60)

    tS = 0

    for i in order:
        if i >= 0:
            tS += secL[i]

    m = tS // 60
    s = tS % 60

    r = data.Duration(m, s)
    return r

# Part 5
#Function ensures that given a route and the possible links of city, the route is traversable
#Takes list of lists of strings (the city links), and list of strings (the route) as input
#Returns a bool value based on whether it is traversable
def validate_route(city_links: list[list[str]], route: list[str]) -> bool:
    for i in range(len(route) - 1):
        l = route[i:i + 2]
        lr = l[::-1]

        if not(l in city_links or lr in city_links):
            return False

    return True

# Part 6
#Function finds the index where the longest sublist containing the same integer begins
#Takes a list of integers as input
#Returns None if no repetition exists,
#otherwise the index (as integer) where max repetition begins
def longest_repetition(items: list[int]) -> Optional[int]:
    p = 0.1
    sindx = 0
    tindx = 0
    cmax = 0
    tmax = 0

    for i in range(len(items)):
        if p != items[i]:
            p = items[i]
            sindx = i
            cmax = 0
        else:
            cmax += 1

        if cmax > tmax:
            tmax = cmax
            tindx = sindx

    if(tmax == 0):
        return None
    else:
        return tindx
