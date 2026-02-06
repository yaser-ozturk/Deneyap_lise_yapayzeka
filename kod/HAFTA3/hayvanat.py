import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import ComplementNB 
from sklearn.metrics import confusion_matrix, accuracy_score
import seaborn as sns
import matplotlib.pyplot as plt

# 1. Veri Yükleme
veri = pd.read_csv("hayvanatbahcesi.csv", encoding='unicode_escape')

# 2. Tüm Veri Seti Üzerinde One-Hot Encoding Uygulama
veri_encoded = pd.get_dummies(veri.drop(["sinifi"], axis=1))

# 3. Giriş ve Çıkış Matrislerini Oluşturma
girisler = np.array(veri_encoded)
cikis = np.array(veri["sinifi"]) 

# 4. Veriyi Bölme
X_train, X_test, y_train, y_test = train_test_split(
    girisler, cikis, test_size=0.35, random_state=109
)

# 5. Modeli Eğitme ve Tahmin
gnb = ComplementNB() 
gnb.fit(X_train, y_train)
y_pred = gnb.predict(X_test) 
y_only = gnb.predict(X_test[0:1, :]) 
print(" test verisi " ,X_test[0:1, :])
print(" gerçek değer:", y_test[0:1])
print("Tek bir örnek için tahmin:", y_only)


sinif_isimleri = {
    1: 'Memeli',
    2: 'Kuş',
    3: 'Sürüngen',
    4: 'Balık',
    5: 'Amfibi',
    6: 'Böcek',
    7: 'Omurgasız'
}

cm = confusion_matrix(y_test, y_pred)

# Gerçekte var olan sınıfların ID'lerini alıyoruz
sinif_idleri = np.unique(y_test) 
# ID'leri kullanarak isim listesini oluşturuyoruz
classes = [sinif_isimleri.get(int(id), f'Sınıf {id}') for id in sinif_idleri] 

cm_df = pd.DataFrame(cm, columns=classes, index=classes) 

plt.figure(figsize=(10,6)) 
sns.heatmap(cm_df, annot=True, fmt="d", cmap="YlGnBu")
plt.title("Karışıklık Matrisi (ComplementNB) - Sınıf İsimleri ile")
plt.ylabel("Gerçek Sınıflar")
plt.xlabel("Tahmin Edilen Sınıflar")
plt.show()

# Metrikler
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nSınıflandırma Raporu:\n")
