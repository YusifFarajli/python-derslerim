# ==========================================
# OBYEKTYÖNÜMLÜ PROQRAMLAŞDIRMA (OOP)
# ==========================================

# 1. CLASS (ÇERTYOJ / ŞABLON) YARADIRIQ
class Telefon:
    # Class Attribute (Bütün telefonlarda olan ortaq xüsusiyyət)
    qurğu_tipi = "Mobil İletişim Cihazı"

    # __init__ -> Yaranan kimi avtomatik işə düşən ustadır (Konstruktor)
    # self -> Həmin konkret telefonu təmsil edir
    def __init__(self, marka, model, qiymət):
        self.marka = marka    # Telefonun markası (Instance Attribute)
        self.model = model    # Telefonun modeli
        self.qiymət = qiymət  # Telefonun qiyməti

    # Metod (Telefonun edə bildiyi hərəkət/funksiya)
    def zəng_et(self, nömrə):
        print(f"{self.marka} {self.model} modelindən {nömrə} nömrəsinə zəng edilir...")

    def məlumatı_göstər(self):
        print(f"Telefon: {self.marka} {self.model} | Qiymət: {self.qiymət} AZN")


# 2. INHERITANCE (İRSİ KEÇMƏ)
# Smartfon sinfi Telefon sinfinin bütün xüsusiyyətlərini avtomatik götürür (miras alır)
class Smartfon(Telefon):
    def internetə_gir(self):
        print(f"{self.marka} ilə brauzer açıldı və internetə bağlanıldı.")


# ==========================================
# OBYEKTLƏRİ (REAL TELEFONLARI) YARADIRIQ
# ==========================================

# Çertyojdan 2 fərqli canlı obyekt yaradırıq:
tel1 = Telefon("Nokia", "3310", 50)
tel2 = Smartfon("Apple", "iPhone 15", 2500)

# Obyektlərin metodlarını işlədəklər:
tel1.məlumatı_göstər()
tel1.zəng_et("0501234567")

print("-" * 30)

tel2.məlumatı_göstər()
tel2.internetə_gir()  # Yalnız Smartfon-da olan xüsusi metod