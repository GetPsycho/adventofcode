import os
# --- Jour 1 : Trebuchet ?! ---
# Quelque chose ne va pas dans la production mondiale de neige, et vous avez été choisi pour y jeter un coup d'œil. 
# Les Elfes t'ont même remis une carte sur laquelle ils ont indiqué, à l'aide d'étoiles, les cinquante endroits les plus susceptibles de connaître des problèmes.

# Tu fais ce travail depuis assez longtemps pour savoir que pour rétablir les opérations d'enneigement, tu dois vérifier les cinquante étoiles avant le 25 décembre.

# Récupérez des étoiles en résolvant des énigmes. Deux énigmes seront disponibles chaque jour du calendrier de l'Avent ;
# la deuxième énigme sera débloquée lorsque vous aurez terminé la première. Chaque énigme donne droit à une étoile. Bonne chance !

# Vous essayez de demander pourquoi ils ne peuvent pas utiliser une machine météorologique ("pas assez puissante"), 
# où ils vous envoient ("le ciel"), pourquoi votre carte est presque vide ("vous posez beaucoup de questions") et attendez, 
# vous venez de dire le ciel ("bien sûr, d'où pensez-vous que vient la neige") 
# quand vous réalisez que les elfes vous chargent déjà dans un trébuchet ("s'il vous plaît, ne bougez pas, nous devons vous attacher").

# Alors qu'ils procèdent aux derniers ajustements, ils découvrent que leur document d'étalonnage (votre entrée dans le puzzle) 
# a été modifié par une très jeune Elfe qui était apparemment juste ravie de montrer ses talents artistiques. 
# Par conséquent, les Elfes ont du mal à lire les valeurs sur le document.


# Le document d'étalonnage nouvellement amélioré se compose de lignes de texte ; 
# chaque ligne contenait à l'origine une valeur d'étalonnage spécifique que les Elfes doivent maintenant récupérer. 
# Sur chaque ligne, la valeur d'étalonnage peut être trouvée en combinant le premier chiffre et le dernier chiffre (dans cet ordre) pour former un seul nombre à deux chiffres.

# Par exemple :

# 1abc2
# pqr3stu8vwx
# a1b2c3d4e5f
# treb7uchet
# Dans cet exemple, les valeurs d'étalonnage de ces quatre lignes sont 12, 38, 15 et 77. En les additionnant, on obtient 142.

# Considérez l'ensemble de votre document d'étalonnage. Quelle est la somme de toutes les valeurs d'étalonnage ?

##############################################Dayone - part#1 ############################################################
# f = open("C:\\Users\\erifontaine\\repopo\\adventofcode\\2023\\input.txt", "r").read().strip()

#import + read the file
work_folder = os.getcwd()
input_relative_path = "2023/input_day_01.txt"
input_absolute_path = os.path.join(work_folder,input_relative_path)
f = open(input_absolute_path, "r").read().strip()

# countGlobal = 0
# for calibElement in f.split('\n'):
#     digitList = []
#     countPerCharElem = 0
#     for charElem in calibElement:
#         if charElem.isdigit():
#             digitList.append(int(charElem))
#     countPerCharElem = str(digitList[0]) + str(digitList[len(digitList)-1])
#     countGlobal += int(countPerCharElem)
# print("resultat: "+ str(countGlobal))



##############################################Dayone - part#2 ############################################################
# calibrationExampleList = (
# "two1nine",
# "eightwothree",
# "abcone2threexyz",
# "xtwone3four",
# "4nineeightseven2",
# "zoneight234",
# "7pqrstsixteen"
# )

# f = open("C:\\Users\\erifontaine\\repopo\\adventofcode\\2023\\input.txt", "r").read().strip()
# letters = ("one","two","three","four","five","six","seven","eight","nine")
# countGlobal = 0
# for calibElement in f.split('\n'):
# # for calibElement in calibrationExampleList:
#     print(calibElement)
#     digitList = []

#     for indice, charElem in enumerate(calibElement):
#         if charElem.isdigit():
#             digitList.append(int(charElem))
#         else:
#             for letterElem in letters:
#                 if(letterElem == calibElement[indice:indice+len(letterElem)]):
#                     digitList.append(letters.index(letterElem)+1)
#                     break

#     print(digitList)
#     countGlobal += int(str(digitList[0])+str(digitList[-1]))
#     print("valeur courante:"+ str(int(str(digitList[0])+str(digitList[-1]))))
#     print("countGlobal: "+str(countGlobal))



