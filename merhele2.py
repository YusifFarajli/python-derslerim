# ==========================================
# 1. DƏYİŞƏNLƏR VƏ MƏLUMAT TİPLƏRİ (QUTULAR)
# ==========================================

# Mətn (String) - Mütləq dırnaq içində yazılır
ad = "Yusif"

# Tam ədəd (Integer) - Dırnaqsız yazılır
yaş = 24

# Onluq kəsir ədəd (Float) - Nöqtə ilə yazılır
ortalamam = 88.5

# Məntiqi dəyər (Boolean) - Yalnız True (Doğru) və ya False (Yalan) olur
tələbəyəm = True

# Bunları ekrana çıxaraq
print("İstifadəçi adı:", ad)
print("Yaş:", yaş)
print("Tələbədirmi?:", tələbəyəm)


# ==========================================
# 2. STRING ƏMƏLİYYATLARI VƏ FORMATLAŞDIRMA
# ==========================================

ders_adı = "python proqramlaşdırma"

# A. Mətni Böyük/Kiçik Hərflərə Çevirmək
print(ders_adı.upper())  # Hamsını BÖYÜK hərf edir: "PYTHON PROQRAMLAŞDIRMA"
print(ders_adı.title())  # Baş Hərfləri Böyüdür: "Python Proqramlaşdırma"

# B. Mətnin Uzunluğunu Saymaq
print("Sözün simvol sayı:", len(ders_adı))

# C. Slicing (Mətni kəsib dilimləmək)
# Python-da saymağa 0-dan başlayırıq!
# [0:6] -> 0-cı indeksdən başla, 6-cıya qədər get (6 daxil deyil)
print(ders_adı[0:6])  # Ekrana çıxacaq: "python"

# D. f-string (Ən rahat formatlama üsulu)
# Mətnin daxilinə dəyişənləri {} fiqurlu mötərizə ilə rahatca yerləşdiririk:
mesaj = f"Salam, mən {ad}. {yaş} yaşım var və {ders_adı.title()} öyrənirəm."
print(mesaj)