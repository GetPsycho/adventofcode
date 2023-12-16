

import os
import re

gear_dictionary = {}
def check_in_range(array, index):
    return 0 <= index < len(array)

def constitute_key_for_dictionary(kline,kcol):
    return "gear_"+str(kline)+"_"+str(kcol)

def insert_in_dictionary(kline,kcol,value):
    gear_dictionary[constitute_key_for_dictionary(kline,kcol)] = value

def exist_in_dictionary(kline,kcol):
    return constitute_key_for_dictionary(kline,kcol) in gear_dictionary

def return_value_in_dictionary(kline,kcol):
    return gear_dictionary[constitute_key_for_dictionary(kline,kcol)]

work_folder = os.getcwd()
input_relative_path = "2023/input_daythree.txt"
input_absolute_path = os.path.join(work_folder,input_relative_path)
f = open(input_absolute_path, "r").read().strip()
#determiner le nb de lignes et colonnes du tableau à remplir


splitFile = f.split("\n")
lineNumber = len(splitFile)
StringLength = len(splitFile[0])
globalCount = 0

#create the empty 2d array
array2D = [["."] * StringLength for _ in range(lineNumber)]

#populate the 2d array
for indiceLine, elemLine in enumerate(f.split("\n")):
    for indiceCol, elemChar in enumerate(elemLine):
        array2D[indiceLine][indiceCol] = elemChar



# PART TWO #############################################################################################
#browse to find valid parameters
gear_line = 0
gear_col = 0
for arIndiceLine, arLine in enumerate(array2D):
    print("arLine: "+ str(arLine))
    for arIndiceCol, arCharELem in enumerate(arLine):
        print("arIndiceCol: "+ str(arIndiceCol))
        print("arCharELem: "+ str(arCharELem))
        potential_parameter = ""
        if(arCharELem.isdigit()):
            candidateNb = str(arCharELem)
            currentPosition = arIndiceCol
            
            #determine if next character is a digit + create the parameter string
            while(candidateNb.isdigit()):
                potential_parameter += candidateNb
                currentPosition += 1
                if(check_in_range(array2D[arIndiceLine], currentPosition)):
                    candidateNb = str(array2D[arIndiceLine][currentPosition])
                else:
                    break
        # If we found a parameter, check if there is a * around it
        if len(potential_parameter) != 0:
            #Check that there is special chars around the parameter found
            print("potential_parameter: " + str(potential_parameter))
            adjacent_number_found = False
            valid_parameter = False

            #before and after
            if(check_in_range(array2D[arIndiceLine], arIndiceCol-1)):
                before_char = str(array2D[arIndiceLine][arIndiceCol-1])
                print("just before:" + str(before_char))
                if(str(before_char)== "*"):
                    valid_parameter = True
                    gear_line = arIndiceLine
                    gear_col = arIndiceCol-1
                if(str(before_char).isdigit()):
                    adjacent_number_found = True
            if(check_in_range(array2D[arIndiceLine], currentPosition)):
                after_char = str(array2D[arIndiceLine][currentPosition])
                print("just after:" + str(after_char))
                if(after_char== "*"):
                    valid_parameter = True
                    gear_line = arIndiceLine
                    gear_col = currentPosition
                if(str(after_char).isdigit()):
                    adjacent_number_found = True

            
            #above and below
            iteration_for_above = currentPosition - arIndiceCol + 2
            for i in range(iteration_for_above):
                if(check_in_range(array2D, arIndiceLine-1) and check_in_range(array2D[arIndiceLine-1], arIndiceCol-1+i)):
                    above_char = str(array2D[arIndiceLine-1][arIndiceCol-1+i])
                    print("above:" + above_char)
                    if( above_char== "*"):
                        valid_parameter = True
                        gear_line = arIndiceLine-1
                        gear_col = arIndiceCol-1+i
                        break
                if(check_in_range(array2D, arIndiceLine+1) and check_in_range(array2D[arIndiceLine+1], arIndiceCol-1+i)):
                    below_char = str(array2D[arIndiceLine+1][arIndiceCol-1+i])
                    print("below: " + below_char)
                    if(below_char== "*"):
                        valid_parameter = True
                        gear_line = arIndiceLine+1
                        gear_col = arIndiceCol-1+i
                        break
            print("valid_parameter:" + str(valid_parameter))
            print("adjacent_number_found:" + str(adjacent_number_found))
            print("potential_parameter:" + str(potential_parameter))
            print("gear_dictionary:" + str(gear_dictionary))
            print("line_number (from 0):" + str(arIndiceLine))
            if(valid_parameter and not adjacent_number_found):
                if(exist_in_dictionary(gear_line,gear_col)):
                    print("gear_line:" + str(gear_line))
                    print("gear_col:" + str(gear_col))
                    print("value from dic:" + str(return_value_in_dictionary(gear_line,gear_col)))
                    globalCount += int(return_value_in_dictionary(gear_line,gear_col))*int(potential_parameter)
                    print("***********globalCount: " + str(globalCount))
                    print("***********")
                else:
                    insert_in_dictionary(gear_line,gear_col,potential_parameter)
                print("arIndiceLine: "+ str(arIndiceLine))
                print("***********parametre ajouté: "+ str(potential_parameter))
                print("***********")
            else:
                print("***********parametre PAS ajouté: "+ str(potential_parameter))
    print("boucle:"+str(arIndiceLine)+" terminée")

print("globalCount: "+ str(globalCount))

# print(array2D)
# PART ONE #############################################################################################
# #browse to find valid parameters
# for arIndiceLine, arLine in enumerate(array2D):
#     print("arLine: "+ str(arLine))
#     for arIndiceCol, arCharELem in enumerate(arLine):
#         print("arIndiceCol: "+ str(arIndiceCol))
#         print("arCharELem: "+ str(arCharELem))
#         potential_parameter = ""
#         if(arCharELem.isdigit()):
#             candidateNb = str(arCharELem)
#             currentPosition = arIndiceCol
            
#             #determine if next character is a digit + create the parameter string
#             while(candidateNb.isdigit()):
#                 potential_parameter += candidateNb
#                 currentPosition += 1
#                 if(check_in_range(array2D[arIndiceLine], currentPosition)):
#                     candidateNb = str(array2D[arIndiceLine][currentPosition])
#                 else:
#                     break
#         if len(potential_parameter) != 0:
#             #Check that there is special chars around the parameter found
#             print("potential_parameter: " + str(potential_parameter))
#             adjacent_number_found = False
#             valid_parameter = False
#             #before and after
#             if(check_in_range(array2D[arIndiceLine], arIndiceCol-1)):
#                 before_char = str(array2D[arIndiceLine][arIndiceCol-1])
#                 print("just before:" + str(before_char))
#                 if( str(before_char)!= "." and not str(before_char).isdigit()):
#                     valid_parameter = True
#                 if(str(before_char).isdigit()):
#                     adjacent_number_found = True
#             if(check_in_range(array2D[arIndiceLine], currentPosition)):
#                 after_char = str(array2D[arIndiceLine][currentPosition])
#                 print("just after:" + str(after_char))
#                 if(after_char!= "." and not str(after_char).isdigit()):
#                     valid_parameter = True
#                 if(str(after_char).isdigit()):
#                     adjacent_number_found = True

            
#             #above and below
#             iteration_for_above = currentPosition - arIndiceCol + 2
#             for i in range(iteration_for_above):
#                 if(check_in_range(array2D, arIndiceLine-1) and check_in_range(array2D[arIndiceLine-1], arIndiceCol-1+i)):
#                     above_char = str(array2D[arIndiceLine-1][arIndiceCol-1+i])
#                     print("above:" + above_char)
#                     if( above_char!= "." and not above_char.isdigit()):
#                         valid_parameter = True
#                         break
#                 if(check_in_range(array2D, arIndiceLine+1) and check_in_range(array2D[arIndiceLine+1], arIndiceCol-1+i)):
#                     below_char = str(array2D[arIndiceLine+1][arIndiceCol-1+i])
#                     print("below: " + below_char)
#                     if(below_char!= "." and not below_char.isdigit()):
#                         valid_parameter = True
#                         break
#             print("valid_parameter:" + str(valid_parameter))
#             print("adjacent_number_found:" + str(adjacent_number_found))
#             print("potential_parameter:" + str(potential_parameter))
#             if(valid_parameter and not adjacent_number_found):
#                 globalCount += int(potential_parameter)
#                 print("***********globalCount: " + str(globalCount))
#                 print("arIndiceLine: "+ str(arIndiceLine))
#                 print("***********parametre ajouté: "+ str(potential_parameter))
#                 print("***********")
#             else:
#                 print("***********parametre PAS ajouté: "+ str(potential_parameter))
#     print("boucle:"+str(arIndiceLine)+" terminée")

# print("globalCount: "+ str(globalCount))