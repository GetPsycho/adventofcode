import os

#import + read the file
work_folder = os.getcwd()
input_relative_path = "2023/input_day_05.txt"
input_absolute_path = os.path.join(work_folder,input_relative_path)
f = open(input_absolute_path, "r").read().strip()


