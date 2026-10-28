name = "Leo"
message = f"Hello, {name}!"
print(message)

shot = 12
print(shot)
print(type(shot))

print(shot + 5)

# shot = "myShot"
# print(shot)
# print(type(shot))

# print(shot + 5)


myList = ["shot01", "shot02", "shot03"]
print(myList)
myIntList = [10, 13, 18, 10]
print(myIntList)

myTuple = (10, 13, 18, 10)
print(myTuple)

mySet = {10, 13, 18, 10}
print(mySet)

frame = 150

if frame > 100:
    cache = "late"
    if frame < 200:
        cache = "mid"
else:
    cache = "early"

print(cache)

shots = ["shot01", "shot02", "shot03"]
print(shots)

for shot in shots:
    print(f"Processing {shot}...")
    # DOING SOME OTHER SHOT SPECIFIC WORK

print("Done processing all shots.")


def image_name(shot: str, frame: int) -> str:
    padded_frame = str(frame).zfill(4)
    return f"{shot}_{padded_frame}.exr"


print(image_name("sh010", 15))
print(image_name("sh010", 150))
print(image_name("sh010", 1001))

# here i import my library
from pathlib import Path

# file_path = Path("data/output.json")
file_path = Path("docs/README.md")
print(file_path.name)
print(file_path.exists())
