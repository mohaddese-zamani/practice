import json
import os

json_file = input("مسیر فایل را وارد کنید: \n")
# E:\New folder\Git\project\practice\home.txt


def open_json():
    if os.path.exists(json_file):
            return True
    else:
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
    for title_file in read_file.get("posts"):
        print(title_file.get("title"))    

def captions_file():
    cap = 0
    for captions in read_file["posts"]:
        cap += len(captions["caption"])
    print(cap)

def name():
    name_file = read_file.get("posts")
    tedad = 0
    for i in name_file:
        x = i.get("author")
        if "name" in x:
            tedad += 1
    print(tedad)


if __name__ == "__main__":
    if not open_json():
        exit()
    if not read_json():
        exit()
    print("\n:عنوان های فایل")
    title()
    print("\nمجموع کپشن های فایل")
    captions_file()
    print("\nمجموع تعداد نویسندگان فایل")
    name()
