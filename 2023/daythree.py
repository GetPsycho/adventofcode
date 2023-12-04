


import re
f = open(r"C:\Users\erifontaine\repopo\adventofcode\2023\input_daythree.txt", "r").read().strip()
#determiner le nb de lignes et colonnes du tableau à remplir
splitFile = f.split("\n")
lineNumber = len(splitFile)
StringLength = len(splitFile[0])

array2Dempty = [["."] * StringLength for _ in range(lineNumber)]

for indiceLine, elemLine in enumerate(f.split("\n")):
    for indiceCol, elemChar in enumerate(elemLine):
        print(indiceCol)
        print(elemChar)
        array2Dempty[indiceLine][indiceCol] = elemChar

print(array2Dempty)


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
# globalCount = 0
# for calibElement in f.split('\n'):
#     splittedList = calibElement.split(":")
#     gameId = int(splittedList[0].split(" ")[-1])
#     revealList = splittedList[-1]
#     CubesFromReveal = re.split(r'[;,]',revealList)
#     minRed = 0
#     minGreen = 0
#     minBlue = 0
#     power = 0
#     for cubes in CubesFromReveal:
#         splittedCube = cubes.strip().split(" ")
#         if (splittedCube[-1] == "red" and int(splittedCube[0]) > minRed):
#             minRed = int(splittedCube[0])
#         if (splittedCube[-1] == "green" and int(splittedCube[0]) > minGreen): 
#             minGreen = int(splittedCube[0])
#         if (splittedCube[-1] == "blue" and int(splittedCube[0]) > minBlue): 
#             minBlue = int(splittedCube[0])
#     power = minRed*minGreen*minBlue
#     globalCount += power

# print(globalCount)