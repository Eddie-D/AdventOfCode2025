file = open("input.txt")

total = 0
for line in file :
    line = line.rstrip() # Remove whitespace including '\n'
    pair = [0,0]
    for si, s in enumerate(line) :
        val = int(s)
        if pair[1] > pair[0] :
            pair[0] = pair[1]
            pair[1] = val
        elif val > pair[1] :
            if pair[1] > pair[0] :
                pair[0] = pair[1]
            pair[1] = val
        elif val > pair[0] and len(line) > si + 1 :
            pair[1] = val
        # print(f"pair: {pair}, val: {val}")
    print(pair)
    total += 10*pair[0] + pair[1]

print(f"Total: {total}")