file = open("input.txt")

current = 50
zeroes = 0
for line in file :
    dir = -1 if line[0] == "L" else 1
    amount = int(line[1:])
    current = (dir * amount + current) % 100
    if current == 0 : zeroes += 1

print(f"There are {zeroes} zeroes")