## Karar Ağaçları

![[Pasted image 20260109175217.png]]

![[Pasted image 20260109204333.png]]

![[Pasted image 20260109175944.png]]

![[Pasted image 20260109180045.png]]

![[Pasted image 20260109180121.png]]

![[Pasted image 20260109180150.png]]


## Karar Ağacı teknikleri

#### ID3 Karar Ağacı Algoritması

![[Pasted image 20260109175728.png]]

ID3 karar ağaç algoritmasının C4.5 ve C5.0 isminde iki tane versiyonu sıklıkla kullanılmaktadır. ID3 karar ağacı algoritmasında her düğümden çıkan dallar ile karar ağacı oluşmaktadır. Ağaçtaki dalların sayısı algoritmada tahmin edilecek sınıf sayısına eşittir. Karar ağacı algoritmasında yapraktaki hata (error) oranına göre budama işlemi yapılır.

![[Pasted image 20260109175807.png]]


![[Pasted image 20260109175831.png]]



#### C&RT Karar Ağacı Algoritması 

Gini indeksi (dizini) veya Gini katsayısı, İtalyan istatistikçi Corrado Gini tarafından 1912’de geliştirilen istatistiksel bir ölçüdür. Gini’ye dayalı ikili bölme işlemine göre çalışan bir karar ağacı algoritmasıdır. Bu algoritmada en son veya uçta olmayan her bir düğümde iki adet dal vardır. Hem Sınıflandırma hem de regresyon (sayısal sonuç) uygulamalarında kullanılır. Budama işlemi oluşturulan karar ağacı yapısına göre değişiklik gösterir. 

#### CHAID Karar Ağacı Algoritması 

Karar ağacı CHAID algoritması, istatistik tabanlı olarak G. V. Kass tarafından 1980’de geliştirilmiştir. Sınıflandırma ve regresyon uygulamalarında tercih edilir. CHAID algoritması, bağımsız değişkenlerin, birbirleriyle olan etkileşimini bulan bir tekniktir. CHAID algoritması dallanma kriterinde bağımlı değişken kategorik ise iki ya da daha çok grup arasında fark olup olmadığını tespit eden Ki-kare testine göre bölme işlemini gerçekleştirir. 

#### SPRINT Karar Ağacı Algoritması 

SPRINT algoritması 1996 yılında Shafer, Agrawal ve Mehta tarafından geliştirilip entropiye dayanmaktadır. SPRINT karar ağaçları algoritması büyük veri kümeleri için ideal bir algoritmadır. Ağaç yapısında en iyi dallanma için her bir değişkene ait özellikleri bir kez sıraya dizer ve karar ağaçı yapısı bu şekilde oluşur. Bu algoritmada her bir değişken için ayrı bir değişken listesi hazırlanır. Bölme işlemi tek bir özelliğin değerine göre saptanır.

#### SLIQ Karar Ağacı Algoritması
  
  SLIQ karar ağacı algoritması 1996 yılında Agrawal, Mehta ve Rissanen tarafından geliştirilmiştir. Bu algoritma Gini tekniği ile nicel ve nitel veri tipleri kullanılabilmektedir. Ayrıca verilerin sıralanması aşamasında en iyi dallara ayırma tekniğini uygulamaktadır. Bu algoritma hızlı ölçüm yapan bir sınıflandırıcıya ve hızlı ağaç budama algoritmasına sahiptir.

## Receiver Operating Characteristic-ROC

![[Pasted image 20260109181137.png]]

![[Pasted image 20260109214530.png]]


![[Pasted image 20260109190051.png]]
aaaaaaa
## Kod ve Modelin testi

![[Pasted image 20260109213331.png]]

![[Pasted image 20260109220733.png]]
Veri setini indirme linki:
https://www.kaggle.com/vbookshelf/rice-leaf-diseases/download

```python

def veri_donusturme(klasor_adi,sinif_adi):
    goruntuler=dosya(klasor_adi)
    goruntu_sinif=[]

    for goruntu in goruntuler:

        goruntu_oku= img.open(goruntu).convert('L')
        gorunu_boyutlandirma=goruntu_oku.resize((28,28))
        goruntu_donusturme=np.array(gorunu_boyutlandirma).flatten()

        if sinif_adi=="bakteri_yaprak_yanik":
            veriler=np.append (goruntu_donusturme, [0])

        elif sinif_adi=="kahve_nokta":
            veriler=np.append (goruntu_donusturme, [1])

        elif sinif_adi=="yaprak_isi":
            veriler=np.append (goruntu_donusturme, [2])      
        else:
            continue
        goruntu_sinif.append(veriler)

    return goruntu_sinif

```


Bu fonksiyon belirtilen klasördeki görüntü dosyalarını okur, standart bir formata dönüştürür ve her görüntüyü ilgili sınıf etiketiyle (label) birleştirir.

Amacı: Görüntüleri Sayısal Veriye Dönüştürmek

Argüman :  `klasor_adi` (görüntülerin bulunduğu klasör yolu) ve `sinif_adi` (görüntülerin ait olduğu sınıfın adı) 

---

```python
goruntuler = dosya(klasor_adi) 
```

- Daha önce tanımlanan `dosya(yol)` fonksiyonunu kullanarak, belirtilen `klasor_adi` içindeki tüm görüntü dosyalarının **tam yollarını** içeren bir liste (`goruntuler`) elde edilir.


```Python
for goruntu in goruntuler: 
    # ... işlemler ...
```

- `goruntuler` listesindeki her bir dosya yolu üzerinde bir döngü başlatılır.

```python
goruntu_oku= img.open(goruntu).convert('L')
gorunu_boyutlandirma=goruntu_oku.resize((28,28))
goruntu_donusturme=np.array(gorunu_boyutlandirma).flatten()
```

Döngü içindeki bu kısım, bir görüntüyü makine öğrenimi modelinin anlayabileceği sayısal bir vektöre dönüştürür

Gri tonlamalı bir `Image` nesnesi. 
Görüntüyü **28x28 piksel** boyutuna küçültür (yeniden boyutlandırır). 
Görüntüyü bir `numpy` dizisine dönüştürür. Ardından `flatten()` metodu ile bu 28x28'lik matrisi **tek boyutlu bir vektöre** dönüştürür. ($28 \times 28 = 784$ elemanlı bir vektör olur). 

---

Veri Dönüştürme ve DataFrame Oluşturma

```python
yanik_veri=veri_donusturme(bakteri_yaprak_yanik,"bakteri_yaprak_yanik")
yanik_veri_df=pd.DataFrame(yanik_veri)

kahve_nokta_veri=veri_donusturme(kahve_nokta,"kahve_nokta")
kahve_nokta_veri_df=pd.DataFrame(kahve_nokta_veri)

yaprak_isi_veri=veri_donusturme(yaprak_isi,"yaprak_isi")
yaprak_isi_veri_df=pd.DataFrame(yaprak_isi_veri)

tum_veri= pd.concat([yanik_veri_df, kahve_nokta_veri_df,yaprak_isi_veri_df ])
```

Kod, her hastalık sınıfı için aynı iki adımı tekrarlar:

Daha önce tanımladığınız `veri_donusturme` fonksiyonunu çağırır. `bakteri_yaprak_yanik` klasöründeki tüm görüntüleri okur, 28x28 gri tonlamalı vektörlere dönüştürür ve her vektörün sonuna 0 etiketini (sınıf numarasını) ekler.

Elde edilen bu vektör listesini kullanarak bir **Pandas DataFrame** oluşturur. Bu DataFrame'in her satırı tek bir görüntüyü temsil eder (784 piksel sütunu + 1 etiket sütunu).


Bu işlem, sırasıyla **yaprak yanığı**, **kahve nokta** ve **yaprak isi** sınıfları için tekrarlanır ve sonuçta üç ayrı DataFrame elde edilir:

- `yanik_veri_df` (Sınıf Etiketi: 0)
- `kahve_nokta_veri_df` (Sınıf Etiketi: 1)
- `yaprak_isi_veri_df` (Sınıf Etiketi: 2)


```python
tum_veri = pd.concat([yanik_veri_df, kahve_nokta_veri_df, yaprak_isi_veri_df])
```

`pd.concat()` fonksiyonu, Pandas'ta birden fazla DataFrame'i birleştirmek için kullanılır.
Bu satır, yukarıda oluşturulan üç ayrı DataFrame'i (**alt alta**) ekleyerek tek bir büyük DataFrame (`tum_veri`) oluşturur.

Sonuç

`tum_veri` DataFrame'i, makine öğrenimi modelinizi eğitmek için hazır olan nihai veri setinizdir. Bu veri seti şunları içerir:

**Görüntü Verisi:** Tüm sınıflara ait, 28x28 boyutuna indirgenmiş, gri tonlamalı ve düzleştirilmiş (flattened) görüntü piksel değerleri (toplam 784 sütun).

**Sınıf Etiketi:** Her satırın (görüntünün) son sütununda, o görüntünün hangi hastalığa ait olduğunu belirten sayısal etiket (0, 1 veya 2).

---
```python
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics  
from sklearn.model_selection import GridSearchCV

Giris=np.array(tum_veri)[:,:784]
Cikis=np.array(tum_veri)[:,784]

Giris_train, Giris_test, Cikis_train, Cikis_test = train_test_split(Giris, Cikis,
test_size=0.2, random_state=109)

model= DecisionTreeClassifier()
clf = model.fit(Giris_train,Cikis_train)
Cikis_pred = clf.predict(Giris_test)

print("Doğruluk:",metrics.accuracy_score(Cikis_test, Cikis_pred))
```

```python
Giris_train, Giris_test, Cikis_train, Cikis_test = train_test_split(Giris, Cikis,
test_size=0.2, random_state=109)
```
- **`Giris` (X):** Tüm görüntülerin piksel değerlerini içeren veri setiniz (Bağımsız değişkenler).
- **`Cikis` (y):** Tüm görüntülerin sınıf etiketlerini (0, 1, 2) içeren veri setiniz (Bağımlı değişkenler).
- **`test_size=0.2`:** Veri setinin %20'sinin test seti olarak ayrılacağını belirtir. Geriye kalan %80'i ise eğitim seti olarak kullanılır.
- **`random_state=109`:** Bu parametre, verinin her çalıştırışta **aynı şekilde** bölünmesini sağlayan bir tohum (seed) görevi görür. Bu, deneylerinizin **tekrarlanabilir** olmasını sağlar. (Eğer bu belirtilmezse, her çalıştırışta farklı bir rastgele bölme gerçekleşir.)
---
```python
import matplotlib.pyplot as plt
from sklearn.preprocessing import label_binarize
from sklearn.metrics import roc_curve, auc
from itertools import cycle

Cikis_test = label_binarize(Cikis_test, classes=[0, 1, 2])
Cikis_pred = label_binarize(Cikis_pred, classes=[0, 1, 2])

plt.figure(figsize=(60, 40),dpi=150)
n_classes=3
fpr = dict()
tpr = dict()
roc_auc = dict()

  

for i in range(n_classes):

    fpr[i], tpr[i], _ = roc_curve(Cikis_test[:, i], Cikis_pred[:, i])
    roc_auc[i] = auc(fpr[i], tpr[i])


colors = cycle(['blue', 'red', 'green'])

  

for i, color in zip(range(n_classes), colors):
    plt.plot(fpr[i], tpr[i], color=color,  
        label=' {0} Sinifina ait ROC eğrisi (AUC = {1:0.2f})' ''.format(i, roc_auc[i]))

  

plt.plot([0, 1], [0, 1], 'k--')
plt.xlim([-0.05, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.legend(loc="lower right")

plt.show()
```

**Çok Sınıflı (Multiclass) Sınıflandırma için ROC Eğrileri (Receiver Operating Characteristic) çizmek 
Kod, modelinizin her bir sınıfı ne kadar iyi ayırabildiğini gösteren bir grafik oluşturur.


``` python
Cikis_test = label_binarize(Cikis_test, classes=[0, 1, 2]) 
Cikis_pred = label_binarize(Cikis_pred, classes=[0, 1, 2])
```

 ROC eğrileri doğası gereği ikili (binary) sınıflandırma için tasarlanmıştır. Üç sınıfınız (0, 1, 2) olduğu için, her sınıfı diğerlerinden ayırmak üzere veriyi "bir'e karşı hepsi" (one-vs-all) formatına dönüştürmeniz gerekir.

**İşlem:** `label_binarize` fonksiyonu, hem gerçek etiketleri (`Cikis_test`) hem de modelin tahminlerini (`Cikis_pred`) üç sütunlu bir matrise dönüştürür.

 Örneğin, etiket $\mathbf{0}$ olan bir örnek artık `[1, 0, 0]` olarak temsil edilir. Etiket $\mathbf{1}$ olan bir örnek `[0, 1, 0]` olur.



```python
for i in range(n_classes): 
    fpr[i], tpr[i], _ = roc_curve(Cikis_test[:, i], Cikis_pred[:, i]) 
    roc_auc[i] = auc(fpr[i], tpr[i])
```

- **Döngü:** Her bir sınıf (0, 1, 2) için ayrı ayrı döngü yapılır.

- **`roc_curve`:** Bu fonksiyon, ikili formata dönüştürülmüş test ve tahmin verilerini kullanarak o sınıf için ROC eğrisinin koordinatlarını hesaplar:
    - **FPR (False Positive Rate):** Yanlış Pozitif Oranı (Yatay Eksen)
    - **TPR (True Positive Rate):** Doğru Pozitif Oranı (Dikey Eksen)

- **`auc`:** Hesaplanan FPR ve TPR değerleri arasındaki alanı (`Area Under the Curve`) hesaplar. **AUC değeri ne kadar 1'e yakınsa, modelin o sınıfı ayırma başarısı o kadar yüksektir.**


```python
colors = cycle(['blue', 'red', 'green']) 

for i, color in zip(range(n_classes), colors): 
    plt.plot(fpr[i], tpr[i], color=color, 
        label=' {0} Sinifina ait ROC eğrisi (AUC = {1:0.2f})' ''.format(i, roc_auc[i])) 
```

- **Çizim:** Her bir sınıfın (0, 1, 2) FPR ve TPR değerleri, atanmış farklı bir renkle (`blue`, `red`, `green`) grafiğe çizilir.
- **Etiketleme:** Her çizgiye, hangi sınıfa ait olduğu ve o sınıfa ait hesaplanan AUC değeri etiketlenir.



```python
import numpy as np

import PIL.Image as img

import os

import pandas as pd

bakteri_yaprak_yanik="C:/Users/User/Desktop/deneyapegitim/yapayzeka/kod/cice_leaf_diseases/Bacterial leaf blight/"

kahve_nokta="C:/Users/User/Desktop/deneyapegitim/yapayzeka/kod/cice_leaf_diseases/Brown spot/"

yaprak_isi="C:/Users/User/Desktop/deneyapegitim/yapayzeka/kod/cice_leaf_diseases/Leaf smut/"

  

def dosya(yol):

    return [os.path.join(yol,f) for f in os.listdir(yol)]

def veri_donusturme(klasor_adi,sinif_adi):

    goruntuler=dosya(klasor_adi)

    goruntu_sinif=[]

    for goruntu in goruntuler:

  

        goruntu_oku= img.open(goruntu).convert('L')

        gorunu_boyutlandirma=goruntu_oku.resize((28,28))

        goruntu_donusturme=np.array(gorunu_boyutlandirma).flatten()

        if sinif_adi=="bakteri_yaprak_yanik":

            veriler=np.append (goruntu_donusturme, [0])

        elif sinif_adi=="kahve_nokta":

            veriler=np.append (goruntu_donusturme, [1])

        elif sinif_adi=="yaprak_isi":

            veriler=np.append (goruntu_donusturme, [2])      

        else:

            continue

        goruntu_sinif.append(veriler)

    return goruntu_sinif

yanik_veri=veri_donusturme(bakteri_yaprak_yanik,"bakteri_yaprak_yanik")

yanik_veri_df=pd.DataFrame(yanik_veri)

kahve_nokta_veri=veri_donusturme(kahve_nokta,"kahve_nokta")

kahve_nokta_veri_df=pd.DataFrame(kahve_nokta_veri)

yaprak_isi_veri=veri_donusturme(yaprak_isi,"yaprak_isi")

yaprak_isi_veri_df=pd.DataFrame(yaprak_isi_veri)

tum_veri= pd.concat([yanik_veri_df, kahve_nokta_veri_df,yaprak_isi_veri_df ])

import pandas as pd

from sklearn.tree import DecisionTreeClassifier

from sklearn.model_selection import train_test_split

from sklearn import metrics  

from sklearn.model_selection import GridSearchCV

Giris=np.array(tum_veri)[:,:784]

Cikis=np.array(tum_veri)[:,784]

Giris_train, Giris_test, Cikis_train, Cikis_test = train_test_split(Giris, Cikis,

test_size=0.2, random_state=109)

model= DecisionTreeClassifier()

clf = model.fit(Giris_train,Cikis_train)

Cikis_pred = clf.predict(Giris_test)

print("Doğruluk:",metrics.accuracy_score(Cikis_test, Cikis_pred))

import matplotlib.pyplot as plt

from sklearn.preprocessing import label_binarize

from sklearn.metrics import roc_curve, auc

from itertools import cycle

Cikis_test = label_binarize(Cikis_test, classes=[0, 1, 2])

Cikis_pred = label_binarize(Cikis_pred, classes=[0, 1, 2])

plt.figure(figsize=(60, 40),dpi=150)

n_classes=3

fpr = dict()

tpr = dict()

roc_auc = dict()

  

for i in range(n_classes):

    fpr[i], tpr[i], _ = roc_curve(Cikis_test[:, i], Cikis_pred[:, i])

    roc_auc[i] = auc(fpr[i], tpr[i])

  
  

colors = cycle(['blue', 'red', 'green'])

  

for i, color in zip(range(n_classes), colors):

    plt.plot(fpr[i], tpr[i], color=color,  

        label=' {0} Sinifina ait ROC eğrisi (AUC = {1:0.2f})' ''.format(i, roc_auc[i]))

  

plt.plot([0, 1], [0, 1], 'k--')
plt.xlim([-0.05, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.legend(loc="lower right")
plt.show()
```