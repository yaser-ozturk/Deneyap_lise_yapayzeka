
## Conda kurulumu

https://www.anaconda.com/docs/getting-started/miniconda/install#windows-installation

Doğru dizinde olduğunuzdan emin olun

```bash
cd Users\User

curl https://repo.anaconda.com/miniconda/Miniconda3-latest-Windows-x86_64.exe --output .\Downloads\Miniconda3-latest-Windows-x86_64.exe
```

Yükleme tamamlanınca %100 olur.

![[Pasted image 20251216143350.png]]

Yüklenen exe'nin çalıştırılması.

```bash
.\Downloads\Miniconda3-latest-Windows-x86_64.exe
```

![[Pasted image 20251216144251.png]]

![[Pasted image 20251216144453.png]]

![[Pasted image 20251216144527.png]]


![[Pasted image 20251216144636.png]]

İndirme işleminin bitmesinin ardından cmd yi aç kapa ve conda kurulmuşmu diye bak.

```bash
C:\Users\User>conda --version                                                      

conda 25.9.1                                                                                     
```

harika conda kurulumu gerçekleşti.

## Enviroment kurulumu

Aşağıdaki komutu **aynen** çalıştır:

```bash
conda tos accept --override-channels --channel https://repo.anaconda.com/pkgs/main`
```

Bu, **resmî Anaconda deposunun** kullanım şartlarını kabul eder.

Enveriment kuralım cmd ye yazalım

```bash
conda create -n env-01 python=3.10 numpy scipy
```

![[Pasted image 20251216150656.png]]

a ya basıp kabul et çıkan bildirimleri a enter.

ilelemede y yaz ve entere bas.

![[Pasted image 20251216150826.png]]
active ve deactive olması:

```bash
conda activate yapayzeka_env   
conda deactivate 
```

![[Pasted image 20251216151248.png]]

 **VS Code’u environment ile ilişkilendirelim**
 
- VS Code’u açt
- `Ctrl + Shift + P`
- **Python: Select Interpreter**
- Listeden:`Python 3.10.x (yapayzeka_env)`seç

**Sonuç:**
- VS Code’un sağ alt köşesinde: `Python 3.10.x (yapayzeka_env)` yazdı

---
**Terminal ile interpreter farkını anladık**

**Önemli kavram:**
Interpreter seçmek ≠ terminalde environment aktif etmek
- Sağ alttaki seçim:
    -  Run / Debug için
- Terminal:
    - Manuel komutlar için
---

**Terminalde env otomatik aktif olsun diye ayar yaptık**

- Terminal açılınca `(yapayzeka_env)` otomatik gelsin

**VS Code Ayarı:**
`Python › Terminal: Activate Environment` Açtık

**Sonuç:**
- Yeni terminal açınca: `(yapayzeka_env) PS ...`

---
**Neden “Run” ile hata aldık?**

Çünkü:
- `[Running] python -u ...`
- **Code Runner eklentisi**
- Sistem Python’u kullandı 

**Çözüm:**
- Code Runner kullanma
-  **Run Python File in Terminal** kullan

## Yapay zekaya adım

### NumPy (Numerical Python)

NumPy, Python’da **sayısal hesaplamalar** yapmak için kullanılan en temel ve en hızlı kütüphanelerden biridir.  
Özellikle **çok boyutlu diziler (array)** üzerinde çalışmak için tasarlanmıştır. Normal Python listelerine göre **daha az bellek kullanır** ve **çok daha hızlı işlem yapar**.

NumPy;

- Vektör ve matris işlemleri
- Lineer cebir hesaplamaları
- İstatistiksel işlemler
- Matematiksel fonksiyonlar

gibi konularda yoğun olarak kullanılır. Yapay zekâ ve makine öğrenmesi algoritmalarının büyük çoğunluğu **NumPy dizileri** üzerinden çalışır.

#### **NumPy Örnek**
```python 
import numpy as np  
dizi = np.array([1, 2, 3, 4, 5]) 
print(dizi * 2)
```

Bu örnekte NumPy dizisindeki tüm elemanlar **tek satırda** 2 ile çarpılmaktadır.

### SciPy

SciPy, **NumPy üzerine inşa edilmiş**, bilimsel ve mühendislik hesaplamaları için kullanılan **çok yönlü bir Python kütüphanesidir**.  
Özellikle veri analizi, sinyal işleme, optimizasyon ve istatistiksel hesaplamalarda yaygın olarak kullanılır.

SciPy; **kümeleme**, **regresyon (tahmin)**, **veri işleme**, **sayısal integrasyon**, **diferansiyel denklemler** ve **optimizasyon** gibi birçok ileri seviye işlemi gerçekleştirebilecek hazır fonksiyonlar sunar. Bu sayede karmaşık matematiksel işlemler, düşük seviyeli kod yazmaya gerek kalmadan hızlı ve güvenilir bir şekilde uygulanabilir.

Makine öğrenmesi ve yapay zekâ projelerinde SciPy;

- Verilerin **ön işlenmesi**,
- Matematiksel modelleme,
- Optimizasyon problemlerinin çözümü  gibi aşamalarda destekleyici bir rol üstlenir.
### Pandas

Pandas, **tablosal veriler** (Excel, CSV, veri tabloları) üzerinde işlem yapmak için kullanılan temel Python kütüphanesidir.  
Verileri **satır ve sütun** mantığıyla ele alır ve veri analizini oldukça kolaylaştırır.
Pandas ile;

- Veri okuma (CSV, Excel, JSON)
- Eksik veri temizleme
- Filtreleme ve sıralama
- İstatistiksel analiz

işlemleri rahatlıkla yapılabilir. Yapay zekâ projelerinde veri genellikle Pandas ile **ön işleme (preprocessing)** aşamasından geçirilir.

#### **Pandas Örnek**
```python
import pandas as pd  
veri = {     "Yaş": [20, 22, 21],   
  "Not": [85, 90, 88] }
df = pd.DataFrame(veri) print(df)`
```

Bu örnekte bir tablo oluşturulmuş ve satır–sütun yapısında ekrana yazdırılmıştır.

---

### Matplotlib

Matplotlib, verileri **grafik ve görseller** ile ifade etmek için kullanılan bir çizim kütüphanesidir.  
Sayısal verilerin daha kolay anlaşılabilmesi için **çizgi grafikleri, sütun grafikleri, dağılım grafikleri** gibi görseller üretir.

Yapay zekâ ve veri analizinde;

- Veri dağılımlarını incelemek
- Model sonuçlarını görselleştirmek
- Eğitim sürecindeki hata (loss) grafiklerini çizmek

amacıyla sıkça kullanılır.

#### **Matplotlib Örnek**

```python
import matplotlib.pyplot as plt 
x = [1, 2, 3, 4] 
y = [10, 20, 15, 25]  
plt.plot(x, y) 
plt.xlabel("X Değeri") 
plt.ylabel("Y Değeri") 
plt.title("Basit Grafik Örneği") 
plt.show()`
```


Bu örnekte verilen x ve y değerleri kullanılarak basit bir çizgi grafiği oluşturulmuştur.

### **Scikit-Learn**

Scikit-Learn, **makine öğrenmesi algoritmalarını kolay ve hızlı bir şekilde uygulamak** için kullanılan en yaygın Python kütüphanelerinden biridir.  
Veri ön işleme, model eğitimi, test ve değerlendirme adımlarını tek bir yapı altında sunar.

Scikit-Learn;

- **Regresyon** (sayısal tahmin),
- **Sınıflandırma** (etiket tahmini),
- **Kümeleme** (benzer verileri gruplama)  
    gibi temel makine öğrenmesi problemlerinde kullanılan çok sayıda algoritmayı hazır olarak içerir.

Derin öğrenme yerine, **klasik makine öğrenmesi** problemleri için tercih edilir.

#### Basit Örnek – Doğrusal Regresyon

```python
from sklearn.linear_model import LinearRegression 
import numpy as np  
X = np.array([[1], [2], [3], [4]]) 
y = np.array([2, 4, 6, 8])  
model = LinearRegression() 
model.fit(X, y)  
print(model.predict([[5]]))  # Tahmin`
```


### **TensorFlow**

TensorFlow, **Google tarafından geliştirilen**, büyük ölçekli **derin öğrenme ve yapay sinir ağları** uygulamaları için kullanılan açık kaynaklı bir kütüphanedir.  
Özellikle görüntü işleme, doğal dil işleme ve büyük veri setleri üzerinde model eğitimi için kullanılır.

TensorFlow;

- Otomatik türev alma,
- GPU/CPU desteği.
- Büyük modelleri verimli şekilde eğitme  
    gibi güçlü özellikler sunar.

#### Basit Örnek – Tek Katmanlı Sinir Ağı
```python
import tensorflow as tf  
model = tf.keras.Sequential([tf.keras.layers.Dense(1, input_shape=(1,)) ])  model.compile(optimizer='adam', loss='mse') 
print("TensorFlow modeli hazır")`
```

### **Keras**

Keras, **TensorFlow üzerinde çalışan**, sinir ağlarını **hızlı ve kolay şekilde kurmak** için geliştirilmiş yüksek seviyeli bir kütüphanedir.  
Kod okunabilirliğini artırır ve karmaşık ağları birkaç satırla tanımlamaya olanak tanır.

Keras;

- Katman tabanlı yapı,
- Hızlı prototipleme,
- Kolay eğitim ve test süreçleri  
    sunarak özellikle **öğrenme ve hızlı deneme** aşamalarında tercih edilir.

#### Basit Örnek – Keras ile Sinir Ağı
```python
from tensorflow.keras.models import Sequential 
from tensorflow.keras.layers import Dense  
model = Sequential() model.add(Dense(8, activation='relu', input_shape=(4,))) model.add(Dense(1))  
model.compile(optimizer='adam', loss='mse') 
print("Keras modeli oluşturuldu")`
```

### **PyTorch**

PyTorch, **Facebook (Meta)** tarafından geliştirilen, özellikle **esnekliği ve dinamik yapısı** ile öne çıkan bir derin öğrenme kütüphanesidir.  
Araştırma ve akademik çalışmalarda oldukça yaygın olarak kullanılır.

PyTorch’un en büyük avantajı;

- Dinamik hesaplama grafiği,
- Python’a çok yakın söz dizimi,
- Model üzerinde adım adım kontrol imkânı  
    sunmasıdır.

#### Basit Örnek – PyTorch Tensör Kullanımı
```python
import torch  
x = torch.tensor([1.0, 2.0, 3.0]) 
y = x * 2  print(y)
```


### Kütüphane kurulumları

VS Code terminalinde veya CMD’ye:

```bash
conda activate yapayzeka_env
```


Terminal başında şunu görmelisin:
```bash
(yapayzeka_env)
```

NumPy, Pandas ve Matplotlib Kur

```bash
conda install numpy 
conda install pandas
conda install matplotlib
conda install scipy
conda install scikit-learn
conda install pytorch torchvision torchaudio cpuonly -c pytorch
pip install tensorflow
```


## Yapayzekaya hızlı bir örnek

Eğitilebilir Yapay Zekâ Platform ile Taş Kâğıt Makas Oyununun Modellenmesi için aşağıda verilen linki tıklayın. https://teachablemachine.withgoogle.com/ 
![[Pasted image 20251216163525.png]]
Class isimlerini “Taş”, “Kâğıt” ve “Makas” olarak isimlendirin

![[Pasted image 20251216163634.png]]

Python ile Yapay Zekâ Öğrenciler “hold to record” butonuna basarak taş, kâğıt ve makas oyunu için görüntü veri seti oluşturun

![[Pasted image 20251216163657.png]]

“train model” butona basarak görüntü veri setinin eğitim işlemini gerçekleştirin

![[Pasted image 20251216163719.png]]

Modeli eğittikten sonra web cam aracılığıyla modelin doğruluğunu test eder.

![[Pasted image 20251216163738.png]]

## Yapay Zeka kullanımı etkinliği

![[Pasted image 20251216175641.png]]

![[Pasted image 20251216171645.png]]

![[Pasted image 20251216164742.png]]

![[Pasted image 20251216164858.png]]

**Iris Veri Setinin Yüklenmesi**

```python
from sklearn.datasets import load_iris  
iris = load_iris()
```

- `load_iris()` fonksiyonu, Scikit-Learn içinde hazır gelen **Iris çiçeği veri setini** yükler.
- Bu veri seti:
    - **150 adet örnek**
    - **3 farklı çiçek türü** içerir:
        - setosa
        - versicolor
        - virginica

---

 Veri Seti İçeriğinin İncelenmesi

`print(iris.feature_names) print(iris.target_names) print(iris.target) print(iris.data)`

- `feature_names`  Girdi özellikleri (bağımsız değişkenler):    
    - sepal length
    - sepal width
    - petal length
    - petal width
    
- `target_names`  Çiçek sınıfları (etiketler)
    
- `target`  Her veri satırının **hangi sınıfa ait olduğunu** gösteren sayısal etiketler  
    (`0=setosa`, `1=versicolor`, `2=virginica`)
- `data`  
	 Gerçek ölçüm verileri (X)

---

Girdi (X) ve Çıkış (Y) Değerlerinin Ayrılması

X = iris.data  Y = iris.target

- `X`: Modelin öğreneceği **özellikler**
- `Y`: Modelin tahmin etmeye çalışacağı **sınıf etiketleri**

---
 
Eğitim ve Test Veri Setlerinin Ayrılması

```python
from sklearn.model_selection import train_test_split

X_train, X_test, Y_train, Y_test =
train_test_split(X,Y,test_size=0.20,random_state=0 )
```

- Veri seti **eğitim** ve **test** olmak üzere ikiye ayrılır.
- Toplam verinin:
    - `%80`’i eğitim verisi
    - `%20`’si test verisi olarak kullanılır.
- `random_state=0` parametresi, her çalıştırmada **aynı veri bölünmesini** sağlar (tekrar edilebilirlik).

---

 Karar Ağacı (Decision Tree) Modelinin Oluşturulması

```python
from sklearn.tree import DecisionTreeClassifier  
model = DecisionTreeClassifier()
```

- **Decision Tree (Karar Ağacı)**, veriyi **if–else mantığıyla** dallara ayırarak sınıflandıran bir algoritmadır.
- Özellik değerlerine göre kararlar alır ve en uygun sınıfı belirler.
- Anlaşılması ve yorumlanması kolay bir makine öğrenmesi yöntemidir.

---

 Modelin Eğitilmesi
```python
model.fit(X_train, Y_train)
```

- Model, eğitim verilerini kullanarak:
    - Girdi özellikleri (`X_train`) ile
    - Sınıf etiketleri (`Y_train`) arasındaki ilişkiyi öğrenir.
- Bu aşamada model **öğrenme sürecini** tamamlar.

![[Pasted image 20251216180257.png]]

---

 Test Verisi Üzerinde Tahmin Yapılması
 
```python
Y_tahmin = model.predict(X_test)
```

- Eğitilen model, daha önce **hiç görmediği test verileri** için sınıf tahmini yapar.
- Bu tahminler modelin gerçek başarımını ölçmek için kullanılır.

---

 Confusion Matrix (Hata Matrisi)
```python
from sklearn.metrics import confusion_matrix
hata_matrisi = confusion_matrix(Y_test, Y_tahmin) 
print(hata_matrisi)
```

- Confusion Matrix, modelin:
    - **Doğru tahminlerini**
    - **Yanlış tahminlerini**
    - **Satırlar → Gerçek sınıflar**
	- **Sütunlar → Tahmin edilen sınıflar**
- sınıf bazında göstermeyi sağlar.
- Modelin hangi sınıflarda hata yaptığını açıkça görmemize yardımcı olur.


![[Pasted image 20251216172657.png]]

---


 Hata Matrisinin Görselleştirilmesi

```python
import seaborn as sns  
import pandas as pd  
import matplotlib.pyplot as plt

index = ['setosa', 'versicolor', 'virginica'] 
columns = ['setosa', 'versicolor', 'virginica']  
hata_goster = pd.DataFrame(hata_matrisi,columns=columns,index=index )
```

- Hata matrisi, **Pandas DataFrame** formatına dönüştürülür.
- Satırlar: **gerçek sınıflar**
- Sütunlar: **tahmin edilen sınıflar**
---

 Heatmap ile Görsel Gösterim

```python
plt.figure(figsize=(10,6)) 
sns.heatmap(hata_goster, annot=True) 
plt.show()
```

- **Heatmap**, hata matrisini renkli bir şekilde gösterir.
- Büyük değerler koyu, küçük değerler açık renkle ifade edilir.
- `annot=True` parametresi hücrelerin içine sayısal değerleri yazar.

## Dersteki kod 

```python

from sklearn.datasets import load_iris

iris = load_iris() # iris veri setini yükle

#print (iris.feature_names) # Girdi özellikleri (bağımsız değişkenler)   bunler liste mi ? iris bi nesne mi ?

#print (iris.target_names)  # Çiçek sınıfları (etiketler)

#print (iris.target)        # Her veri satırının hangi sınıfa ait olduğunu gösteren sayısal etiketler

#print (iris.data)          # veri setini yazdır

  
  

X = iris.data  # Modelin öğreneceği özellikler
Y = iris.target  # Modelin tahmin etmeye çalışacağı sınıf etiketleri


from sklearn.model_selection import train_test_split

  

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.20, random_state = 0) ## random state nedir ?

print("Eğitim veri seti boyutu=",len(X_train))

print("Test veri seti boyutu=",len(X_test))

  
  

"""

from sklearn.tree import DecisionTreeClassifier

model = DecisionTreeClassifier()

"""

  

from sklearn.neighbors import KNeighborsClassifier

model =  KNeighborsClassifier ()

model.fit(X_train,Y_train)

  
  
  

Y_tahmin = model.predict( X_test )

print("Yolanan x=",X_test[0])

print("Gerçek etiketler=",Y_test)

print("Tahmin edilen etiketler=",Y_tahmin)

  
  
  

from sklearn.metrics import confusion_matrix

hata_matrisi = confusion_matrix(Y_test, Y_tahmin)

print(hata_matrisi)   # bunu yorumla

  
  

import seaborn as sns

import pandas as pd

import matplotlib.pyplot as plt

index = ['setosa','versicolor','virginica']  

columns = ['setosa','versicolor','virginica']  

hata_goster = pd.DataFrame(hata_matrisi,columns,index)  

  
  

plt.figure(figsize=(10,6))  

sns.heatmap(hata_goster, annot=True)

plt.show()

  
  
  
  

"""

  

"""

```
## KNN


![[Pasted image 20251216180126.png]]

![[Pasted image 20251216215411.png]]
## Karar ağaçları

![[Pasted image 20251216180707.png]]
![[Pasted image 20251216181345.png]]
## EKLER

![[Pasted image 20251216181226.png]]
