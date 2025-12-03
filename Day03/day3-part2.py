file = open("input.txt")

total = 0
for line in file :
    line = line.rstrip() # Remove whitespace including '\n'
    joltages = [0 for _ in range(13)]
    for si, s in enumerate(line) :
        val = int(s)
        joltages[len(joltages) - 1] = val
        for i in range(len(joltages) - 1) :
            if joltages[i+1] > joltages[i] :
                for j in range(i, len(joltages)-1): joltages[j] = joltages[j+1]
                break

    joltages = joltages[0:-1]
    total += int("".join([str(j) for j in joltages]))

print(f"Total: {total}")