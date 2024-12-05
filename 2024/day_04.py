import config


input_file = 'input_day_04.txt'

with open(config.input_absolute_path+input_file, 'r') as f:
    puzzle_input = f.read()


def part1(puzzle_input):
    splitFile = puzzle_input.split("\n")
    lineNumber = len(splitFile)
    StringLength = len(splitFile[0])
    print("lineNumber: ", lineNumber)
    print("StringLength: ", StringLength)
    XMAS_Count = 0

    #create the empty 2d array
    array2D = [["."] * StringLength for _ in range(lineNumber)]

    #populate the 2d array
    for indiceLine, elemLine in enumerate(puzzle_input.split("\n")):
        for indiceCol, elemChar in enumerate(elemLine):
            array2D[indiceLine][indiceCol] = elemChar
    
    for y, arLine in enumerate(array2D):
        print("arLine: "+ str(arLine))
        for x, arCharELem in enumerate(arLine):
            limite_ligne_a_droite = (x <= len(arLine)-4)
            limite_ligne_a_gauche = x >= 3
            limite_colonne_en_bas = (y <= lineNumber-4)
            limite_colonne_en_haut = (y >= 3)
            if(arCharELem == "X"):
                # en ligne droite
                if(limite_ligne_a_droite):
                    if(str(arLine[x+1])+str(arLine[x+2])+str(arLine[x+3])== "MAS"):
                        XMAS_Count = XMAS_Count + 1
                # en ligne gauche
                if(limite_ligne_a_gauche):
                    if(str(arLine[x-1])+str(arLine[x-2])+str(arLine[x-3])== "MAS"):
                        XMAS_Count = XMAS_Count + 1
                # en colonne bas
                if(limite_colonne_en_bas):
                    if(str(array2D[y+1][x])+str(array2D[y+2][x])+str(array2D[y+3][x])== "MAS"):
                        XMAS_Count = XMAS_Count + 1
                # en colonne haut
                if(limite_colonne_en_haut):
                    if(str(array2D[y-1][x])+str(array2D[y-2][x])+str(array2D[y-3][x])== "MAS"):
                        XMAS_Count = XMAS_Count + 1
                # diagonale droite + bas
                if(limite_ligne_a_droite and limite_colonne_en_bas):
                    if(str(array2D[y+1][x+1])+str(array2D[y+2][x+2])+str(array2D[y+3][x+3])== "MAS"):
                        XMAS_Count = XMAS_Count + 1
                # diagonale gauche + bas
                if(limite_ligne_a_gauche and limite_colonne_en_bas):
                    if(str(array2D[y+1][x-1])+str(array2D[y+2][x-2])+str(array2D[y+3][x-3])== "MAS"):
                        XMAS_Count = XMAS_Count + 1
                # diagonale droite + haut
                if(limite_ligne_a_droite and limite_colonne_en_haut):
                    if(str(array2D[y-1][x+1])+str(array2D[y-2][x+2])+str(array2D[y-3][x+3])== "MAS"):
                        XMAS_Count = XMAS_Count + 1
                # diagonale gauche + haut
                if(limite_ligne_a_gauche and limite_colonne_en_haut):
                    if(str(array2D[y-1][x-1])+str(array2D[y-2][x-2])+str(array2D[y-3][x-3])== "MAS"):
                        XMAS_Count = XMAS_Count + 1
                
    return(XMAS_Count)


def part2(puzzle_input):
    splitFile = puzzle_input.split("\n")
    lineNumber = len(splitFile)
    StringLength = len(splitFile[0])
    print("lineNumber: ", lineNumber)
    print("StringLength: ", StringLength)
    XMAS_Count = 0

    #create the empty 2d array
    array2D = [["."] * StringLength for _ in range(lineNumber)]

    #populate the 2d array
    for indiceLine, elemLine in enumerate(puzzle_input.split("\n")):
        for indiceCol, elemChar in enumerate(elemLine):
            array2D[indiceLine][indiceCol] = elemChar
    
    for y, arLine in enumerate(array2D):
        print("arLine: "+ str(arLine))
        for x, arCharELem in enumerate(arLine):
            limite_ligne_a_droite = (x <= len(arLine)-3)
            limite_colonne_en_bas = (y <= lineNumber-3)
            if(limite_ligne_a_droite and limite_colonne_en_bas):
                slash = arCharELem+array2D[y+1][x+1]+array2D[y+2][x+2]
                antislash = array2D[y][x+2]+array2D[y+1][x+1]+array2D[y+2][x]
                if((slash=="SAM" or slash=="MAS") and (antislash=="SAM" or antislash=="MAS")):
                    XMAS_Count = XMAS_Count + 1

    return(XMAS_Count)


# print('Part 1:', part1(puzzle_input))
print('Part 2:', part2(puzzle_input))


