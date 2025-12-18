import json
import os

class Crud:
    def __init__(self):
        self.file = "database\\data.json"

    def load(self):
        if os.path.exists(self.file):
            with open(self.file, "r") as f:
                return json.load(f)
        return []

    def save(self, data):
        with open(self.file, "w") as f:
            json.dump(data, f, indent=4)

    def create(self, id, name):
        data = self.load()
        data.append({"id": id, "name": name})
        self.save(data)
        print("Data Added")

    def read(self):
        for d in self.load():
            print(d)

    def update(self, id, new_name):
        data = self.load()
        for d in data:
            if d["id"] == id:
                d["name"] = new_name
                self.save(data)
                print("Data Updated")
                return
        print("ID Not Found")

    def delete(self, id):
        data = self.load()
        for d in data:
            if d["id"] == id:
                data.remove(d)
                self.save(data)
                print("Data Deleted")
                return
        print("ID Not Found")

