import pandas as pd

Data_set =pd.DataFrame([
    {"name": "Ali", "age": 25, "income": 3000},
    {"name": "Sara", "age": 30, "income": 7000},
    {"name": "Reza", "age": 22, "income": 2000},
    {"name": "Mina", "age": 28, "income": 3500},
    {"name": "Nima", "age": 26, "income": 7000},
    {"name": "Zahra", "age": 33, "income": 6000},
    {"name": "Peyman", "age": 24, "income": 4200},
    {"name": "Fatemeh", "age": 29, "income": 4200},
    {"name": "Mohammad", "age": 31, "income": 5500},
    {"name": "Leila", "age": 27, "income": 3700},
    {"name": "Kian", "age": 27, "income": 2200},
    {"name": "Samira", "age": 32, "income": 6500},
    {"name": "Ehsan", "age": 35, "income": 7000},
    {"name": "Roya", "age": 21, "income": 1800},
    {"name": "Morteza", "age": 30, "income": 5100},
    {"name": "Niloofar", "age": 27, "income": 4200},
    {"name": "Omid", "age": 26, "income": 4200},
    {"name": "Afsaneh", "age": 28, "income": 3400},
    {"name": "Hassan", "age": 31, "income": 5800},
    {"name": "Vahid", "age": 29, "income": 4200},
    {"name": "Shirin", "age": 34, "income": 6200},
    {"name": "Ali", "age": 25, "income": 3200},
    {"name": "Sima", "age": 32, "income": 6300},
    {"name": "Arash", "age": 27, "income": 2100},
    {"name": "Khadijeh", "age": 30, "income": 5100},
    {"name": "Ali", "age": 24, "income": 3300},
])
df = pd.DataFrame(Data_set)

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