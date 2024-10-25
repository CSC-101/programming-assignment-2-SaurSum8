from typing import Optional

import data

# Write your functions for each part in the space below.

# Part 1
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
def shorter_duration_than(a: data.Duration, b: data.Duration) -> bool:
    sA = a.minutes * 60 + a.seconds
    sB = b.minutes * 60 + b.seconds

    if sA < sB:
        return True
    else:
        return False

# Part 3
def songs_shorter_than(songs: list[data.Song], upper: data.Duration) -> list[data.Song]:

    L = []
    upperS = upper.minutes * 60 + upper.seconds

    for song in songs:
        v = song.duration.minutes * 60 + song.duration.seconds
        if v < upperS:
            L.append(song)

    return L

# Part 4
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
def validate_route(city_links: list[list[str]], route: list[str]) -> bool:
    for i in range(len(route) - 1):
        l = route[i:i + 2]
        lr = l.reverse()

        if not(l in city_links and lr in city_links):
            return False

    return True

# Part 6
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
