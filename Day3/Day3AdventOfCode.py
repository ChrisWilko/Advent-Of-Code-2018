from collections import Counter
import re


def first(string, canvas_size):
    canvas = [[None] * canvas_size for _ in range(canvas_size)]
    for claim in string:
        match = re.match(r'^#(?P<claim>\d+) @ (?P<x>\d+),(?P<y>\d+): (?P<w>\d+)x(?P<h>\d+)', claim)
        for row in range(1, int(match['w']) + 1):
            for col in range(1, int(match['h']) + 1):
                a = row + int(match['x']) - 1
                b = col + int(match['y']) - 1
                if not canvas[a][b]:
                    canvas[a][b] = claim
                else:
                    canvas[a][b] = 'X'
    c = Counter(x for xs in canvas for x in xs)
    return c['X']


with open('input.txt', 'r') as file:
    lines = [line.rstrip() for line in file]
print(first(lines, 1100))

