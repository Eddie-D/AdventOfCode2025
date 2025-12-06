file = open("input.txt")

lines = [l.rstrip() for l in file.readlines()]

for i, l in enumerate(lines) :
    if l == "" :
        fresh = [[int(r) for r in l.split('-')] for l in lines[:i]]
        fruits = [int(l) for l in lines[i+1:]]

total = 0
for f in fruits :
    for r in fresh :
        if r[0] <= f and f <= r[1] : 
            total += 1
            break

print(f"Total: {total}")
