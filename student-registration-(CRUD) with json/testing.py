import os

path = (str(os.getcwd())+r"\file_handing\tara.txt")
# path = path.replace("\","\\")
 # path = r"file_handling\tara.txt"
print(path)

with open(path,'r')as file:
    data=file.read()
print(data)

