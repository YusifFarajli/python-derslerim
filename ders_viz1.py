import matplotlib.pyplot as plt

# X və Y oxu üçün rəqəmlər təyin edirik
x = [1, 2, 3, 4]
y = [1, 4, 9, 16]

# Figure və Axes obyektlərini yaradırıq
fig, ax = plt.subplots()

# Xətti qrafik çəkirik (stilizasiya ilə)
ax.plot(x, y, color="red", linestyle="--", marker="o", linewidth=2, label="Kvadratlar")

# Başlıq və oxların adlarını qoyuruq
ax.set_title("Kvadrat Ədədlər Qrafiki")
ax.set_xlabel("Nömrə (X)")
ax.set_ylabel("Dəyər (Y)")

# Tor xətləri (grid) və leqenda əlavə edirik
ax.grid(True, linestyle="--", alpha=0.6)
ax.legend()

# Qrafiki ekranda göstəririk
plt.show()