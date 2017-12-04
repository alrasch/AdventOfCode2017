with open('input4.txt') as input:
    line = input.readline()
    invalid = 0
    lines = 0
    while line:
        words = line.split()
        if len(words) != len(set(words)):
            invalid += 1
        line = input.readline()
        lines += 1
    print(int(lines - invalid))

with open ('input4.txt') as input:
    line = input.readline()
    res = 0
    while line:
        x = ["".join(sorted(i)) for i in line.split()]
        if (len(x) == len(set(x))):
            res += 1
        line = input.readline()
    print(res)
