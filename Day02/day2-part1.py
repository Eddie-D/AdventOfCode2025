file = open("./input.txt")

total = 0
for line in file :
    pairs = [x.split('-') for x in line.split(',')]
    for start, end in pairs:
        for i in range(int(start), int(end) + 1) :
            s = str(i)
            if s[:len(s)//2] ==  str(s)[len(s)//2:] :
                total += i
                print(f"adding {i}")

print(f"Total is: {total}")