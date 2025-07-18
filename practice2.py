import json
import os

json_file = os.path.join(os.path.expanduser("~"), "Desktop", "home-page.txt")
read_file = {}

def open_json():
    if not os.path.exists(json_file):
        print("فایل مورد نظر پیدا نشد:", json_file)
        return False

def read_json():
    global read_file
    try:
        with open(json_file , "r", encoding="utf-8") as file:
            read_file = json.load(file)
        return True
    except json.JSONDecodeError:
        print("خطا در خواندن فایل JSON")
        return False

def title():
    for title_file in read_file.get("posts", []):
        print(title_file.get("title"))    

def captions_file():
    captions = 0
    for caption in read_file["posts"]:
        captions += len(caption["caption"])
    print(captions)

def name():
    name_file = read_file.get("posts", [])
    count = sum(1 for post in name_file if "name" in post.get("author", {}))
    print(count)


open_json()
read_json()
print("\n:عنوان های فایل")
title()
print("\nمجموع کپشن های فایل")
captions_file()
print("\nمجموع تعداد نویسندگان فایل")
name()

