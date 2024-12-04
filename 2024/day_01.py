import config


input_file = 'input_day_01.txt'
with open(config.input_absolute_path+input_file, 'r') as f:
    puzzle_input = f.read()

def part1(puzzle_input):
    location_1 = []
    location_2 = []
    for i, data in enumerate(puzzle_input.split("\n")):
        location_1.append(data.split()[0])
        location_2.append(data.split()[1])

    location_1.sort()
    location_2.sort()
    distance = 0
    for i in range(len(location_1)):
        distance = distance + abs(int(location_1[i]) - int(location_2[i]))
        
    return(distance)

def part2(puzzle_input):
    location_1 = []
    location_2 = []
    for i, data in enumerate(puzzle_input.split("\n")):
        location_1.append(data.split()[0])
        location_2.append(data.split()[1])
        
    distance = 0
    for i in range(len(location_1)):
        occurence = 0
        for j in range(len(location_2)):
            if(int(location_1[i])==int(location_2[j])):
                occurence = occurence + 1
        distance = distance + occurence*int(location_1[i])
    return(distance)

# print('Part 1:', part1(puzzle_input))
print('Part 2:', part2(puzzle_input))


