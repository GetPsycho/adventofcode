import os

#import + read the file
work_folder = os.getcwd()
input_relative_path = "adventofcode\\2023\\input_day_05.txt"
input_absolute_path = os.path.join(work_folder,input_relative_path)
f = open(input_absolute_path, "r").read().strip()

#split line by line
for line_number, line in enumerate(f.split("\n")):
    
    #put the seeds into a data structure
    # print('line_number: '+ str(line_number)+ ' line:'+ str(line))
    if line.startswith('seeds'):
        split_seed_line = line.split(':')
        print('line: '+ str(split_seed_line))




