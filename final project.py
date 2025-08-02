import json
import pandas as pd
from sklearn.tree import DecisionTreeClassifier


def read_jason():
    try:
        with open("E:/New folder/Git/project/practice/data.json", "r", encoding="utf-8") as f:
            data = json.load(f)
            return data
    except:
        print("مشکل در باز کردن فایل")
        return []


def new_products():
    products = [
        {"productName": "محصول A", "price": 17000000},
        {"productName": "محصول B", "price": 27000000},
        {"productName": "محصول C", "price": 12000000},
        {"productName": "محصول D", "price": 38000000}
    ]
    return products


def show_mean(data):
    df = pd.DataFrame(data)
    miangin = df["price"].mean()
    df["sold"] = df["price"] < miangin
    return df, miangin


def model_training(df):
    X = df[['price']]
    y = df['sold']
    model = DecisionTreeClassifier()
    model.fit(X, y)
    return model


def prediction(model, products, miangin):
    l = []
    for i in products:
        df = pd.DataFrame([i])
        pishbini = model.predict(df[['price']])[0]
        if pishbini == 1:
            result = "فروخته می‌شود"
        else:
            result = "فروخته نمی‌شود"
        if i["price"] < miangin:
            results = "← قیمت مناسب"
        else:
            results = "← قیمت بالا"
        final = f"{i['productName']} با قیمت {i['price']:,} → {result} {results}"
        print(final)
        l.append(final)
    return l


if __name__ == "__main__":
    data = read_jason()

    if data:
        print("محصولات موجود:")
        for d in data:
            print(f"{d['productName']}")

        print("\nقیمت محصولات:")
        for d in data:
            print(f"🛒 {d['productName']}: 💸 {d['price']:,}")        
        df, miangin = show_mean(data) 
        print(f"\nمیانگین قیمت: {miangin}\n")


        model = model_training(df)
        products = new_products()
        prediction(model, products, miangin)
