import json
import os

open_file = os.path.join(os.path.expanduser("~"), "Desktop", "home-page.txt")

with open(open_file, "r", encoding="utf-8") as file:
    reade_file = json.load(file)

for title_file in reade_file.get("posts", []):
    print(title_file.get("title"))