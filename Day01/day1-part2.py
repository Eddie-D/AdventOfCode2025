file = open("input.txt")

current = 50
zeroes = 0
for line in file :
    dir = -1 if line[0] == "L" else 1
    amount = int(line[1:])
    new = (current + (dir * amount))
    # The floor idea works only when second number is bigger than first (56 -> 0 would return 0, but 56 -> 100 returns 1) dir multiplication compensates for this
    zeroes += abs((dir * new // 100) - (dir * current // 100))
    current = new

print(f"There are {zeroes} zeroes")