import pandas as pd

# Məlumatlarımızı lüğət (dictionary) şəklində təyin edirik
melumat = {
    "Ad": ["Ali", "Aysel", "Leyla", "Murad"],
    "Yaş": [22, 25, 23, 24],
    "İxtisas": ["CS", "Data Science", "IT", "Business"],
    "Bal": [85, 92, 78, 88]
}

# Bu məlumatı Pandas DataFrame-ə (cədvəle) çeviririk
df = pd.DataFrame(melumat)

# Cədvəli ekrana çap edirik
print("--- Tələbələr Cədvəli ---")
print(df)