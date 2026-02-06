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

 Etmen tabanlı çözümlerde yapay zekânın makine öğrenmesi alanında kullanılan öğrenme yöntemi takviyeli öğrenme (reinforcement learning) olarak bilinmektedir. Takviyeli öğrenme gerçek hayattaki yaşayarak öğrenme gibidir. Bu öğrenmede genel olarak şu hususlar söz konusudur:  Öğrenmede ödül/ceza mantığı vardır. 
 
  Ödül olarak algılanacak değerler daha yüksekken, ceza olarak algılanan değerler düşük değerler olarak tasarlanır. 
  
  Takviyeli öğrenme yapan unsurun ödül/ceza değerini belirleyen belli eylemler vardır (duvara çarparsan eksi 1 puan, çarpmazsan -yoluna devam edersen- her zaman artı 1 puan gibi). 
  
  Takviyeli öğrenme yapacak unsur içerisinde bulunduğu ortam/problem için rastgele eylemlerde bulunur ve çok sayıda eylemlerle en iyi tecrübenin kazanılması sağlanır. Etmen tabanlı çözümlerde takviyeli öğrenme için kullanılan temel tekniklerden biri de Q-Öğrenme (Q-Learning) olarak bilinmektedir. 
  
  Q-Öğrenme’de daha önceden tasarlanmış ödül/ceza puanlarının yer aldığı bir tablo kullanılmak suretiyle, başlangıçta içi boş olan yeni bir Q tablosunun en uygun değerlerle doldurulması sağlanır. Şekil 6.2a’da gösterildiği gibi; başlangıç noktası (start) ve bitiş noktası (goal) gösterilen bir problemde, engellerin olduğu her kareye negatif, engelsiz karelere ise pozitif puan verdiği düşünülürse; Q-Öğrenme ile gerçekleştirilen işlem sonucunda, etmenin Şekil 6.2b’de görüldüğü gibi kendisini amaca götüren en uygun yolu bulması sağlanmaktadır. Bu örnekte soldaki görüntü önceden tasarlanmış ödül/ceza (puan) tablosuyken, sağdaki görüntü başlangıçta içi boş olan ama daha sonra en uygun yoldaki değerlerin diğer karelere göre daha yüksek olduğu Q tablosudur.
  
  ![[Pasted image 20260206021225.png]]


Q-Öğrenme’de etmen her seferinde rastgele adımları denemekte ve bu paragrafı takiben verilen formül sayesinde mevcut ödül/ceza tablosunu kullanmak suretiyle gelecek eylemlerinden gelebilecek maksimum değerleri (tıpkı satrançta gelecek hamleleri düşünmek gibi) dikkate almakta; yine öğrenmesini etkileyen diğer parametreleri ve yeni tablodaki ödül/ceza değerini harmanlayarak adım attığı eylemlerdeki değerlerin güncellenmesini sağlamaktadır. Böylelikle iyi eylemler zamanla daha fazla değer kazanırken, kötü eylemlerin değerlerinin zamanla azalması sağlanmaktadır.


![[Pasted image 20260206021352.png]]

en öğrencilere Q-Öğrenme formülünü şu akışa benzer bir şekilde anlatır: 
1. Q-Öğrenme tekniği çalışmadan önce elimizde eylemlerin puanlarını taşıyan bir tablomuz olur. Bununla birlikte içi boş değerlerden (sıfır) oluşan puan tablosuyla aynı satır-sütundan oluşan bir Q tablosu tasarlarız. 
2. Q-Öğrenme için öğrenme oranı ve azalma değeri olarak iki reel sayı belirleriz. Bu sayılar öğrenme gücünü ve şans faktörünü etkiler. 
3. Etmenimiz probleme göre ilk adımını atar.
4. Formülde eylem sonucunda öğrenilen değer kısmını hesaplamak için etmenin gelecek olası adımlarının bütün kombinasyonlarından (ilk başta boş tasarladığımız ama zamanla dolacak Q tablosundan) gelecek en büyük puanı azalma değeri ile çarpar ve eylem puanlarını taşıyan tablodan etmenin attığı adıma tekabül eden ödül değeriyle topladıktan sonra elde ettiğimiz değeri öğrenme oranı ile çarparız. 
5. Dördüncü adım ile elde ettiğimiz değeri Q tablosunda mevcut olan değerin üzerine ekler, ardından (1 – öğrenme oranı) değeriyle çarparız. 
6. Yeni elde ettiğimiz değer, etmenin adım attığı Q tablosu hücresindeki yeni değer olur. 
7. Üçüncü adımdan itibaren bütün işlem adımlarını bir durma sayısı/kriterine kadar tekrarlar, böylece Q tablosunu döngüsel/iteratif bir şekilde güncelleriz.


## 1.4. Çok Etmenli Etkileşimler 

Birden fazla etmenin varlığı çok etmenli modellemeleri ortaya çıkarmaktadır. Bu modelleme özellikle günümüz karmaşık problemlerinin çözümünde daha etkin sonuçlar üretebilmektedir. Çok etmenli problem modellemelerinde etmenler arası ilişkiler, her bir etmenin çevreyle etkileşimi ve bağlı oldukları çevresel düzenlemeler farklılıklar içerebilmekte, böylece karmaşık düzendeki problemlere adaptasyon daha kolay sağlanabilmektedir.

![[Pasted image 20260206021701.png]]


Eğitmen, çok etmenli modellemeye örnek olarak farklı karakterlerin birbiriyle etkileşimde olduğu video oyunlarını örnek verir. Bu noktada, Braw stars ya da platform tabanlı video oyunlarda (örneğin, Mario), karakterlerin nitelikleri, eylemleri, çevrenin düzenlenmesi ve hatta çok etmenli mantıkta farklı karakterler arası ilişkileri etmen tabanlı modelleme odağında öğrenciler ile tartışır.