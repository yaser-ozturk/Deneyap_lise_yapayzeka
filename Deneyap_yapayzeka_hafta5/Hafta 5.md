## Nöron mimarisi benzetimi

![[Pasted image 20260116173707.png]]

![[Pasted image 20260116173727.png]]

Temel bir yapay sinir ağı modelinin matematiksel denklemi : 

![[Pasted image 20260116173903.png]]

Burada;
 y: x’e bağlı bağımlı değişken olup, giriş parametrelerine göre modelden elde edilen doğruluk sonucunu verir.
 x: Bağımsız giriş parametresidir. 
 w: Her bir giriş parametresinin ağırlık değeridir. 
 b: Sabit bir bias değeridir.

---

![[Pasted image 20260116175401.png]]

![[Pasted image 20260116175455.png]]


Toplam paramtrelerin hesabı:
1. **Ağırlık Sayısı:** Bir katmandaki nöron sayısı ile bir sonraki katmandaki nöron sayısının çarpımıdır. Çünkü her nöron, bir sonraki katmandaki tüm nöronlara bir çizgiyle (ağırlıkla) bağlanır.
2. **Bias Sayısı:** Giriş katmanı hariç, ağdaki tüm nöronların (gizli katmanlar + çıkış katmanı) her birinin bir bias değeri vardır.
3. **Toplam Parametre:** Ağırlıklar + Biaslar.



![[Pasted image 20260116174004.png]]

![[Pasted image 20260116181435.png]]
## Activasyon Fonksiyonları

![[Pasted image 20260116175142.png]]

| **Fonksiyon**                 | **Çıkış Aralığı**   | **Temel Özelliği ve Kullanım Alanı**                                                                                                   |
| ----------------------------- | ------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| **Sigmoid**                   | $[0, 1]$            | Olasılıksal sonuçlar üretir. Genelde ikili sınıflandırma (Evet/Hayır) problemlerinde çıkış katmanında tercih edilir.                   |
| **Tanh (Hiperbolik Tanjant)** | $[-1, 1]$           | Sigmoid'e benzer ama "sıfır merkezli"dir. Gizli katmanlarda genellikle Sigmoid'den daha iyi performans gösterir.                       |
| **ReLU**                      | $[0, \infty)$       | Negatif değerleri doğrudan sıfır yapar. Hesaplaması en kolay ve en hızlı fonksiyondur; modern derin öğrenme modellerinin standardıdır. |
| **Leaky ReLU**                | $(-\infty, \infty)$ | ReLU'nun "ölü nöron" (negatiflerin tamamen kaybolması) sorununu çözmek için negatife küçük bir eğim verir.                             |
| **Maxout**                    | Değişken            | Girdilerin en büyüğünü seçer. ReLU ve Leaky ReLU'yu kapsayan daha genel bir yapıdır, öğrenme kapasitesi yüksektir.                     |
| **ELU**                       | $(-\alpha, \infty)$ | Negatif değerler için üstel (exponential) bir eğri çizer. Gürültüye karşı daha dayanıklıdır ve ReLU'ya göre daha hızlı yakınsar.       |


![[Pasted image 20260116175011.png]]

![[Pasted image 20260116180100.png]]

## Örnek Uygulama

Veri seti için indirme linki : https://github.com/deneyapyz/lise/tree/main/Hafta5/ENB2012_data.xlsx

![[Pasted image 20260116175649.png]]

 X1: Rölatif sıkılık 
 X2: Yüzey Alanı 
 X3: Duvar Alanı 
 X4: Çatı Alanı 
 X5: Genel Yükseklik
 X6: Bina yönlendirme 
 X7: Cam Alanı
 X8: Cam Alan Dağılımı 

 Y1: Isıtma Yükü 
 Y2: Soğutma Yükü

![[Pasted image 20260116185032.png]]

---
### Nöral network fonksiyonları için:
1. **Kök (Input):** Veriler girer.
2. **Gövde (Common Path):** Bilgi işlenir ve ortak özellikler çıkarılır.
3. **Dallar (Outputs):** Gövdeden ikiye ayrılır. Bir dal doğrudan meyve verirken (`first_output`), diğer dal önce biraz daha uzayıp (`64 unit Dense`) sonra meyve verir (`second_output`).
#### Giriş Katmanı (Input Layer)

```Python
input_layer = Input(shape=(data_x_train_scaled.shape[1],), name='Input_Layer')
```

- Modelin hangi boyutta veri kabul edeceğini belirler.
- shape[1]` değeri veri setindeki özellik (feature) sayısıdır (bu veri setinde 8). Sondaki virgül `(8,)`, verinin tek boyutlu bir vektör dizisi halinde geleceğini Keras'a bildirir.

#### Ortak Yol (Shared Layers - Backbone)

```Python
common_path = Dense(units=128, activation='relu', name='First_Dense')(input_layer)
common_path = Dropout(0.3)(common_path)
common_path = Dense(units=128, activation='relu', name='Second_Dense')(common_path)
common_path = Dropout(0.3)(common_path)
```

- Her iki çıktının da ortaklaşa kullandığı "ana gövdeyi" oluşturur.
- **Dense (128):** 128 nörondan oluşan tam bağlantılı katman. Verideki karmaşık ilişkileri öğrenir.
- **Activation='relu':** Negatif değerleri sıfırlayarak modelin doğrusal olmayan (non-linear) yapıları öğrenmesini sağlar.
- **Dropout(0.3):** Eğitimin her adımında nöronların %30'unu rastgele kapatır. Bu, modelin veriyi **ezberlemesini (overfitting)** engeller; modeli daha dayanıklı hale getirir.

#### Birinci Çıktı (First Output)

```Python
first_output = Dense(units=1, name='First_Output__Last_Layer')(common_path)
```

- Ortak yoldan gelen bilgiyi kullanarak doğrudan ilk hedef değişkeni (örneğin Isıtma Yükü) tahmin eder.
- **Neden tek nöron?** Çünkü regresyon yapıyorsun ve sonuçta tek bir sayı elde etmek istiyorsun.

#### İkinci Çıktı Yolu (Branching Path)


```Python
second_output_path = Dense(units=64, activation='relu', name='Second_Output__First_Dense')(common_path)
second_output_path = Dropout(0.3)(second_output_path)
second_output = Dense(units=1, name='Second_Output__Last_Layer')(second_output_path)
```

-  İkinci çıktı (örneğin Soğutma Yükü) için ortak yoldan bir dal (branch) ayırır.
- **Farkı ne?** İkinci çıktı için modelin biraz daha "özelleşmiş" bir öğrenme yapması istenmiş. Bu yüzden doğrudan çıkışa gitmek yerine araya 64 nöronluk bir katman daha eklenmiş.

---
### Modelin oluşturulması:

```Python
model = Model(inputs=input_layer, outputs=[first_output, second_output])
print(model.summary())
```

![[Pasted image 20260116184323.png]]
**Param :** **öğrenilmesi gereken toplam parametre (Ağırlık + Bias)** sayısı.
	**First_Dense (1,152):** * Giriş (8) $\times$ Nöron (128) + Bias (128) = $1,024 + 128 = \mathbf{1,152}$.

**Connected to:** Bu katmanın hangi katmandan veri aldığını gösterir.


#### Stratejinin Belirlenmesi

```python
optimizer = tf.keras.optimizers.SGD(learning_rate=0.00001)
model.compile(optimizer=optimizer,
              loss={'First_Output__Last_Layer': 'mse','Second_Output__Last_Layer': 'mse'},
              metrics={'First_Output__Last_Layer':tf.keras.metrics.RootMeanSquaredError(),
'Second_Output__Last_Layer': tf.keras.metrics.RootMeanSquaredError()})
```

Modeli oluşturmak yetmez, ona nasıl "öğreneceğini" söylemen gerekir. `compile` aşaması, modelin başarı kriterlerini belirler.

- **`loss` (Kayıp Fonksiyonu):** Modelin tahminleri ile gerçek değerler arasındaki farkı ölçer. Burada `mse` (Mean Squared Error - Ortalama Kare Hata) kullanılmış. Regresyon (sayısal tahmin) projelerinde (ısıtma yükü tahmini gibi) standarttır.

![[Pasted image 20260116185635.png]]

- **`metrics`:** Eğitim sırasında terminalde göreceğin başarı göstergesidir. `RMSE` (Hata Kareler Ortalamasının Karekökü), hatayı gerçek birim (örneğin kW) cinsinden görmeni sağlar.

---

### 2. `EarlyStopping`: "Yeterince Öğrendin" Gardiyanı

```python
earlyStopping_callback = EarlyStopping(monitor='val_loss',
                              min_delta=0,
                              patience=10,
                              verbose=1)
```

Modeli 500 tur (epoch) eğitebilirsin ama bazen model 100. turda en iyi noktaya ulaşır ve sonrasında veriyi **ezberlemeye (overfitting)** başlar.

- **`monitor='val_loss'`:** Modelin hiç görmediği doğrulama verisindeki hatayı izler.
- **`patience=10`:** Eğer doğrulama hatası 10 tur boyunca daha iyiye gitmezse, "daha fazla eğitme, ezberlemeye başladın" der ve eğitimi durdurur.
- `min_delta=0` İyileşmenin "yeterli" kabul edilmesi için gereken **minimum değişim** miktarıdır.
	Eğer hata payı $0.0000001$ gibi çok küçük bir miktar düşüyorsa, bu gerçek bir iyileşme midir yoksa sadece sayısal bir gürültü mü? `min_delta=0` dersen, hatadaki en ufak bir düşüşü bile (0'dan büyük her iyileşmeyi) "öğrenmeye devam ediyor" kabul eder. 
- `verbose=o` (Bilgi verilsin mi?)  Sessiz mod. Eğitim durduğunda hiçbir mesaj yazmaz.

---

####  Gerçek Eğitim (Antrenman)

```python
history = model.fit(x=data_x_train_scaled, y=data_y_train, verbose=0, epochs=500, batch_size=10,

validation_split=0.3, callbacks=earlyStopping_callback)
```

Bu satır, işlemcinin (CPU/GPU) ter döktüğü yerdir.

- **`epochs=500`:** Veri setinin üzerinden en fazla kaç kez geçileceği.
- **`batch_size=10`:** Modelin ağırlıklarını her 10 veride bir güncellemesi. (Küçük batch, daha hassas ama daha yavaş öğrenme demektir).
- **`validation_split=0.3`:** Eğitim verisinin %30'unu ayırıp kenara koyar. Modeli eğitirken bu %30'luk kısımla sürekli "Bakalım doğru yolda mıyız?" diye test yapar.

---

#### Tahmin yürütme testi

```python
y_pred = np.array(model.predict(data_x_test_scaled))
```

Eğitim bittikten sonra model artık bir "uzman" haline gelmiştir.

- **`data_x_test_scaled`:** Modelin eğitimde hiç görmediği test verilerini verirsin.
- **`y_pred`:** Modelin bu verilere bakarak yaptığı tahminleri (Isıtma ve Soğutma yükü değerleri) içeren bir dizidir.
![[Pasted image 20260116221319.png]]

![[Pasted image 20260116221338.png]]