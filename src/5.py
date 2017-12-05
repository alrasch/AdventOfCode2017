with open('input5.txt') as input:
    lines = input.readlines()
    for i, line in enumerate(lines):
        lines[i] = int(line.rstrip())

    index = 0
    steps = 0
    try:
        while True:
            lines[index] += 1
            index += (int(lines[index]) - 1)
            steps += 1
    except IndexError:
        print('Exited after ', steps, ' steps.')

with open('input5.txt') as input:
    lines = input.readlines()
    for i, line in enumerate(lines):
        lines[i] = int(line.rstrip())

    index = 0
    steps = 0
    try:
        while True:
            print(index)
            if int(lines[index]) >= 3:
                lines[index] -= 1
                index += (int(lines[index]) + 1)
            else:
                lines[index] += 1
                index += (int(lines[index]) - 1)
            steps += 1
    except IndexError:
        print('Exited after ', steps, ' steps.')

