import numpy as np
import matplotlib.pyplot as plt

# Zaman və triqonometrik dəyərlər yaradırıq
t = np.arange(0, 5, 0.1)
y1 = np.sin(2 * np.pi * t)
y2 = np.cos(2 * np.pi * t)

# 2 sətir, 1 sütundan ibarət subplots yaradırıq
fig, axs = plt.subplots(2, 1, figsize=(8, 6))

# Birinci qrafik (Sine)
axs[0].plot(t, y1, linestyle="-.", color="blue")
axs[0].set_title("Sine Qrafiki")
axs[0].set_ylabel("Dəyər")

# İkinci qrafik (Cosine)
axs[1].plot(t, y2, linestyle="--", color="red")
axs[1].set_title("Cosine Qrafiki")
axs[1].set_xlabel("Zaman (t)")
axs[1].set_ylabel("Dəyər")

# Qrafiklərin bir-birinə qarışmaması üçün səliqəyə salırıq
plt.tight_layout()

# Ekranda göstəririk
plt.show()