file = open("input.txt")

lines = [l.rstrip() for l in file.readlines()]

for i, l in enumerate(lines) :
    if l == "" :
        fresh = [[int(r) for r in l.split('-')] for l in lines[:i]]
        fruits = [int(l) for l in lines[i+1:]]

total = 0
fresh.sort(key=lambda f: f[0])
print(fresh)
old = [-1,-1]
remove = []
for i, r in enumerate(fresh) :
    if r[0] <= old[1] and old[1] <= r[1]:
        old[1] = r[1]
        remove.insert(0,i)
    elif r[0] <= old[1] :
        remove.insert(0,i)
    else :
        old = r

print(remove)

for i in remove :
    fresh.pop(i)

print(fresh)

for f1, f2 in fresh :
    total += f2 + 1 - f1

print(f"Total: {total}")
