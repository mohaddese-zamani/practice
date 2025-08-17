import pandas as pd
import json

def load_data(path):
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return pd.DataFrame(data) 


def show_values(df):
    ali_count = len(df[df['name'] == 'Ali'])
    print(f"تعداد نام علی = {ali_count}")


    median_income = df["income"].median()
    comparison = (df['income'] == median_income).sum()
    print(f"تعداد افرادی که درآمدشان با مقدار میانه برابر است = {comparison}")

    mode_age = df['age'].mode()[0] 
    age_count = len(df[df['age'] == mode_age])
    print(f"سن {mode_age} تعداد {age_count} تکرار شده است.")

if __name__ == "__main__":
    df = load_data(r"E:\New folder\Git\project\practice\people.txt")
    show_values(df)