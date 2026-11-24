import sys
import json

print(sys.version)

data = {}

with open("D:/Documents/DATA/myData.json", "r") as f:
    data = json.load(f)

data["name"] = "Some Other Name"

print(data)
