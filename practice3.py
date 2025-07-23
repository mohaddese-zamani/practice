import pandas as pd

Data_set = pd.DataFrame({
    'name': ['Ali', 'Barad', 'Mina', 'Mmd', 'Asghar'],
    'age': [25, 30, 22, 50, 18],
    'city': ['Shiraz', 'Mashhad', 'Tehran', 'Rasht', 'Tabriz'],
    'income': [800, 500, 200, 400, 700],
    'job': ['farmer', 'tailor', 'baker', 'coach', 'fireman']
})

def filters(ds):
    Jobs_filter = ds['job'].isin(['farmer', 'fireman'])
    Age_filter = ds['age'] <= 40
    income_filter = ds['income'] >= 500

    finall_filters = ds[Jobs_filter & Age_filter & income_filter]
    return finall_filters.sort_values('income', ascending=False)[['name', 'job', 'income']]

finall_filters = filters(Data_set)
print(finall_filters)