import math
def steps(n):
    root = math.ceil(math.sqrt(n))
    current = root if root % 2 != 0 else root + 1
    number = (current-1) / 2
    cycle = n - ((current - 2) ** 2)
    inner_offset = cycle % (current-1)
    return int(number + math.fabs(inner_offset - number))

from collections import defaultdict
from itertools import count

def sum_spiral():
    grid = defaultdict(int)
    get_value = lambda i,j: sum(grid[k,l] for k in range(i-1, i+2) for l in range(j-1, j+2))
    grid[0, 0], i, j = 1, 0, 0
    for s in count(1, 2):
        for _ in range(s):
            i += 1
            grid[i, j] = get_value(i, j)
            yield grid[i, j]
        for _ in range(s):
            j -= 1
            grid[i, j] = get_value(i, j)
            yield grid[i, j]
        for _ in range(s+1):
            i -= 1
            grid[i, j] = get_value(i, j)
            yield grid[i, j]
        for _ in range(s+1):
            j += 1
            grid[i, j] = get_value(i, j)
            yield grid[i, j]

def part2():
    for x in sum_spiral():
        if x > 361527: return x

print(steps(361527))
print(part2())
