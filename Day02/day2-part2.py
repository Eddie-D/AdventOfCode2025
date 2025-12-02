from functools import reduce
from sympy import primefactors

file = open("./input.txt")

# For a breakdown with identical sections, any breakdown of that by a 
# divisor of its section size will also work.
# So we only need to check prime factors 
def checkSections(i) :
    s = str(i)
    l = len(s)
    factors = primefactors(l)
    # Prime length or single digit length would create one section, so exit now
    if l == 1 or factors[0] == i : return 0

    for p in factors :
        size = l // p
        sections = [s[(x*size):((x+1)*size)] for x in range(0,p)]

        if all(map(lambda x: x==sections[0], sections)) :
            return i
    return 0

total = 0
for line in file :
    pairs = [x.split('-') for x in line.split(',')]
    for start, end in pairs:
        print(f"Starting {start}")
        for i in range(int(start), int(end) + 1) :
            total += checkSections(i)

print(f"Total is: {total}")