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

shot = {
    "name": "sh010",
    "frames": [1001, 1050],
    "status": "work in progress",
}

print("Shotname is: " + shot.get("name"))
print("Shot status is: " + shot.get("status"))
shot["status"] = "done"
print("Shot status is: " + shot.get("status"))

if "fps" in shot:
    print(f"Shot fps is: {shot['fps']}")

print(f"Shot fps is: {shot.get('fps', 24)}")

my_shot_list = ["sh010", "sh011", "sh012"]

for counter, my_shot in enumerate(my_shot_list):
    print(f"{counter}. {my_shot}")

for counter in range(10):
    print(f"Counter is: {counter}")

shots = [
    {"name": "sh010", "status": "done"},
    {"name": "sh011", "status": "work in progress"},
    {"name": "sh012", "status": "work in progress"},
    {"name": "sh013", "status": "done"},
]

done_shots = [shot["name"] for shot in shots if shot["status"] == "done"]
print(done_shots)


project = "my_project"


def build_name(shot: str):
    suffix = "final"
    print(suffix)
    return f"{project}_{shot}_{suffix}"


print(build_name("sh010"))
# print(suffix)

# MAIN CODE
from myModule.myHelperFunction import myFunc

#  print(myFunc(0))

from myModule.shot import Shot

shot_a = Shot("sh010")
print(shot_a.label())
shot_b = Shot("sh020", status="work in progress")
print(shot_b.label())

shot_a.status = "done"
print(shot_a.label())
print(shot_a.all_frames())
