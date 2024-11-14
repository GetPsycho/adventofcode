import config

input_file = 'input_day_05.txt'
f = open(config.input_absolute_path+input_file, "r").read().strip()

current_list_id = -1
lists_of_maps = []

# initializations of lists
for i in range(7):
    lists_of_maps.append([])

#split file line by line
for line_number, line in enumerate(f.split("\n")):
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

# print("split_seed_id: ",string_seed_id)

location_list = []
# now for each seed id we go from map to map to find the location
for seed_number, seed_id in enumerate(string_seed_id.strip().split(" ")):
    # print("seed id: ", line_number)
    travelling_id = int(seed_id)
    for map_number, map_data in enumerate(lists_of_maps):
        for dico_number, dico_data in enumerate (map_data):
            destination = int(dico_data["dest"])
            source = int(dico_data["source"])
            length = int(dico_data["length"])
            print(" seed_id: ",travelling_id)
            print(" source+length-1: ",source+length-1)
            print(" source: ",source)
            if( travelling_id <= source+length-1 and  travelling_id >= source ):
                travelling_id = travelling_id - source + destination
                print("travelling_id", travelling_id)
                break
            else:
                print("PAS DANE L'RANGE")
    location_list.append(travelling_id)
print("location_list: ",location_list)
print("lowest location:", min(location_list))





