## Mantık kavramı

 Mantık, insan zihni gibi doğruyu ve yanlışı ayırt etmek için kullanılan bir düşünme disiplinidir. Mantık kavramı doğru (1) veya yanlıştan (0) oluşan bir yargının sonucudur. Örneğin; "İstanbul, Türkiye'nin doğusundadır." cümlesi bir önermedir ve bu önerme yanlıştır. "23 Nisan, Ulusal Egemenlik ve Çocuk Bayramı’dır." önermesi ise doğru bir önermedir. Mantık kavramı insan beyninin problem çözme teknikleri ile oldukça benzerdir. İnsan beyni ilk olarak problemin kaynağı olan faktörleri tespit ettikten sonra, problemin çözümü için çözüm aşamalarını mantıksal olarak gerçekleştirir.

Yapay Zeka Matemetiği

Günlük hayatta bir insanın yaşı, **boyutsuz bir skalar değer** olarak ifade edilir. Buna karşılık, bir insanın fotoğrafı; piksel değerlerinden oluşan ve **iki boyutlu sayısal bir yapı** olan **matris** ile temsil edilir. Matrislerin satır veya sütunlarını oluşturan her bir tek boyutlu yapı ise **vektör** olarak adlandırılır.

**Tensör** kavramı; birden fazla boyutu olan ve daha karmaşık yapıları temsil etmek için kullanılır. Örneğin, bir insanın damarlarındaki kan akışı incelenirken, damarın hacimsel ve yüzeysel alan değişimlerinin birlikte ifade edilmesi gerekmektedir. Bu tür çok boyutlu fiziksel büyüklüklerin modellenmesinde tensörler kullanılır. Benzer şekilde, **zekâ küpü** yapısı da tensöre örnek olarak verilebilir.

![[Pasted image 20251226043157.png]]

![[Pasted image 20251226043128.png]]

![[significance_cartoon.png]]
## Bulanık mantık

Klasik mantıkta:
- Doğru / Yanlış
- 0 / 1

Bulanık mantıkta ise:
- **Kısmen doğru**
- **0 ile 1 arasında değerler**
  
Örnek:  “Su sıcak mı?”
- Klasik: sıcak / değil
- Fuzzy: %30 sıcak, %70 ılık


![[1667299624QZZmuHDQG7.png]]

### Fuzzy ile adım adım

![[Pasted image 20251226025641.png]]

#### **Fuzzification (Bulanıklaştırma)**

**Kesin (crisp) sayısal girişleri**, **bulanık kümelere** dönüştürür.

Örnek:
	
	Giriş:
	`Sıcaklık = 30 °C`
	
	
	Tanımlı bulanık kümeler:
	- Soğuk
	- Ilık
	- Sıcak
	
	Sonuç: `μ(Soğuk) = 0.0 μ(Ilık)  = 0.6 μ(Sıcak) = 0.4`
	
	Yani 28°C hem **ılık** hem **sıcak**, ama farklı oranlarda.

---

Membership Function (Üyelik Fonksiyonları)

Bir değerin **bir fuzzy kümeye ne kadar ait olduğunu** belirler.

![[Membership-functions-examples-16-31-A-membership-function-of-a-fuzzy-set-A-on-a.png]]

![[Fuzzy-logic-example-The-classification-of-some-variable-temperature-is-not-binary-like.png]]

#### Rule Base (Kural Tabanı / Rule Table)

**IF – THEN** şeklinde yazılmış insan mantığına yakın kurallar.

 Örnek Kurallar

`IF sıcaklık IS hot AND hız IS düşük THEN güç IS orta`
`IF sıcaklık IS cold THEN güç IS yüksek`

25 oda
hız 100 rpm
eğer cold sa ve motorumun hızı düşükse ozaman motara verilecek gücü yüksek yap

Rule Table Örneği

| Sıcaklık \ Hız | Düşük  | Orta  | Yüksek    |
| -------------- | ------ | ----- | --------- |
| Soğuk          | Yüksek | Orta  | Düşük     |
| Ilık           | Orta   | Orta  | Düşük     |
| Sıcak          | Düşük  | Düşük | Çok Düşük |
Bu tablo **IF-THEN kurallarının tabloya dökülmüş hali**.
#### Inference Mechanism (Çıkarım Mekanizması)

- Kuralları değerlendirir
- Girişlerin etkisini **çıktı fuzzy kümelerine** yansıtır
- En yaygın yöntemler
	-  Mamdani (En yaygın)
		- AND → **min**
		- OR → **max**
		Örnek:   `IF A AND B → min(μA, μB)`

---

#### Aggregation (Birleştirme)

Birden fazla kuraldan gelen çıktılar **tek bir fuzzy çıktı** haline getirilir.

`max(çıktı1, çıktı2, çıktı3)`

---

#### Defuzzification (Durulaştırma)

- **Bulanık çıkışı**, **tek bir sayısal değere** çevirir.
- En yaygın yöntem: Centroid (Ağırlık Merkezi)
	
	FORMÜL KOY
	
	En kararlı ve en çok kullanılan yöntemdir.
	
	Diğer yöntemler
	
	- Mean of Maximum (MoM)
	- Largest of Maximum (LoM)
	- Smallest of Maximum (SoM)



Önerilen Youtube videoları.

https://www.youtube.com/watch?v=J_Q5X0nTmrA

https://www.youtube.com/watch?v=RuuZ5vKgoqI

Neden Fuzzy Kullanılır?

-  Matematiksel modeli zor sistemler  
-  İnsan mantığına yakın kontrol  
-  Gürültülü sensör verileri  
-  AUV, robot, iklimlendirme, hız kontrolü



## Kod yazımı ve kurulum

![[Pasted image 20251226050534.png]]

Fuzzy logic uygulamamız için bu kütphaneyi enviromentimize eklememiz gerekecek. aşağıdaki kod ile eklenebilir.

```bash
conda activate yapayzeka_env
pip install scikit-fuzzy
```

![[Pasted image 20251226031846.png]]

Kütüphaneler

`import numpy as mat  import skfuzzy as bulanik  from skfuzzy import control as kontrol` 

- `numpy` → Sayısal aralıklar (universe) için
- `skfuzzy` → Membership function (trimf)
- `skfuzzy.control` → Fuzzy sistem (Antecedent, Consequent, Rule)

---

Fuzzy Değişkenlerin Tanımlanması (Antecedent / Consequent)

Giriş Değişkenleri (Antecedent)

```python
bulasik_miktari = kontrol.Antecedent(mat.arange(0, 100, 1), 'bulaşık miktarı')  kirlilik = kontrol.Antecedent(mat.arange(0, 100, 1), 'kirlilik seviyesi')` 
```

- **Bulaşık miktarı** → 0–100 arası
- **Kirlilik seviyesi** → 0–100 arası
- Bunlar **crisp girişlerdir**, birazdan fuzzification yapılacak.

---

Çıkış Değişkeni (Consequent)

`yikama = kontrol.Consequent(mat.arange(0, 180, 1),'yıkama süresi')` 

- Yıkama süresi → 0–180 dakika
- Bu değişken **fuzzy çıkış** olacak, sonra defuzzification ile tek sayıya indirgenecek.

---

Membership Function Tanımları

Bulaşık Miktarı

```python
bulasik_miktari['az'] = bulanik.trimf(bulasik_miktari.universe, [0, 0, 30])  bulasik_miktari['normal'] = bulanik.trimf(bulasik_miktari.universe, [10, 30, 60])  bulasik_miktari['çok'] = bulanik.trimf(bulasik_miktari.universe, [50, 60, 100])
```

- **az** → 0–30
- **normal** → 10–60
- **çok** → 50–100

![[Pasted image 20251226041611.png]]

 Kümeler **üst üste biniyor**, bu fuzzification için gerekli.

---

Kirlilik Seviyesi

```python
kirlilik['az'] = bulanik.trimf(kirlilik.universe[0, 0, 30])  
kirlilik['normal'] = bulanik.trimf(kirlilik.universe, [10, 30, 60])  kirlilik['çok'] = bulanik.trimf(kirlilik.universe, [50, 60, 100])
```

![[Pasted image 20251226041428.png]]

- Bulaşık miktarıyla **aynı yapı**
- Sistem simetrik ve anlaşılır

---

Yıkama Süresi (Çıkış)

```python
yikama['kisa'] = bulanik.trimf(yikama.universe, [0, 0, 50])  
yikama['normal'] = bulanik.trimf(yikama.universe, [40, 50, 100])  
yikama['uzun'] = bulanik.trimf(yikama.universe, [60, 80, 180])
```

- **kısa** → 0–50 dk
- **normal** → 40–100 dk
- **uzun** → 60–180 dk

Yine örtüşme var → yumuşak geçiş.

---

Rule Base (Kural Tabanı)

Burada **9 adet IF–THEN kuralı** tanımlanmış.

```python
kural1 = kontrol.Rule(bulasik_miktari['az'] & kirlilik['az'], yikama['kisa'])
```

Eğer bulaşık az VE kirlilik az ise yıkama süresi kısa

---

 Tüm Kuralların Mantığı
![[Pasted image 20251226042224.png]]

---

Fuzzy Kontrol Sisteminin Oluşturulması

```python
sonuc = kontrol.ControlSystem([kural1, kural2, ..., kural9])
```

- Rule base burada sisteme yükleniyor
- Henüz hesaplama yok

---

Simülasyon Nesnesi

```python
model_sonuc = kontrol.ControlSystemSimulation(sonuc)
```

- Giriş verilerini alıp
- Inference + Defuzzification yapan yapı

---

Girişlerin Verilmesi (Crisp Input)

```python
model_sonuc.input['bulaşık miktarı'] = 50 
model_sonuc.input['kirlilik seviyesi'] = 80
```

- Bulaşık miktarı = **50**
- Kirlilik = **80**

---

Fuzzification + Inference + Defuzzification

```python
model_sonuc.compute()
```

İçeride olanlar:

1. **Fuzzification**
	- 50 → az / normal / çok üyelikleri
	- 80 → normal / çok üyelikleri

1. **Inference (Mamdani)**
    - AND → min
    - Kurallar aktive edilir

2. **Aggregation**    
    - Çıktı fuzzy kümeleri birleştirilir

3. **Defuzzification**
    - Centroid yöntemi
    - Tek bir sayı üretilir

---

**Çıkışın Alınması**

```python
print(model_sonuc.output['yıkama süresi'])
```


**dakika cinsinden** net yıkama süresini verir.

![[Pasted image 20251226041902.png]]


---

Bu Kodun Fuzzy Adımlarla Eşleşmesi

| Fuzzy Adım          | Kodda Neresi          |
| ------------------- | --------------------- |
| Fuzzification       | `trimf`, `input[...]` |
| Membership Function | `bulanik.trimf()`     |
| Rule Base           | `kontrol.Rule()`      |
| Inference           | `compute()`           |
| Defuzzification     | `compute()`           |
| Crisp Output        | `output[...]`         |

----

```Python
import numpy as mat
import skfuzzy as bulanik
from skfuzzy import control as kontrol

bulasik_miktari = kontrol.Antecedent(mat.arange(0, 100, 1), 'bulaşık miktarı')
kirlilik = kontrol.Antecedent( mat.arange(0, 100, 1), 'kirlilik seviyesi')
yikama = kontrol.Consequent(mat.arange(0, 180, 1),'yıkama süresi')

bulasik_miktari['az'] = bulanik.trimf(bulasik_miktari.universe, [0, 0, 30])
bulasik_miktari['normal'] = bulanik.trimf(bulasik_miktari.universe, [10, 30, 60])
bulasik_miktari['çok'] = bulanik.trimf(bulasik_miktari.universe, [50, 60, 100])

kirlilik['az'] = bulanik.trimf(kirlilik.universe, [0, 0, 30])
kirlilik['normal'] = bulanik.trimf(kirlilik.universe, [10, 30, 60])
kirlilik['çok'] = bulanik.trimf(kirlilik.universe, [50, 60, 100])

yikama['kisa'] = bulanik.trimf(yikama.universe, [0, 0, 50])
yikama['normal'] = bulanik.trimf(yikama.universe, [40, 50, 100])
yikama['uzun'] = bulanik.trimf(yikama.universe, [60, 80, 180])

kural1 = kontrol.Rule(bulasik_miktari['az'] & kirlilik['az'], yikama['kisa'])
kural2 = kontrol.Rule(bulasik_miktari['normal'] & kirlilik['az'], yikama['normal'])
kural3 = kontrol.Rule(bulasik_miktari['çok'] & kirlilik['az'], yikama['normal'])
kural4 = kontrol.Rule(bulasik_miktari['az'] & kirlilik['normal'], yikama['normal'])
kural5 = kontrol.Rule(bulasik_miktari['normal'] & kirlilik['normal'], yikama['uzun'])
kural6 = kontrol.Rule(bulasik_miktari['çok'] & kirlilik['normal'], yikama['uzun'])
kural7 = kontrol.Rule(bulasik_miktari['az'] & kirlilik['çok'], yikama['normal'])
kural8 = kontrol.Rule(bulasik_miktari['normal'] & kirlilik['çok'], yikama['uzun'])
kural9 = kontrol.Rule(bulasik_miktari['çok'] & kirlilik['çok'], yikama['uzun'])
sonuc = kontrol.ControlSystem([kural1, kural2, kural3, kural4, kural5, kural6, kural7, kural8,kural9])

model_sonuc = kontrol.ControlSystemSimulation(sonuc)  

model_sonuc.input['bulaşık miktarı'] = 50
model_sonuc.input['kirlilik seviyesi']=80

model_sonuc.compute()
print (model_sonuc.output['yıkama süresi'])
```
## Bulanık mantık Nerede neden kullandık ki şimdi

#### Fuzzy Logic burada neden devreye girer?

**Bulanık mantık**, PID katsayılarını:

- Matematiksel modele gerek duymadan
- İnsan sezgisine dayalı
- Gerçek zamanlı
- Adaptif

olarak belirler. PID’i “akıllı” hale getirir.

#### Fuzzy Logic neden Yapay Zekâdır?

Çünkü fuzzy:

- Kesin kurallara bağlı değildir
- İnsan uzman bilgisini kullanır
- Belirsiz verilerle karar verir
- Doğal dil ile çalışır

 Bu özellikler **yapay zekânın temel tanımıdır**.
Fuzzy Logic, **ilk endüstriyel yapay zekâ yöntemlerinden biridir.**

## Yotube hesap örneği

https://www.youtube.com/watch?v=_H2NPo41vsg&t=776s

![[Pasted image 20251226172256.png]]

![[Pasted image 20251226172344.png]]

![[Pasted image 20251226172428.png]]

![[Pasted image 20251226172532.png]]

![[Pasted image 20251226200825.png]]