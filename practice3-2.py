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

ali_count = len(df[df['name'] == 'Ali'])
print(f"تعداد نام علی = {ali_count}")


median_income = df["income"].median()
comparison = (df['income'] == median_income).sum()
print(f"تعداد افرادی که درآمدشان با مقدار میانه برابر است = {comparison}")


mode_age = df['age'].mode()[0] 
age_count = len(df[df['age'] == 27])
print(f"سن {mode_age} تعداد {age_count} تکرار شده است.")

