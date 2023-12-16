
import os

#import + read the file
work_folder = os.getcwd()
input_relative_path = "2023/input_day_04.txt"
input_absolute_path = os.path.join(work_folder,input_relative_path)
f = open(input_absolute_path, "r").read().strip()

splitFile = f.split("\n")
lineNumber = len(splitFile)
StringLength = len(splitFile[0])
globalCount = 0

#we browse, line by line
for indice_line, data_line in enumerate(f.split("\n")):

    split_List = data_line.split(":")
    card_name = split_List[0]
    card_data = split_List[1]
    card_data_split = card_data.split("|")

    #winning numbers list
    number_winning_list = card_data_split[0]
    number_winning_list = number_winning_list.replace("  "," ")
    number_winning_list_split = number_winning_list.strip().split(" ")
    print("number_winning_list_split: "+str(number_winning_list_split))

    #owned numbers list
    number_owned_list = card_data_split[1]
    number_owned_list = number_owned_list.replace("  "," ")
    number_owned_list_split = number_owned_list.strip().split(" ")
    print("number_owned_list_split: "+str(number_owned_list_split))

    #we check if there is winning numbers
    matching_numbers = 0
    for owned_number in number_owned_list_split:
        if owned_number in number_winning_list_split:
            matching_numbers = matching_numbers+1

    #card point value calculation
    # 1 = 1, 2 = 2 ,3 = 4, 4 = 8, 5 = 16, etc...
    card_value = 1
    if(matching_numbers != 0):
        card_value = 2 ** (matching_numbers-1)
        globalCount +=card_value
    print("***********globalCount: " + str(globalCount))



