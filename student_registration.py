import os
import json
import uuid
import file_reader

path=os.getcwd()

filename=r"student\student.json"
filename=os.path.join(path,filename)


existing_data= file_reader.load_json()
def register():

   

         
   data = {}
   data["id"]= uuid.uuid4().hex[:6]
   data["name"]=input("please enter name :")
   data["address"]=input("enter address :")

   while True:
      contact= input("enter 10 digit contact number:")

      if len(contact)==10 and contact.isdigit():
          data["contact"]=contact
          break
      else:
         print("invalid number please re enter your 10-digit contact number :\n")

   existing_data.append(data)

   file_reader.write_file(existing_data)

   print("\n***registration successful***\n")

def view_all_student():
   
   data=existing_data

   if not data:
      print("\nno record found\n")

      return
   
   print("\n======all student=========\n")
   for st in data:
      for k,v in st.items():

         print(f"{k} --> {v}")
   
def search_student():
   data=existing_data
   if not data:
     print("\nNo records found!\n")
     return

   student_id=input("enter student id to search:")
   for st in data:
      if st["id"]==student_id:
         print("student found")
         for k,v in st.item():
            print(f"{k}--{v}")
         return
   print("\n student not found")
def delete_student():
   data=existing_data
   if not data:
     print("\nNo records found!\n")
     return
   sid=input("enter student id to delete")
   for st in data:
      if st["id"] == sid:
            data.remove(st)
            file_reader.write_file(data)
            print("\n*** Student Deleted Successfully ***\n")
            return
      print("\nStudent Not Found!\n")
   