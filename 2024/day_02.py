import config


input_file = 'input_day_02.txt'
selected_bad_reports = ""
go_over_limit_for_bad_cases = 0
flat_for_bad_cases = 0
variation_issue_for_bad_cases = 0

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


def safe_report_selector(reports_input,filter_bad_reports):
    safe_report_quantity = 0
    global selected_bad_reports, go_over_limit_for_bad_cases, flat_for_bad_cases, variation_issue_for_bad_cases
    
    print("reports_input: ", len(reports_input.split("\n")))
    for i, report in enumerate(reports_input.split("\n")):
        previous_level = 0
        current_variation = "null"
        for j, level in enumerate(report.split(" ")):
            if(j == 0):
                previous_level = level
                continue
            new_variation = determine_variation(previous_level, level)
            if(abs(int(level)-int(previous_level))>3 or (current_variation != "null" and new_variation!=current_variation) or new_variation == "flat"):
                # continue here
                if(filter_bad_reports):
                    # selected_bad_reports = selected_bad_reports + report.replace(" "+str(previous_level),"",1)+"\n"
                    report_to_filter = report.split(" ")
                    del report_to_filter[j-1]
                    report_filtered_string = " ".join(report_to_filter)
                    selected_bad_reports = selected_bad_reports + report_filtered_string +"\n"
                else:
                    if(abs(int(level)-int(previous_level))>3):
                        go_over_limit_for_bad_cases = go_over_limit_for_bad_cases + 1
                    elif(new_variation == "flat"):
                        flat_for_bad_cases = flat_for_bad_cases + 1
                    elif(current_variation != "null" and new_variation!=current_variation):
                        variation_issue_for_bad_cases = variation_issue_for_bad_cases + 1
                break
            else:
                previous_level = level
                if(j==1):
                    current_variation = new_variation
                    continue
                if(j>1):
                    if(j == len(report.split(" ")) - 1):
                        safe_report_quantity = safe_report_quantity + 1
    
    return (safe_report_quantity)

def part2(puzzle_input):
    safe_report_quantity = safe_report_selector(puzzle_input, True)
    safe_report_quantity = safe_report_quantity + safe_report_selector(selected_bad_reports, False)
    return(safe_report_quantity)


print('Part 1:', part1(puzzle_input))
print('Part 2:', part2(puzzle_input))
print("go_over_limit_for_bad_cases: ",go_over_limit_for_bad_cases)
print("flat_for_bad_cases: ", flat_for_bad_cases)
print("variation_issue_for_bad_cases: ", variation_issue_for_bad_cases)
print("RAF:", go_over_limit_for_bad_cases+ flat_for_bad_cases + variation_issue_for_bad_cases)


