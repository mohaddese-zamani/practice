import json
import os

def title_json():

    open_file = os.path.join(os.path.expanduser("~"), "Desktop", "home-page.txt")
    if not os.path.exists(open_file):
        print("فایل مورد نظر پیدا نشد:", open_file)
    else:
        try:
            with open(open_file, "r", encoding="utf-8") as file:
                reade_file = json.load(file)

            for title_file in reade_file.get("posts", []):
                print(title_file.get("title"))
        except json.JSONDecodeError:
            print("خطا در خواندن فایل JSON")

title_json()
