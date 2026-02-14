## Etmen Tabanlı Yapay Zekâ Modelleme Temelleri

Agent yapay zeka 

- YAPAY ZEKA NASIL AKSİYONA ÇEVİRİR  
- SADECE CEVAP ÜRETME İNTERNET KULLAN KARMAŞIK GÖREVLERİ YAP

 Yapay Zekâ kapsamında çevresel faktörlerle etkileşim gerektiren problem çözümlemeleri için tasarlanmış çeşitli yaklaşımlar bulunmaktadır. Bu yaklaşımların özünde şu ana dek değinilen farklı Yapay Zekâ algoritmalarının etkileşimsel fonksiyonları içerecek şekilde tasarlanması yer almaktadır. Buna göre, çevreyle etkileşen Yapay Zekâ unsurları kısaca etmen ya da İngilizce karşılığından esinlenerek ajan (agent) olarak adlandırılmaktadır. 

Görsleden anlaşılacağı gibi anlaşılacağı üzere bir etmen, çevresiyle etkileşime girip girdiği etkileşim sonucunda elde ettiği bulgulara göre dönütlerde (yani eylemlerde) bulunabilecek şekilde tasarlanmaktadır. Bir etmenin eylemlerine karar verme aşamasında içerisinde bulunduğu durum ve çevreden aldığı ödül/ceza dönütleri etkili olmakta, bunlar gelecek durumları da yönlendirmektedir. Buradan hareketle, özellikle kolektif, çok sayıda unsurun bir araya gelerek çözüm üretmesi gereken problem durumlarında birden fazla etmen de kullanılabilmektedir. Genel olarak bu yöndeki Yapay Zekâ tabanlı çözüm yaklaşımlarına etmen tabanlı Yapay Zekâ, bu yöndeki çözüm süreçlerinin tasarımına da etmen tabanlı modelleme adı verilmektedir. 

![[Pasted image 20260206015707.png]]

**Örnek: Sıcak Nesne Deneyimi** Bir çocuğun sıcak bir nesneye dokunması bir eylemdir. Canının yanması (ceza/negatif geri bildirim), çocuğun "sıcağa dokunmamalıyım" bilgisini öğrenmesini sağlar. Bu, etmen tabanlı modellemenin temelidir.


LLm ler (KAHİN)
- Kendi mağarasında (eğitim verisi ile oturur)
- Sadece bildiklerini (statik bilgileri söylerler)
- Bugün hava nası ne bilim 2024 den sonrasına ulasamıyorum
  
Generatif yapay zeka AI agent lar

- Beyin ve Araç kutusu güç daha çok araç kutusu neleri olduğuna bağlı robotlar için sensör chat gpt için hangi siteler hangi bilgiler
- Bu gün hava nası mağradan çıkar hava durumu aracını kullanır bilgiyi alır eleştirir yorumlar cevap verir.

Temel döngü : 


![[Pasted image 20260206040928.png]]


![[Pasted image 20260206040038.png]]

![[Pasted image 20260206041942.png]]

## Etmen Tabanlı Modellemede Problem Tasarımı 

Etmen tabanlı çözümlerin çalışacağı problemlerde, etkin çözüm elde etmek adına birtakım faktörlerin/bileşenlerin dikkate alınması ve bunlar altında tanımlamalar yapılması gerekmektedir. İlgili faktörleri/bileşenleri genel olarak şöyle ifade edebiliriz: 

Robot süpürgesi örneğini de irdeler. Robot süpürgeyi bir etmen olarak kabul edersek; kamera, kızılötesi gibi sensörler ile çevre algılama sağlanırken, dinamik tepki vericiler olarak çeşitli motorlar, fırçalar, mekanik kollar vs. ile problem çözümü (çevreyi temizlemek/süpürmek) sağlanır.

- Etmen Sayısı: Çözümde kullanılacak etmenlerin sayısı, tek bir etmenin mi yoksa çok sayıda etmenin mi (kolektif bir şekilde) çalışacağı belirlenmelidir. Bazı problemler tek bir etmen ile kolayca çözülebilirken, bazı problemler de çok sayıda etmenin hem çevreyle hem de birbirleriyle iletişim halinde olarak çalışmasını ve çözüme ulaşmasını gerekli kılmaktadır. 
  
  YAZAR - ELEŞTİRMEN - ARAŞTIRMACI - PROJE 

	![[Pasted image 20260206042545.png]]
- Etmen Nitelikleri: Çözümde yer alacak etmenlerin sahip olacakları muhtemel parametreler aynı zamanda etmen nitelikleri olarak bilinmektedir. Bu parametreler, etmenlerin eylemlerine, muhakemelerine ve çevreyle ya da diğer unsurlarla (örneğin diğer etmenler) etkileşimlerine yön verecek, düzenlenebilir değerler olmaktadır. 

- Etmen Eylemleri: Etmen eylemleri, ilgili etmenlerin çevreyle etkileşimleri ve geçerli nitelik değerleri üzerinden karar süreçlerini işletmelerini ve hatta eylemde bulunmalarını içermektedir. Bu eylem yapıları aslında birer fonksiyon olarak tanımlanmaktadır. 

- Çevre: Etmenlerin içerisinde bulundukları çevrenin, en iyi etmen etkileşimleri için sınırları ve karakteristik nitelikleri ile tanımlanmaları gerekmektedir.
  
| **Bileşen**                  | **Açıklama**                                               | **Örnek (Robot Süpürge)**                           |
| ---------------------------- | ---------------------------------------------------------- | --------------------------------------------------- |
| **Etmen Sayısı**             | Tek bir etmen mi yoksa kolektif çalışan çoklu etmenler mi? | Tek bir süpürge veya sürü halinde çalışan robotlar. |
| **Etmen Nitelikleri - Tool** | Etmenin sahip olduğu sabit veya değişken parametreler.     | Pil seviyesi, emiş gücü, koordinat bilgisi.         |
| **Etmen Eylemleri**          | Etmenin yapabileceği fonksiyonel hareketler.               | İleri gitme, sağa dönme, fırçayı çalıştırma.        |
| **Çevre**                    | Etmenin hareket ettiği sınırları belirlenmiş alan.         | Evin odaları, duvarlar, halılar.                    |

 Benzer şekilde; bir insan olarak da çevreyle etkileşimlerimiz neticesinde kararlar alabilen ve eylemler gerçekleştiren unsurlar olarak etmen tabanlı modellemeyle olan benzerliklerimiz konusunda örnekler (örneğin markette kasiyer ile olan iletişimimiz, bir çocuğun sıcak bir unsura elini değdirdiği zaman ulaştığı tecrübe: ‘sıcağa dokunmamalıyım’…vs.) vererek, etmen kavramına ilişkin pekiştirici örnekleri de vurgulayarak, öğrencilerin kavramları daha iyi anlamasını sağlayacaktır.

İfade edilen unsurlar ile etmenlerin içerisinde bulunacağı problemin de tanımlanması gerekmektedir. Problemle ilgili olarak şu tanım faktörleri önemlidir: 

Problem Kısıtları: Problem ile ilgili çözümü temsil eden parametrelerin hangi kısıtlar altında olacağı, etmen davranışları neticesindeki çıktıların da gidişatını belirlemektedir. 

Çevredeki Dinamik Unsurlar: Etmenlerin eylemleri neticesinde durumları değişebilecek dinamik çevrenin söz konusu olacağı gibi, çevrede yer alacak ve etmenlerin gelecek davranışlarını şekillendirecek başka dinamik unsurlar da söz konusu olabilmektedir. Özellikle çok etmenli modellemelerde başka etmenler de dinamik unsurlar olarak kabul edilmektedir. Yine tek veya çok etmenli problem çözümlerinde çevreyle bağlantılı değişken parametreli unsurlar da problem çözümünü benzetim odaklı problemler için daha uyumlu hale getirebilmektedir.

Ödül/Ceza Fonksiyonları: Etmenlerin eylemleri sonrasında gelecek kararlarını ve eylemlerini düzenleyecek birtakım çevresel ödüller veya cezalar dönüt olarak verilebilmektedir. Bu ödül ve cezalar çevredeki bazı unsurlarla etkileşimden doğabileceği gibi, etmenler için tanımlanan kurallarla ya da etmenin çevrede hareket halinde olduğu her aşamada uygulanabilmektedir.


1. **Problem Kısıtları:** Etmenin hareket alanını ve davranış sınırlarını belirler (Örn: Duvarlar, merdiven boşlukları).
2. **Dinamik Unsurlar:** Çevrede zamanla değişen objeler (Örn: Hareket eden insanlar, yer değiştiren eşyalar).
3. **Ödül/Ceza Fonksiyonları:** Etmenin "doğru" yolu bulması için kullanılan puanlama sistemidir.


## Q-Öğrenme ile Öğrenen Etmen Modelleme

 Etmen tabanlı çözümlerde yapay zekânın makine öğrenmesi alanında kullanılan öğrenme yöntemi takviyeli öğrenme (reinforcement learning) olarak bilinmektedir. Takviyeli öğrenme gerçek hayattaki yaşayarak öğrenme gibidir. Bu öğrenmede genel olarak şu hususlar söz konusudur: Öğrenmede ödül/ceza mantığı vardır. 
 
  Ödül olarak algılanacak değerler daha yüksekken, ceza olarak algılanan değerler düşük değerler olarak tasarlanır. 
  
  Takviyeli öğrenme yapan unsurun ödül/ceza değerini belirleyen belli eylemler vardır (duvara çarparsan eksi 1 puan, çarpmazsan -yoluna devam edersen- her zaman artı 1 puan gibi). 
  
  Takviyeli öğrenme yapacak unsur içerisinde bulunduğu ortam/problem için rastgele eylemlerde bulunur ve çok sayıda eylemlerle en iyi tecrübenin kazanılması sağlanır. Etmen tabanlı çözümlerde takviyeli öğrenme için kullanılan temel tekniklerden biri de Q-Öğrenme (Q-Learning) olarak bilinmektedir. 
  
  Q-Öğrenme’de daha önceden tasarlanmış ödül/ceza puanlarının yer aldığı bir tablo kullanılmak suretiyle, başlangıçta içi boş olan yeni bir Q tablosunun en uygun değerlerle doldurulması sağlanır.
  
Şekil 6.2a’da gösterildiği gibi; başlangıç noktası (start) ve bitiş noktası (goal) gösterilen bir problemde, engellerin olduğu her kareye negatif, engelsiz karelere ise pozitif puan verdiği düşünülürse; Q-Öğrenme ile gerçekleştirilen işlem sonucunda, etmenin Şekil 6.2b’de görüldüğü gibi kendisini amaca götüren en uygun yolu bulması sağlanmaktadır. 

Bu örnekte soldaki görüntü önceden tasarlanmış ödül/ceza (puan) tablosuyken, sağdaki görüntü başlangıçta içi boş olan ama daha sonra en uygun yoldaki değerlerin diğer karelere göre daha yüksek olduğu Q tablosudur.
  
  ![[Pasted image 20260206021225.png]]


Q-Öğrenme’de etmen her seferinde rastgele adımları denemekte ve bu paragrafı takiben verilen formül sayesinde mevcut ödül/ceza tablosunu kullanmak suretiyle gelecek eylemlerinden gelebilecek maksimum değerleri (tıpkı satrançta gelecek hamleleri düşünmek gibi) dikkate almakta; yine öğrenmesini etkileyen diğer parametreleri ve yeni tablodaki ödül/ceza değerini harmanlayarak adım attığı eylemlerdeki değerlerin güncellenmesini sağlamaktadır. Böylelikle iyi eylemler zamanla daha fazla değer kazanırken, kötü eylemlerin değerlerinin zamanla azalması sağlanmaktadır.

![[Pasted image 20260206053140.png]]

![[Pasted image 20260206021352.png]]

![[Pasted image 20260206053608.png]]


1. Q-Öğrenme tekniği çalışmadan önce elimizde eylemlerin puanlarını taşıyan bir tablomuz olur. Bununla birlikte içi boş değerlerden (sıfır) oluşan puan tablosuyla aynı satır-sütundan oluşan bir Q tablosu tasarlarız. 
   
![[Pasted image 20260206053241.png]]               

![[Pasted image 20260206053323.png]]

2. Q-Öğrenme için öğrenme oranı Learning Rate ve azalma (gamma) değeri olarak iki reel sayı belirleriz. Bu sayılar öğrenme gücünü ve şans faktörünü etkiler. 
3. Etmenimiz probleme göre ilk adımını atar.
4. Formülde eylem sonucunda öğrenilen değer kısmını hesaplamak için etmenin gelecek olası adımlarının bütün kombinasyonlarından (ilk başta boş tasarladığımız ama zamanla dolacak Q tablosundan) gelecek en büyük puanı azalma değeri ile çarpar ve eylem puanlarını taşıyan tablodan etmenin attığı adıma tekabül eden ödül değeriyle topladıktan sonra elde ettiğimiz değeri öğrenme oranı ile çarparız. 
5. Dördüncü adım ile elde ettiğimiz değeri Q tablosunda mevcut olan değerin üzerine ekler, ardından (1 – öğrenme oranı) değeriyle çarparız. 
6. Yeni elde ettiğimiz değer, etmenin adım attığı Q tablosu hücresindeki yeni değer olur. 
   ![[Pasted image 20260206053750.png]]

7. Üçüncü adımdan itibaren bütün işlem adımlarını bir durma sayısı/kriterine kadar tekrarlar, böylece Q tablosunu döngüsel/iteratif bir şekilde güncelleriz.

![[Pasted image 20260206054242.png]]

![[Pasted image 20260206054302.png]]

![[Pasted image 20260206054320.png]]


## Uygulama ve kod

```python

import numpy as np

ortam_satir_sayisi = 11
ortam_sutun_sayisi = 11   # 11 e 11 lik bir kare matris 

q_degerleri = np.zeros((ortam_satir_sayisi, ortam_sutun_sayisi, 4))
# başlangıç tablosunun yazımı 3 de matris 11 satır 11 stun 4 derinlik

hareketler = ['yukari', 'sag', 'asagi', 'sol'] # hareketler bir string listede

oduller = np.full((ortam_satir_sayisi, ortam_sutun_sayisi), -100.)
# ödül matrisi yazımı 11 satır  11 sutun haritada her yeri - 100 yaptım ki baslangıcta her yer siyah 

oduller[0, 5] = 100.
# harimanın büyük ödül noktasını belirledim yani ödül tablomda her yer -100 birtek bu nokta 100

gecitler = {}
# bu kod satırı ile güvenli yollar belirlenir
gecitler[1] = [i for i in range(1, 10)]  
gecitler[2] = [1, 7, 9]
gecitler[3] = [i for i in range(1, 8)]
gecitler[3].append(9)
gecitler[4] = [3, 7]
gecitler[5] = [i for i in range(11)]
gecitler[6] = [5]
gecitler[7] = [i for i in range(1, 10)]
gecitler[8] = [3, 7]
gecitler[9] = [i for i in range(11)]
"""
{
1: [1, 2, 3, 4, 5, 6, 7, 8, 9], 
2: [1, 7, 9], 
3: [1, 2, 3, 4, 5, 6, 7, 9], 
4: [3, 7], 
5: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 
6: [5], 
7: [1, 2, 3, 4, 5, 6, 7, 8, 9], 
8: [3, 7], 
9: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
}
"""

```

![[Pasted image 20260206055526.png]]


```python
  

for satir_indeks in range(1, 10):    # satır indeks 1 den 9 a kadar git

  for sutun_indeks in gecitler[satir_indeks]: # dictionarynin içindeki listelere ulaşır mesela 2 key için sutun indeks [1, 7, 9] u kullanır ve buradaki yerlere -1 atanır

    oduller[satir_indeks, sutun_indeks] = -1.

  

for satir in oduller:
  print(satir)
"""
[-100. -100. -100. -100. -100.  100. -100. -100. -100. -100. -100.]
[-100.   -1.   -1.   -1.   -1.   -1.   -1.   -1.   -1.   -1. -100.]
[-100.   -1. -100. -100. -100. -100. -100.   -1. -100.   -1. -100.]
[-100.   -1.   -1.   -1.   -1.   -1.   -1.   -1. -100.   -1. -100.]
[-100. -100. -100.   -1. -100. -100. -100.   -1. -100. -100. -100.]
[-1.     -1.   -1.   -1.   -1.   -1.   -1.   -1.   -1.   -1.   -1.]
[-100. -100. -100. -100. -100.   -1. -100. -100. -100. -100. -100.]
[-100.   -1.   -1.   -1.   -1.   -1.   -1.   -1.   -1.   -1. -100.]
[-100. -100. -100.   -1. -100. -100. -100.   -1. -100. -100. -100.]
[-1.     -1.   -1.   -1.   -1.   -1.   -1.   -1.   -1.    -1.  -1.]
[-100. -100. -100. -100. -100. -100. -100. -100. -100. -100. -100
"""

```



```python
# bool deger dönduru bulunan indeks odullerde neye karşılık geliyor
def engel_mi(gecerli_satir_indeks, gecerli_sutun_indeks):
  if oduller[gecerli_satir_indeks, gecerli_sutun_indeks] == -1.:
    return False
  else:
    return True

```


```python

def baslangic_belirle():

  gecerli_satir_indeks = np.random.randint(ortam_satir_sayisi)
  gecerli_sutun_indeks = np.random.randint(ortam_sutun_sayisi)
  # random bir oduller harıtasında yer ata ottam_satir_sayisi global degiskenler

  while engel_mi(gecerli_satir_indeks, gecerli_sutun_indeks): # koridora mı denk geldim duvaramı eger duvarsa tekrar random bir noktaya at

    gecerli_satir_indeks = np.random.randint(ortam_satir_sayisi)
    gecerli_sutun_indeks = np.random.randint(ortam_sutun_sayisi)

  return gecerli_satir_indeks, gecerli_sutun_indeks # duvar degilse bu döner

```


```python

def sonraki_noktaya_git(gecerli_satir_indeks, gecerli_sutun_indeks, hareket_indeks):

  yeni_satir_indeks = gecerli_satir_indeks # hiçbir hareket olmassa eski yerinde kal
  yeni_sutun_indeks = gecerli_sutun_indeks# hiçbir hareket olmassa eski yerinde kal

  if hareketler[hareket_indeks] == 'yukari' and gecerli_satir_indeks > 0:
# köşedemiyim kontrolü yapmak icin 0 . satırda yukarıya gitmesi eger haerek istegim yukarıya ise
    yeni_satir_indeks -= 1 # satırımı azalttım yani 

  elif hareketler[hareket_indeks] == 'sag' and gecerli_sutun_indeks < ortam_sutun_sayisi - 1:

    yeni_sutun_indeks += 1

  elif hareketler[hareket_indeks] == 'asagi' and gecerli_satir_indeks < ortam_satir_sayisi - 1:

    yeni_satir_indeks += 1

  elif hareketler[hareket_indeks] == 'sol' and gecerli_sutun_indeks > 0:

    yeni_sutun_indeks -= 1

  return yeni_satir_indeks, yeni_sutun_indeks

```


```python
def en_kisa_mesafe(basla_satir_indeks, basla_sutun_indeks): # maşiyet etkin bir sonraki noktam neresi olsun

  if engel_mi(basla_satir_indeks, basla_sutun_indeks):
    return [] # zaten engelin ustundeysem bos dizi gönder

  else:

    gecerli_satir_indeks, gecerli_sutun_indeks = basla_satir_indeks, basla_sutun_indeks

    en_kisa = []

    en_kisa.append([gecerli_satir_indeks, gecerli_sutun_indeks]) # en kısa listesine suanki konumu jayıt ettim

    while not engel_mi(gecerli_satir_indeks, gecerli_sutun_indeks):
    # engel noktası bulana kadar tara 

      hareket_indeks = sonraki_hareket_belirle(gecerli_satir_indeks, gecerli_sutun_indeks, 1.)

      gecerli_satir_indeks, gecerli_sutun_indeks = sonraki_noktaya_git(gecerli_satir_indeks,gecerli_sutun_indeks, hareket_indeks)

      en_kisa.append([gecerli_satir_indeks, gecerli_sutun_indeks])

    return en_kisa

```


```python
# Epsilon-Greedy kullanılır 
def sonraki_hareket_belirle(gecerli_satir_indeks, gecerli_sutun_indeks, epsilon):

  if np.random.random() < epsilon:  # np.random.random() 0 ile 1 arasında rastgele bir sayı üretir.

# np.argmax(...) Mevcut konumdaki Q-tablosuna bakar ve 4 hareket (yukarı, aşağı, sağ, sol) arasından en yüksek puana (değere) sahip olan hareketin indeksini döndü

    return np.argmax(q_degerleri[gecerli_satir_indeks, gecerli_sutun_indeks])
  else:

    return np.random.randint(4) # 0 ile 4 arası sayı 
```

Epsilon değerini nasıl seçtiğin, etmenin karakterini belirler:

- epsilon = 1.0 Etmen her zaman bildiği en iyi yolu seçer (Hiç risk almaz).
- epsilon = 0.0 Etmen her zaman rastgele hareket eder (Öğrenemez, sadece gezinir).
- **Gerçek Uygulama:** Genelde eğitim başında epsilon düşük tutulur (çok keşif), eğitim ilerledikçe epsilon artırılır (öğrenileni kullanma).

```python

epsilon = 0.9  # haereket seçiminde randomluk vermek için
azalma_degeri = 0.9
ogrenme_orani = 0.9

  

for adim in range(1000):  # bin iterasyonla q tablomuzun yazımı gerçekleşmektedir.

  satir_indeks, sutun_indeks = baslangic_belirle() # duvar olmayan random bir nokta

  while not engel_mi(satir_indeks, sutun_indeks): # engele gidene kadar 

    hareket_indeks = sonraki_hareket_belirle(satir_indeks, sutun_indeks, epsilon)

    eski_satir_indeks, eski_sutun_indeks = satir_indeks, sutun_indeks

    satir_indeks, sutun_indeks = sonraki_noktaya_git(satir_indeks, sutun_indeks, hareket_indeks)

    odul = oduller[satir_indeks, sutun_indeks]

    eski_q_degeri = q_degerleri[eski_satir_indeks, eski_sutun_indeks, hareket_indeks]

    fark = odul + (azalma_degeri * np.max(q_degerleri[satir_indeks, sutun_indeks])) - eski_q_degeri

    yeni_q_degeri = eski_q_degeri + (ogrenme_orani * fark) # q tablosunda güncellenecek deger bulundu

    q_degerleri[eski_satir_indeks, eski_sutun_indeks, hareket_indeks] = yeni_q_degeri # q tablosu guncellendi

```


```python
print('Eğitim tamamlandı.') # okuma ve ekrana yazdırma

ogr_sonrasi_satir = input('Robotun harekete başlayacağı satır indeksini giriniz:')
ogr_sonrasi_sutun = input('Robotun harekete başlayacağı stun indeksini giriniz:')

print('Kargo noktasına giden rota:',
      en_kisa_mesafe(int(ogr_sonrasi_satir), int(ogr_sonrasi_sutun)))
      # okunan deger ler string sen burda int e cast ediyorsun

```


## Açıklamasız kod

```python
import numpy as np

ortam_satir_sayisi = 11

ortam_sutun_sayisi = 11

q_degerleri = np.zeros((ortam_satir_sayisi, ortam_sutun_sayisi, 4))

hareketler = ['yukari', 'sag', 'asagi', 'sol']

oduller = np.full((ortam_satir_sayisi, ortam_sutun_sayisi), -100.)

oduller[0, 5] = 100.

gecitler = {}

  

gecitler[1] = [i for i in range(1, 10)]

gecitler[2] = [1, 7, 9]

gecitler[3] = [i for i in range(1, 8)]

gecitler[3].append(9)

gecitler[4] = [3, 7]

gecitler[5] = [i for i in range(11)]

gecitler[6] = [5]

gecitler[7] = [i for i in range(1, 10)]

gecitler[8] = [3, 7]

gecitler[9] = [i for i in range(11)]

  
  
  

for satir_indeks in range(1, 10):

  for sutun_indeks in gecitler[satir_indeks]:

    oduller[satir_indeks, sutun_indeks] = -1.

  

for satir in oduller:

  print(satir)

  
  

def engel_mi(gecerli_satir_indeks, gecerli_sutun_indeks):

  if oduller[gecerli_satir_indeks, gecerli_sutun_indeks] == -1.:

    return False

  else:

    return True

  
  
  

def baslangic_belirle():

  gecerli_satir_indeks = np.random.randint(ortam_satir_sayisi)

  gecerli_sutun_indeks = np.random.randint(ortam_sutun_sayisi)

  while engel_mi(gecerli_satir_indeks, gecerli_sutun_indeks):

    gecerli_satir_indeks = np.random.randint(ortam_satir_sayisi)

    gecerli_sutun_indeks = np.random.randint(ortam_sutun_sayisi)

  return gecerli_satir_indeks, gecerli_sutun_indeks

  
  
  

def sonraki_hareket_belirle(gecerli_satir_indeks, gecerli_sutun_indeks, epsilon):

  if np.random.random() < epsilon:

    return np.argmax(q_degerleri[gecerli_satir_indeks, gecerli_sutun_indeks])

  else:

    return np.random.randint(4)

  
  
  

def sonraki_noktaya_git(gecerli_satir_indeks, gecerli_sutun_indeks, hareket_indeks):

  yeni_satir_indeks = gecerli_satir_indeks

  yeni_sutun_indeks = gecerli_sutun_indeks

  if hareketler[hareket_indeks] == 'yukari' and gecerli_satir_indeks > 0:

    yeni_satir_indeks -= 1

  elif hareketler[hareket_indeks] == 'sag' and gecerli_sutun_indeks < ortam_sutun_sayisi - 1:

    yeni_sutun_indeks += 1

  elif hareketler[hareket_indeks] == 'asagi' and gecerli_satir_indeks < ortam_satir_sayisi - 1:

    yeni_satir_indeks += 1

  elif hareketler[hareket_indeks] == 'sol' and gecerli_sutun_indeks > 0:

    yeni_sutun_indeks -= 1

  return yeni_satir_indeks, yeni_sutun_indeks

  
  
  

def en_kisa_mesafe(basla_satir_indeks, basla_sutun_indeks):

  if engel_mi(basla_satir_indeks, basla_sutun_indeks):

    return []

  else:

    gecerli_satir_indeks, gecerli_sutun_indeks = basla_satir_indeks, basla_sutun_indeks

    en_kisa = []

    en_kisa.append([gecerli_satir_indeks, gecerli_sutun_indeks])

    while not engel_mi(gecerli_satir_indeks, gecerli_sutun_indeks):

      hareket_indeks = sonraki_hareket_belirle(gecerli_satir_indeks, gecerli_sutun_indeks, 1.)

      gecerli_satir_indeks, gecerli_sutun_indeks = sonraki_noktaya_git(gecerli_satir_indeks,gecerli_sutun_indeks, hareket_indeks)

      en_kisa.append([gecerli_satir_indeks, gecerli_sutun_indeks])

    return en_kisa

  

epsilon = 0.9

azalma_degeri = 0.9

ogrenme_orani = 0.9

  

for adim in range(1000):

  satir_indeks, sutun_indeks = baslangic_belirle()

  while not engel_mi(satir_indeks, sutun_indeks):

    hareket_indeks = sonraki_hareket_belirle(satir_indeks, sutun_indeks, epsilon)

    eski_satir_indeks, eski_sutun_indeks = satir_indeks, sutun_indeks

    satir_indeks, sutun_indeks = sonraki_noktaya_git(satir_indeks, sutun_indeks, hareket_indeks)

    odul = oduller[satir_indeks, sutun_indeks]

    eski_q_degeri = q_degerleri[eski_satir_indeks, eski_sutun_indeks, hareket_indeks]

    fark = odul + (azalma_degeri * np.max(q_degerleri[satir_indeks, sutun_indeks])) - eski_q_degeri

    yeni_q_degeri = eski_q_degeri + (ogrenme_orani * fark)

    q_degerleri[eski_satir_indeks, eski_sutun_indeks, hareket_indeks] = yeni_q_degeri

print('Eğitim tamamlandı.')

  

ogr_sonrasi_satir = input('Robotun harekete başlayacağı satır indeksini giriniz:')

ogr_sonrasi_sutun = input('Robotun harekete başlayacağı stun indeksini giriniz:')

  

print('Kargo noktasına giden rota:',

      en_kisa_mesafe(int(ogr_sonrasi_satir), int(ogr_sonrasi_sutun)))
```