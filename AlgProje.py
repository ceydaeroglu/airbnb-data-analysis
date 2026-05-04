import pandas as pd
import numpy as np

#Veri seti temizlenir ve hazır hale getirilir. Ev listesi oluşturulur.
veri_seti = pd.read_csv("AB_NYC_2019.csv")
silinecek_sutunlar = ["host_id", "host_name", "last_review", "reviews_per_month", "calculated_host_listings_count", "latitude", "longitude", "neighbourhood", "minimum_nights", "availability_365"]
veri_seti = veri_seti.drop(silinecek_sutunlar, axis=1)
veri_seti = veri_seti.query("price > 0 and price < 1000")
veri_seti = veri_seti.dropna()
ev_listesi = veri_seti.to_dict("records")

#Quick sort tanımlanır ve uygun fonksiyon oluşturulur.
#Listenin ortasındaki eleman pivot seçilerek referans alınır. Küçükten büyüğe sıralama yapılır.
def quick_sort(liste):
    if len(liste) <= 1:
        return liste
    pivot_eleman = liste[len(liste) // 2]
    pivot_fiyat = pivot_eleman["price"]
    pivottan_kucukler = [ev for ev in liste if ev["price"] < pivot_fiyat]
    pivottan_buyukler = [ev for ev in liste if ev["price"] > pivot_fiyat]
    pivota_esitler = [ev for ev in liste if ev["price"] == pivot_fiyat]
    return quick_sort(pivottan_kucukler) + pivota_esitler + quick_sort(pivottan_buyukler)

#Quick Sort fonksiyonu kullanılarak evler fiyatlarına göre sıralanır ve en ucuz 5 ev ekrana yazdırılır.
sirali_evler = quick_sort(ev_listesi)
print("En ucuz 5 ev:")
for ev in sirali_evler[:5]:
    print(f"Fiyat: {ev['price']}$, Mahalle: {ev['neighbourhood_group']}, Oda Tipi: {ev['room_type']}")


#Binary search tanımlanır ve uygun fonksiyon oluşturulur.
def butceye_uygun_ev_bul(sirali_liste, hedef_butce):
    sol_indeks = 0
    sag_indeks = len(sirali_liste) - 1
    en_iyi_ev = None
    while sol_indeks <= sag_indeks:
        orta_indeks = (sol_indeks + sag_indeks) // 2
        ortadaki_ev = sirali_liste[orta_indeks]
        orta_fiyat = sirali_liste[orta_indeks]["price"]

        if orta_fiyat == hedef_butce:
            return ortadaki_ev
        elif orta_fiyat < hedef_butce:
            en_iyi_ev = ortadaki_ev
            sol_indeks = orta_indeks + 1
        else:
            sag_indeks = orta_indeks - 1
    return en_iyi_ev

butce = int(input("Lütfen bütçenizi giriniz: "))
bulunan_ev = butceye_uygun_ev_bul(sirali_evler, butce)
if bulunan_ev:
    print(f"Bütçenize uygun en iyi ev: Fiyat: {bulunan_ev['price']}$, Mahalle: {bulunan_ev['neighbourhood_group']}, Oda Tipi: {bulunan_ev['room_type']}")
else:
    print("Bütçenize uygun bir ev bulunamadı.")