import pandas as pd
import numpy as np

veri_seti = pd.read_csv("AB_NYC_2019.csv")

#Proje için anlam ifade etmeyen sütunlar silinir. Boş değerler 0 ile doldurulur. Aykırı değerler silinir. Boş kısım var mı diye kontrol edilir.
silinecek_sutunlar = ["id", "name", "host_id", "host_name", "last_review"]
veri_seti = veri_seti.drop(silinecek_sutunlar, axis=1)
veri_seti["reviews_per_month"].fillna(0, inplace=True)
veri_seti = veri_seti.query("price > 0 and price < 1000")
print(veri_seti.isnull().sum())

#Çok fazla mahalle bulunduğu için "neighbourhood" sütunu silinir. Silinmezse "Curse of Dimensionality" ile karşılaşılır.
#"neighbourhood_group" ve "room_type" sütunları kategorik olduğu için one-hot encoding yapılır.
#drop_first=True ile sütunların ilk kategorileri silinir. Sonuç etkilenmez, çünkü bu kategoriler diğer kategorilerle temsil edilir.
#dtype=int ile True-False değerleri 1-0 olarak kodlanır.
veri_seti.drop(["neighbourhood"], axis=1, inplace=True)
veri_seti = pd.get_dummies(veri_seti, columns=["neighbourhood_group", "room_type"], drop_first=True, dtype=int)

#Ölçeklendirme sayesinde farklı ölçeklerdeki özellikler aynı öneme sahip olur.
#fit_transform veriyi Numpy dizisine dönüştürür. Bu yüzden veri tekrar DataFrame'e çevrilir. Sütun isimleri korunur.
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
dizi = scaler.fit_transform(veri_seti)
hazir_veri_seti = pd.DataFrame(dizi, columns=veri_seti.columns)

from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

#1'den 10'a kadar farklı K değerleri için KMeans modeli oluşturulur ve her modelin atalet puanı hesaplanır.
#Atalet, bir kümenin içindeki evlerin o kümenin merkezine olan uzaklıklarının toplamıdır. Düşük olması istenir.
#Grafik sayesinde Elbow Method ile en uygun K değeri belirlenir. Grafiğe göre bu değer 3'tür.
atalet_puanlari = []
k_degerleri = range(1, 11)
for k in k_degerleri:
    kmeans = KMeans(n_clusters=k, random_state=42, n_init="auto")
    kmeans.fit(hazir_veri_seti)
    atalet_puanlari.append(kmeans.inertia_)
plt.plot(k_degerleri, atalet_puanlari, marker="o")
plt.xlabel("K Değeri")
plt.ylabel("Atalet Puanı")
plt.xticks(k_degerleri)
plt.grid()
plt.show()

#Model oluşturulur ve veriler kümelenir. Kümeler veri setine eklenir ve her kümenin ortalama özellikleri hesaplanır.
model = KMeans(n_clusters=3, random_state=42, n_init="auto")
kumeler = model.fit_predict(hazir_veri_seti)
veri_seti["Segment_No"] = kumeler
segment_ozeti = veri_seti.groupby("Segment_No").mean()
print(segment_ozeti)

#Segmentlere göre ortalama ev fiyatları görselleştirilir. Bar grafiği kullanılır.
ortalama_fiyatlar = veri_seti.groupby("Segment_No")["price"].mean()
plt.bar(ortalama_fiyatlar.index, ortalama_fiyatlar.values)
plt.title("Segmentlere Göre Ortalama Ev Fiyatları")
plt.xlabel("Segment Numarası ve Ortalama Fiyat")
plt.ylabel("Ortalama Fiyat")
plt.xticks([0, 1, 2], ["S0, ~117 Dolar", "S1, ~174 Dolar", "S2, ~93 Dolar"])
plt.show()