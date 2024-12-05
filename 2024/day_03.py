import config
import re


input_file = 'input_day_03.txt'
with open(config.input_absolute_path+input_file, 'r') as f:
    puzzle_input = f.read()


def part1(puzzle_input):
    sum = 0
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    occurences = re.findall(pattern, puzzle_input)
    for value1,value2 in occurences:
            sum = sum + int(value1) * int(value2)
    return(sum)


def part2(puzzle_input):
    sum = 0
    pattern = r"(do\(\))|(don't\(\))|(mul\((\d{1,3}),(\d{1,3})\))"
    mul_active = True

    for match in re.finditer(pattern, puzzle_input):
        do, dont, mul, val1, val2 = match.groups()
        if do:
            mul_active = True
        elif dont:
            mul_active = False 
        elif mul and mul_active:
            sum = sum + int(val1) * int(val2)
    return(sum)


# print('Part 1:', part1(puzzle_input))
print('Part 2:', part2(puzzle_input))


