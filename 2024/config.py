import os
import socket

# Récupérer le nom de l'ordinateur
computer_name = socket.gethostname()

#import + read the file
work_folder = os.getcwd()
if (computer_name == 'ETL-SOP-POR0196'):
    input_relative_path = "2024\\"
else:
    input_relative_path = "adventofcode\\2024\\"
    
input_absolute_path = os.path.join(work_folder,input_relative_path)