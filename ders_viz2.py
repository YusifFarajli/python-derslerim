import matplotlib.pyplot as plt

# --- 1. Sütunlu Diaqram (Bar Chart) nümunəsi ---
mehsullar = ["Alma", "Banan", "Gilas", "Nar"]
satislar = [15, 30, 20, 25]

fig, ax = plt.subplots()

# Sütunlu qrafik çəkirik
ax.bar(mehsullar, satislar, color="orange", width=0.6)

ax.set_title("Meyvə Satışları")
ax.set_xlabel("Meyvələr")
ax.set_ylabel("Satış Miqdarı")

# Qrafiki göstəririk
plt.show()