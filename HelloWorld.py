"""
My Module

Some Base Python Introduction
"""

import json

print("Hello World")

varA = 1.0
varA *= 2
varA = varA + 1  # varA += 1

print(f"Our Variable is: {varA}")

# dictionary (dict)
json_data = {
    "name": "Jonas",
    "age": 30,
}

json_data["age"] = 31

for i in range(100):
    json_data[f"key_{i}"] = f"value_{i}"
    # print(f"i is: {i}")

# write out our python data set
with open("D:/Documents/DATA/myData.json", "w") as f:
    json.dump(json_data, f, indent=4)

# print(json_data)
