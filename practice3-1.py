import pandas as pd
import json 

def load_data(path):
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return pd.DataFrame(data) 


def show_Values(df):
    mean_age = df["age"].mean()
    mean_income = df["income"].mean()

    median_age = df["age"].median()
    median_income = df["income"].median()

    mode_age = df['age'].mode()[0] 
    mode_income = df['income'].mode()[0]  

    print(f"میانگین سن ها = {mean_age}")
    print(f"میانگین درآمد ها = {mean_income}")
    print(f"میانه سنین = {median_age}")
    print(f"میانه درآمد = {median_income}")
    print(f"مد سنین = {mode_age}")
    print(f"مد درآمد = {mode_income}")
    if mean_income > median_income:
        print("میانگین درآمد بیشتر از میانه است.")
    elif mean_income < median_income:
        print("میانه درآمد بیشتر از میانگین است.")
    else:
        print("میانگین و میانه درآمد برابر هستند.")

if __name__ == "__main__":
    df = load_data(r"E:\New folder\Git\project\practice\people.txt")
    show_Values(df)