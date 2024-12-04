import config


input_file = 'input_day_02.txt'
with open(config.input_absolute_path+input_file, 'r') as f:
    puzzle_input = f.read()

def determine_variation(previous_level,current_level):
    variation_value = int(current_level)-int(previous_level)
    if(variation_value<0):
        variation = "decreasing"
    elif(variation_value==0):
        variation = "flat"
    else:
        variation = "increasing"
    return variation

def part1(puzzle_input):
    safe_report_quantity = 0
    for i, report in enumerate(puzzle_input.split("\n")):
        previous_level = 0
        current_variation = "null"
        for j, level in enumerate(report.split(" ")):
            if(j == 0):
                previous_level = level
                continue
            new_variation = determine_variation(previous_level, level)
            if(abs(int(int(level)-int(previous_level)))>3 or (current_variation != "null" and new_variation!=current_variation) or new_variation == "flat"):
                break
            else:
                previous_level = level
                if(j==1):
                    current_variation = new_variation
                    continue
                if(j>1):
                    if(j == len(report.split(" ")) - 1):
                        safe_report_quantity = safe_report_quantity + 1
    return(safe_report_quantity)

# 7 6 4 2 1
# 1 2 7 8 9
# 9 7 6 2 1
# 1 3 2 4 5
# 8 6 4 4 1
# 1 3 6 7 9


def part2(puzzle_input):
    safe_report_quantity = 0
    for i, report in enumerate(puzzle_input.split("\n")):
        previous_level = 0
        current_variation = "null"
        for j, level in enumerate(report.split(" ")):
            if(j == 0):
                previous_level = level
                continue
            new_variation = determine_variation(previous_level, level)
            if(abs(int(int(level)-int(previous_level)))>3 or (current_variation != "null" and new_variation!=current_variation) or new_variation == "flat"):
                # continue here
                break
            else:
                previous_level = level
                if(j==1):
                    current_variation = new_variation
                    continue
                if(j>1):
                    if(j == len(report.split(" ")) - 1):
                        safe_report_quantity = safe_report_quantity + 1
    return(safe_report_quantity)


# print('Part 1:', part1(puzzle_input))
print('Part 2:', part2(puzzle_input))


