# Game 1: 1 red, 3 blue, 11 green; 1 blue, 5 red; 3 blue, 5 green, 13 red; 6 red, 1 blue, 4 green; 16 red, 12 green
# Game 2: 3 red, 13 blue, 5 green; 14 green, 14 blue; 9 blue, 10 green, 3 red; 2 green, 5 blue; 11 green, 3 blue, 3 red; 16 blue, 2 red, 9 green
# Game 3: 17 blue, 5 red; 3 red, 11 green, 17 blue; 1 red, 6 blue, 9 green; 3 blue, 11 green, 1 red; 3 green, 10 red, 11 blue; 12 red, 3 green, 15 blue
# Game 4: 14 green, 14 red, 1 blue; 15 red, 13 green, 1 blue; 6 green, 15 red; 7 green
# Game 5: 3 green, 1 blue, 3 red; 6 red, 2 green, 2 blue; 12 red, 3 green, 1 blue; 2 green, 9 red; 1 blue; 2 blue, 10 red

#cubes rouges: 12
#cubes verts: 13
#cubes bleus: 14

import re
f = open(r"C:\Users\erifontaine\repopo\adventofcode\2023\input_daytwo.txt", "r").read().strip()

##############################################Daytwo - part#1 ############################################################
# stringExample = "Game 1: 1 red, 3 blue, 11 green; 1 blue, 5 red; 3 blue, 5 green, 13 red; 6 red, 1 blue, 4 green; 16 red, 12 green"
# globalCount = 0
# for calibElement in f.split('\n'):
#     splittedList = calibElement.split(":")
#     gameId = int(splittedList[0].split(" ")[-1])
#     validGame = True
#     revealList = splittedList[-1]
#     CubesFromReveal = re.split(r'[;,]',revealList)
#     for cubes in CubesFromReveal:
#         splittedCube = cubes.strip().split(" ")
#         if (splittedCube[-1] == "red" and int(splittedCube[0]) > 12):
#             validGame = False
#             break
#         elif (splittedCube[-1] == "green" and int(splittedCube[0]) > 13): 
#                 validGame = False
#                 break
#         else:
#             if int(splittedCube[0]) > 14: 
#                 validGame = False
#                 break
#     print ("gameId: "+str(gameId)+"| Liste: "+str(CubesFromReveal)+" |validGame: "+str(validGame))
#     if (validGame):
#         globalCount += gameId

# print(globalCount)

##############################################Daytwo - part#2 ############################################################

# stringExampleList = (
#     "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
#     "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
#     "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
#     "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
#     "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"
# )
globalCount = 0
for calibElement in f.split('\n'):
    splittedList = calibElement.split(":")
    gameId = int(splittedList[0].split(" ")[-1])
    revealList = splittedList[-1]
    CubesFromReveal = re.split(r'[;,]',revealList)
    minRed = 0
    minGreen = 0
    minBlue = 0
    power = 0
    for cubes in CubesFromReveal:
        splittedCube = cubes.strip().split(" ")
        if (splittedCube[-1] == "red" and int(splittedCube[0]) > minRed):
            minRed = int(splittedCube[0])
        if (splittedCube[-1] == "green" and int(splittedCube[0]) > minGreen): 
            minGreen = int(splittedCube[0])
        if (splittedCube[-1] == "blue" and int(splittedCube[0]) > minBlue): 
            minBlue = int(splittedCube[0])
    power = minRed*minGreen*minBlue
    globalCount += power

print(globalCount)

# powerSum = 0
# sum = 0
# # with open('day2.txt') as input:
# for line in f.split('\n'):
#     game = line.strip().split(':')
#     moves = game[1].split(';')
#     gameID = int(game[0].strip().split(' ')[1])
#     minRed = 0
#     minGreen = 0
#     minBlue = 0
#     for move in moves:
#         pieces = move.strip().split(',')
#         for piece in pieces:
#             count = int(piece.strip().split(' ')[0])
#             color = piece.strip().split(' ')[1]
#             if color == 'red' and count > minRed:
#                 minRed = count
#             if color == 'blue' and count > minBlue:
#                 minBlue = count
#             if color == 'green' and count > minGreen:
#                 minGreen = count	
#     if minGreen <= 13 and minBlue <= 14 and minRed <= 12:
#         sum += gameID
#     power = minRed * minGreen * minBlue
#     powerSum += power

# print(f'Part 1 = {sum}')
# print(f'Part 2 = {powerSum}')