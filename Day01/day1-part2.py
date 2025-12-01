file = open("input.txt")

current = 50
zeroes = 0
for line in file :
    dir = -1 if line[0] == "L" else 1
    amount = int(line[1:])
    new = (current + (dir * amount))
    # print(f"{line[0:-1]}: {abs(((dir *(new)) // 100) - (dir * current // 100))}, total: {new}")
    zeroes += abs(((dir *(new)) // 100) - (dir * current // 100))
    current = new

print(f"There are {zeroes} zeroes")