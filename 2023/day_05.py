import config

input_file = 'input_day_05.txt'
f = open(config.input_absolute_path+input_file, "r").read().strip()

#split line by line
for line_number, line in enumerate(f.split("\n")):
    
    #put the seeds into a data structure
    # print('line_number: '+ str(line_number)+ ' line:'+ str(line))
    if line.startswith('seeds'):
        split_seed_id = line.split(':')[1]
        print('seeds id: '+ str(split_seed_id))
    # for seed_id in split_seed_id.split():
    #     print('seed_id: '+ seed_id)
    if line.endswith('map:'):
        



