import os
import json

path = os.getcwd()


folder = os.path.join(path, "student")
filename = os.path.join(folder, "student.json")

if not os.path.exists(folder):
    
    os.makedirs(folder)


def load_json():


    if os.path.exists(filename):
        
        with open(filename, 'r') as file:
            
            content = file.read()

            if content.strip(): 
                     
                return json.loads(content)
            else:
                return []         

    else:
        return []                   


def write_file(existing_data):
    

    with open(filename, 'w') as file:
        json.dump(existing_data, file, indent=4)
