import config

input_file = 'input_day_05.txt'
filter = open(config.input_absolute_path+input_file, "r").read().strip()

current_list_id = -1
lists_of_maps = []

# initializations of lists
for i in range(7):
    lists_of_maps.append([])

#split file line by line
for line_number, line in enumerate(filter.split("\n")):
    # print('line number:',line_number,' | line content: ', line)

    #put the seeds into a data structure
    if line.startswith('seeds'):
        string_seed_id = line.split(':')[1]
        continue
    #put the maps into list of lists
    if line.endswith('map:'):
        current_list_id = current_list_id+1
        # print("nouvelle map")
        continue
    if line.strip() == "":
        continue
    else:
        dico = {"dest":line.split(" ")[0], "source":line.split(" ")[1], "length":line.split(" ")[2]}
        lists_of_maps[current_list_id].append(dico)

print("split_seed_id: ",string_seed_id)

#Day 5 - Part 2
seed_list_length = []
seed_list_start = []

for seed_order, seed_data in enumerate(string_seed_id.strip().split(" ")):
    if(seed_order==0 or seed_order%2==0): 
        seed_list_start.append(int(seed_data))
    else:
        seed_list_length.append(int(seed_data))

print("seed_list_start: ", seed_list_start)
print("seed_list_length: ", seed_list_length)


# avec un premier range je connais la premiere fourchette 
# et j'ajoute tous les nombre dans la liste finale
# deuxieme boucle:
# si est dans le range precedent:
# on regarde si son range est dedans
# = on fait Rien 
# si ca depasse: on ajoute ce qui depasse
# si il est plus bas:
# on regarde son range et on determine ce qu'il faut ajouter (= ce qui depasse)'
# si plus haut:
# meme chose
# les differents cas:
# separé, dessous
# separé, dessus
# joint, dessous
# joint dessus
# dedans
lowest_location_list = 0
seed_list_final = set()
for seed_start_order, seed_start_data in enumerate(seed_list_start):
    print("seed_start_order: ",seed_start_order)
    for i in range(int(seed_list_length[seed_start_order])):
        # seed_list_final.add(seed_start_data+i)
        # seed_list_final.append(int(seed_start_data)+i)

# now for each seed id we go from map to map to find the location
# for seed_id in seed_list_final:
        # print("seed id: ", line_number)
        # travelling_id = int(seed_id)
        travelling_id = seed_start_data+i
        for map_number, map_data in enumerate(lists_of_maps):
            for dico_number, dico_data in enumerate (map_data):
                destination = int(dico_data["dest"])
                source = int(dico_data["source"])
                length = int(dico_data["length"])
                # print(" seed_id: ",travelling_id)
                # print(" source+length-1: ",source+length-1)
                # print(" source: ",source)
                if( travelling_id <= source+length-1 and  travelling_id >= source ):
                    travelling_id = travelling_id - source + destination
                    # print("travelling_id", travelling_id)
                    break
        if travelling_id < lowest_location_list:
            lowest_location_list = travelling_id
    # location_list.append(travelling_id)
# print("location_list: ",location_list)
# print("lowest location:", min(location_list))
print("lowest location:", lowest_location_list)


# Chargement des données
# with open("/mnt/data/input_day5.txt", "r") as file:
#     lines = file.readlines()
# input_file = 'input_day_05.txt'
# lines = open(config.input_absolute_path+input_file, "r").readlines() 

# # Extraction des plages de graines
# seeds_line = next(line for line in lines if line.startswith("seeds:"))
# seed_ranges = list(map(int, seeds_line.split(":")[1].split()))

# # Création des graines individuelles à partir des plages
# def generate_seeds(seed_ranges):
#     for i in range(0, len(seed_ranges), 2):  # Parcourir les paires (start, length)
#         start, length = seed_ranges[i], seed_ranges[i + 1]
#         for seed in range(start, start + length):
#             yield seed  # Générer chaque graine une par une

# # Extraction des maps
# def extract_map(section_name):
#     start = lines.index(f"{section_name}\n") + 1
#     end = next((i for i, line in enumerate(lines[start:], start=start) if line.strip() == ""), len(lines))
#     return [tuple(map(int, line.split())) for line in lines[start:end]]

# seed_to_soil_map = extract_map("seed-to-soil map:")
# soil_to_fertilizer_map = extract_map("soil-to-fertilizer map:")
# fertilizer_to_water_map = extract_map("fertilizer-to-water map:")
# water_to_light_map = extract_map("water-to-light map:")
# light_to_temperature_map = extract_map("light-to-temperature map:")
# temperature_to_humidity_map = extract_map("temperature-to-humidity map:")
# humidity_to_location_map = extract_map("humidity-to-location map:")

# # Fonction pour transformer une valeur selon une map
# def transform(value, mapping):
#     for dest_start, src_start, length in mapping:
#         if src_start <= value < src_start + length:
#             return dest_start + (value - src_start)
#     return value  # Si non trouvé, la valeur reste inchangée

# # Trouver la plus petite localisation
# lowest_location = float('inf')  # Initialiser avec l'infini

# for seed in generate_seeds(seed_ranges):
#     soil = transform(seed, seed_to_soil_map)
#     fertilizer = transform(soil, soil_to_fertilizer_map)
#     water = transform(fertilizer, fertilizer_to_water_map)
#     light = transform(water, water_to_light_map)
#     temperature = transform(light, light_to_temperature_map)
#     humidity = transform(temperature, temperature_to_humidity_map)
#     location = transform(humidity, humidity_to_location_map)
#     lowest_location = min(lowest_location, location)  # Garder le minimum

# print("La plus petite localisation est :", lowest_location)





