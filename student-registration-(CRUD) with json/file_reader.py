import os
import json
path=os.getcwd()

filename=r"student\student.json"
filename=os.path.join(path,filename)

def load_json():

    
    
    if os.path.exists(filename):
        with open(filename,'r') as file:
           content=file.read()
           if content:
              existing_data= json.loads(content)
           else:
              existing_data= []

    else:
       existing_data= []

    return existing_data
 
 
def write_file(existing_data):
   
   with open(filename,'w') as file:
      json.dump(existing_data,file,indent=4)