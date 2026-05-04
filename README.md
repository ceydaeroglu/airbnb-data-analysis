# Airbnb Data Analysis & Search Algorithms

*(Please scroll down for the Turkish version / Türkçe versiyon için aşağı kaydırınız)*

## English

### Project Overview
This repository contains two interconnected projects applying Machine Learning and fundamental Data Structures/Algorithms to the **New York City Airbnb Open Data (2019)**. The goal of this project is to analyze market dynamics through segmentation and build an efficient search engine for users based on their budget constraints.

### Features & Modules

**1. Machine Learning (`MLProje.py`)**
* **Data Preprocessing:** Handled missing values, removed outliers (prices > $1000), and applied One-Hot Encoding for categorical features to prevent the Curse of Dimensionality.
* **K-Means Clustering:** Applied the Elbow Method to determine the optimal number of clusters (K=3).
* **Market Segmentation:** Divided the NYC Airbnb market into three distinct segments based on geographic location, room type, and price distribution.

**2. Algorithms (`AlgProje.py`)**
* **Quick Sort:** Implemented a custom Quick Sort algorithm to efficiently sort thousands of listings by price.
* **Binary Search:** Built a custom Binary Search algorithm to allow users to input a target budget and instantly find the best available listing that does not exceed their limit.

### Tech Stack
* **Language:** Python
* **Libraries:** Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn

### How to Run
1. Clone the repository: `git clone https://github.com/ceydaeroglu/airbnb-data-analysis.git`
2. Ensure you have the required libraries installed: `pip install pandas numpy scikit-learn matplotlib seaborn`
3. Run the ML pipeline: `python MLProje.py`
4. Run the Search Algorithm: `python AlgProje.py`

---

## Türkçe

### Proje Özeti
Bu depo, **New York City Airbnb (2019)** veri seti üzerinde Makine Öğrenmesi ve temel Veri Yapıları/Algoritmalar kullanılarak geliştirilmiş iki entegre projeyi içermektedir. Projenin temel amacı, evleri segmentlere ayırarak pazar dinamiklerini analiz etmek ve kullanıcıların bütçelerine en uygun evi bulmalarını sağlayan hızlı bir arama motoru inşa etmektir.

### Özellikler ve Modüller

**1. Makine Öğrenmesi (`MLProje.py`)**
* **Veri Ön İşleme:** Kayıp veriler temizlendi, aykırı değerler (1000$ üzeri fiyatlar) filtrelendi ve Boyutluluk Lanetini (Curse of Dimensionality) önlemek adına kategorik değişkenlere One-Hot Encoding uygulandı.
* **K-Means Kümeleme:** Elbow (Dirsek) metodu kullanılarak optimum küme sayısı (K=3) belirlendi.
* **Pazar Segmentasyonu:** NYC Airbnb pazarı; coğrafi konum, oda tipi ve fiyat dağılımına göre üç farklı profile ayrıldı.

**2. Algoritmalar (`AlgProje.py`)**
* **Quick Sort (Hızlı Sıralama):** Veri setindeki binlerce ilanı fiyata göre en hızlı şekilde sıralamak için özel bir Quick Sort algoritması kodlandı.
* **Binary Search (İkili Arama):** Kullanıcıların bütçelerini aşmayan en iyi seçeneği saliseler içinde bulabilmesi için özel bir Binary Search algoritması geliştirildi.

### Kullanılan Teknolojiler
* **Dil:** Python
* **Kütüphaneler:** Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn

### Nasıl Çalıştırılır?
1. Depoyu klonlayın: `git clone https://github.com/ceydaeroglu/airbnb-data-analysis.git`
2. Gerekli kütüphaneleri yükleyin: `pip install pandas numpy scikit-learn matplotlib seaborn`
3. ML segmentasyonunu çalıştırmak için: `python MLProje.py`
4. Arama motorunu çalıştırmak için: `python AlgProje.py`

---
## Author / Yazar
**Ceyda Eroğlu** B.Sc. Artificial Intelligence and Machine Learning | Marmara University  
Yapay Zeka ve Makine Öğrenmesi | Marmara Üniversitesi
