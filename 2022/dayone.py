
# Les rennes du Père Noël mangent généralement de la nourriture normale, 
# mais ils ont besoin de beaucoup d'énergie magique pour distribuer les cadeaux à Noël. 
# Pour cela, leur en-cas préféré est un fruit étoilé spécial qui ne pousse que dans les profondeurs de la jungle. 
# Les lutins t'ont emmené dans leur expédition annuelle jusqu'au bosquet où pousse ce fruit.

# Pour fournir suffisamment d'énergie magique, l'expédition doit récupérer un minimum de cinquante étoiles avant le 25 décembre. 
# Bien que les elfes vous assurent que le bosquet regorge de fruits, vous décidez d'attraper tous les fruits que vous verrez en chemin, juste au cas où.

# Collectez des étoiles en résolvant des énigmes. 
# Deux énigmes seront disponibles chaque jour du calendrier de l'Avent ; l'énigme suivante sera débloquée lorsque vous aurez terminé la première. 
# Chaque énigme donne droit à une étoile. Bonne chance !

# La jungle doit être trop envahie et difficile à parcourir en véhicule ou à atteindre depuis les airs ; 
# l'expédition des Elfes se fait traditionnellement à pied. Alors que vos bateaux approchent de la terre, 
# les Elfes commencent à faire l'inventaire de leurs provisions. La nourriture est un élément important à prendre en compte, 
# en particulier le nombre de calories que chaque lutin transporte (votre contribution au puzzle).

# À tour de rôle, les lutins notent le nombre de calories contenues dans les divers repas, en-cas, rations, etc. 
# qu'ils ont emportés avec eux, un élément par ligne. Chaque lutin sépare son propre inventaire de celui du lutin précédent (s'il y en a un) par une ligne blanche.

# Par exemple, supposons que les lutins finissent d'écrire les calories de leurs objets et obtiennent la liste suivante :
# 1000
# 2000
# 3000

# 4000

# 5000
# 6000

# 7000
# 8000
# 9000

# 10000

# Cette liste représente les calories de la nourriture transportée par cinq Elfes :

# Le premier lutin transporte des aliments contenant 1000, 2000 et 3000 calories, soit un total de 6000 calories.
# Le deuxième lutin transporte un aliment de 4000 calories.
# Le troisième lutin transporte des aliments contenant 5000 et 6000 calories, soit un total de 11000 calories.
# Le quatrième lutin transporte des aliments contenant 7000, 8000 et 9000 calories, soit un total de 24000 calories.
# Le cinquième lutin transporte un aliment contenant 10000 calories.
# Au cas où les lutins auraient faim et auraient besoin d'une collation supplémentaire, ils doivent savoir à quel lutin s'adresser : ils aimeraient savoir combien de calories est transporté par le lutin qui transporte le plus de calories. Dans l'exemple ci-dessus, il s'agit de 24 000 (portées par le quatrième lutin).

# Trouvez le lutin qui transporte le plus de calories. Combien de calories totales ce lutin transporte-t-il ?























# def find_max_calories(input_text):
#     # Split the input into lists of Calories for each Elf
#     elves_calories = [list(map(int, group.split())) for group in input_text.strip().split('\n\n')]

#     # Calculate the total Calories for each Elf
#     total_calories_per_elf = [sum(calories) for calories in elves_calories]

#     # Find the Elf with the highest total Calories
#     max_calories_index = total_calories_per_elf.index(max(total_calories_per_elf))

#     # Output the result
#     max_calories = total_calories_per_elf[max_calories_index]
#     print(f"The Elf carrying the most Calories is Elf {max_calories_index + 1} with {max_calories} Calories.")

# # Example usage with the provided input
# input_text = """
# 1000
# 2000
# 3000

# 4000

# 5000
# 6000

# 7000
# 8000
# 9000

# 10000
# """

# find_max_calories(input_text)