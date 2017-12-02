import itertools
def get_numbers(string):
    return [int(n) for n in string.split()]

def solve_1():
    with open('input2.txt', 'r') as input:
        line = input.readline()
        sum = 0
        while line:
            numbers = line.split()
            numbers = [int(number_string) for number_string in numbers]
            diff = max(numbers) - min(numbers)
            sum += diff

            line = input.readline()
        print(sum)

def solve_2():
    with open('input2.txt', 'r') as input:
        line = input.readline()
        sum = 0
        while line:
            numbers = line.split()
            numbers = [int(number_string) for number_string in numbers]
            for combo in itertools.combinations(numbers, 2):
                if max(combo) % min(combo) == 0:
                    sum += max(combo) / min(combo)
                    break
            line = input.readline()
        print(int(sum))

solve_1()
solve_2()
