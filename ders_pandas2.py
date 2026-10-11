import pandas as pd

# CSV faylını oxuyub DataFrame-ə çeviririk
df = pd.read_csv("telebeler.csv")

print("--- Cədvəlin İlk 3 Sətri ---")
print(df.head(3))  # Başlanğıcdan 3 sətri göstərir

print("\n--- Cədvəl Haqqında Ümumi Məlumat ---")
print(df.info())  # Sütun tipləri və boş sətir olub-olmadığını göstərir

print("\n--- Balı 85-dən Yuxarı Olan Tələbələr ---")
secilenler = df[df["Bal"] > 85]
print(secilenler)