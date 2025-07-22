import pandas as pd

Titles = pd.DataFrame({
    'name': ['Ali', 'Barad', 'Mina', 'Mmd', 'Asghar'],
    'age': [25, 30, 22, 50, 18],
    'city': ['Shiraz', 'Mashhad', 'Tehran', 'Rasht', 'Tabriz'],
    'income': [800, 500, 200, 400, 700],
    'job': ['farmer', 'tailor', 'baker', 'coach', 'fireman']
})

vam = Titles[(Titles['income'] >= 500) & (Titles['age'] >= 25)]

print(vam)