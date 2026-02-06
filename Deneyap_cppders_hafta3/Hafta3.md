# Hafta 3

## Class

C++’ta bir sınıf şu temel yapıda tanımlanır:

``` 
class SinifAdi 
{ 
	private:     // Sadece sınıf içinden erişilebilen değişken ve fonksiyonlar 
	public:     // Dışarıdan erişilebilen değişken ve fonksiyonlar 
};

- class → Anahtar kelime, sınıf tanımlamak için.

- SinifAdi → Sınıfın adı (genellikle PascalCase yazılır).

- private: → Bu bölümdeki değişkenlere sadece sınıfın içindeki fonksiyonlar erişebilir.

- public: → Bu bölümdeki değişkenlere main gibi dış kodlar erişebilir.
```



Aşağıdaki kod Online derste yazılan 

```Cpp
#include <iostream>
#include <string>
using namespace std;

// ---------------------------------------------------------
// IHA sınıfı: Bir İHA'nın (İnsansız Hava Aracı) özelliklerini tutan sınıf.
// Bu sınıf içinde yapıcı (constructor), yıkıcı (destructor) ve
// bazı kontrol fonksiyonları bulunmaktadır.
// ---------------------------------------------------------
class IHA {
private:
    int agirlik;   // İHA'nın ağırlığı
    int pil;       // Pil seviyesi
    int gps;       // GPS sinyal gücü
    int ruzgar;    // Rüzgar durumu

public:

    // ---------------------------------------------------------
    // Constructor (Yapıcı Fonksiyon)
    // Nesne oluşturulduğunda otomatik olarak çalışır.
    // Parametre olarak gelen değerlerle değişkenleri başlatır.
    // ---------------------------------------------------------
    IHA(int a, int p, int g, int r) {
        agirlik = a;
        pil = p;
        gps = g;
        ruzgar = r;

        cout << "IHA nesnesi oluşturuldu! -> "
             << "Agirlik: " << agirlik
             << " Pil: " << pil
             << " GPS: " << gps
             << " Ruzgar: " << ruzgar
             << endl;
    }

    // ---------------------------------------------------------
    // Destructor (Yıkıcı Fonksiyon)
    // Nesne işini bitirdiğinde otomatik çalışır.
    // Bellek temizliği burada yapılır.
    // ---------------------------------------------------------
    ~IHA() {
        cout << "IHA nesnesi yok edildi." << endl;
    }

    // ---------------------------------------------------------
    // Tüm bilgileri yazdıran fonksiyon
    // ---------------------------------------------------------
    void goster_tum() {
        cout << "Agirlik: " << agirlik << endl;
        cout << "Pil: " << pil << endl;
        cout << "GPS: " << gps << endl;
        cout << "Ruzgar: " << ruzgar << endl;
        cout << "----------------- " << endl;
    }

    // ---------------------------------------------------------
    // Görev hazır mı kontrolünü yapan fonksiyon
    // Koşullara göre bir string döndürür.
    // ---------------------------------------------------------
    string gorevHazirligiKontrol() {
        if (agirlik > 10)
            return "Ağır yük, kalkış reddedildi!";
        else if (pil < 50)
            return "Pil yetersiz, görev iptal!";
        else if (gps < 50)
            return "GPS sinyali zayıf!";
        else if (ruzgar > 20)
            return "Rüzgar çok şiddetli!";
        else
            return "Görev hazır!";
    }

};

// ---------------------------------------------------------
// MAIN FONKSİYONU
// Burada sınıftan nesneler oluşturuluyor ve fonksiyonlar çağrılıyor.
// ---------------------------------------------------------
int main() {

    // 1) Tek bir nesne oluşturmak
    // Constructor çağrılır.
    IHA ahmet(90, 90, 90, 90);
    ahmet.goster_tum();  // Nesnenin bilgileri yazdırılır
    cout << ahmet.gorevHazirligiKontrol() << endl;

    cout << "\n--- Dizi halinde IHA nesneleri oluşturuluyor ---\n";

    // 2) Birden fazla IHA nesnesi dizi içinde oluşturuluyor
    // Her bir eleman oluşturulduğunda constructor çalışır
    IHA ihalar[6] = {
        IHA(8, 80, 90, 15),
        IHA(12, 60, 70, 18),
        IHA(9, 30, 55, 10),
        IHA(10, 90, 45, 20),
        IHA(11, 55, 80, 45),
        IHA(7, 70, 85, 12)
    };

    // 3) Döngü ile tüm İHA bilgilerini yazdırma
    for (int i = 0; i < 6; i++) {
        ihalar[i].goster_tum();
        cout << ihalar[i].gorevHazirligiKontrol() << endl << endl;
    }

    // Program bittiğinde tüm nesneler için destructor çalışacaktır.
}

```

Çıktı : 

```
IHA nesnesi oluşturuldu! -> Agirlik: 90 Pil: 90 GPS: 90 Ruzgar: 90
Agirlik: 90
Pil: 90
GPS: 90
Ruzgar: 90
-----------------
Görev hazır!

--- Dizi halinde IHA nesneleri oluşturuluyor ---
IHA nesnesi oluşturuldu! -> Agirlik: 8 Pil: 80 GPS: 90 Ruzgar: 15
IHA nesnesi oluşturuldu! -> Agirlik: 12 Pil: 60 GPS: 70 Ruzgar: 18
IHA nesnesi oluşturuldu! -> Agirlik: 9 Pil: 30 GPS: 55 Ruzgar: 10
IHA nesnesi oluşturuldu! -> Agirlik: 10 Pil: 90 GPS: 45 Ruzgar: 20
IHA nesnesi oluşturuldu! -> Agirlik: 11 Pil: 55 GPS: 80 Ruzgar: 45
IHA nesnesi oluşturuldu! -> Agirlik: 7 Pil: 70 GPS: 85 Ruzgar: 12

Agirlik: 8
Pil: 80
GPS: 90
Ruzgar: 15
-----------------
Görev hazır!

Agirlik: 12
Pil: 60
GPS: 70
Ruzgar: 18
-----------------
Ağır yük, kalkış reddedildi!

Agirlik: 9
Pil: 30
GPS: 55
Ruzgar: 10
-----------------
Pil yetersiz, görev iptal!

Agirlik: 10
Pil: 90
GPS: 45
Ruzgar: 20
-----------------
GPS sinyali zayıf!

Agirlik: 11
Pil: 55
GPS: 80
Ruzgar: 45
-----------------
Ağır yük, kalkış reddedildi!

Agirlik: 7
Pil: 70
GPS: 85
Ruzgar: 12
-----------------
Görev hazır!

IHA nesnesi yok edildi.
IHA nesnesi yok edildi.
IHA nesnesi yok edildi.
IHA nesnesi yok edildi.
IHA nesnesi yok edildi.
IHA nesnesi yok edildi.
IHA nesnesi yok edildi.

```


## Fonksiyon çağrıları

Dosya işlemlerine girmeden önce aşağıdaki bilgiler mutlaka bilinmelidir.

---
Aşağıda **C++’ta Call by Value** ve **Call by Reference** kavramları açıklanmıştır.

**1. CALL BY VALUE (Değer ile Çağırma)**
Fonksiyon çağrıldığında **değerin bir kopyası** gönderilir.  
Fonksiyon içinde yapılan değişiklikler **orijinal değişkeni etkilemez.**

- Değişken → kopyalanır → fonksiyonda işlenir
- Ana değişken olduğu gibi kalır

Örnek
```cpp
#include <iostream>
using namespace std;

void arttirValue(int x) {
    x = x + 10;   // sadece x’in kopyası değişir
    cout << "Fonksiyon içi (call by value): " << x << endl;
}

int main() {
    int sayi = 5;
    arttirValue(sayi);
    cout << "Main içi: " << sayi << endl;  // değişmez
}
```

çıktı: 

```yaml
Fonksiyon içi (call by value): 15 Main içi: 5
```

!!!!!!!!!!!!  **Gördüğün gibi main’deki `sayi` değişmedi.**

---

 **2. CALL BY REFERENCE (Referans ile Çağırma)**

Fonksiyona **değişkenin kendisi** gönderilir.  
Fonksiyon içindeki değişiklik **orijinal değişkene yansır.**

- Değişken → adresi gönderilir
- Fonksiyonda yapılan işlem → main’deki değişkeni etkiler

Örnek

```cpp
#include <iostream>
using namespace std;

void arttirReference(int &x) {
    x = x + 10;   // artık gerçek değişken değişiyor
    cout << "Fonksiyon içi (call by reference): " << x << endl;
}

int main() {
    int sayi = 5;
    arttirReference(sayi);
    cout << "Main içi: " << sayi << endl;  // değişti!
}
```

Çıktı :

```
Fonksiyon içi (call by reference): 15
Main içi: 15
```

!!!!!!!!!!!!!!!!!!!!  **Referans (&) kullanıldığı için değişken gerçekten değişti.** 

----

## Dosya işlemleri

Aşağıdaki sınıf yapısı dosya okuma/yazma işlemlerini öğretmek için derste tasarlanmıştır:;

```cpp
#include <iostream>
#include <fstream>      // Dosya işlemleri için gerekli kütüphane
using namespace std;


class IHA {
public:
    // Değişkenler public yapıldı ki main içinde direkt erişilebilsin
    int agirlik;
    int pil;
    int gps;
    int ruzgar;

    IHA(int a = 0, int p = 0, int g = 0, int r = 0) {
        agirlik = a;
        pil = p;
        gps = g;
        ruzgar = r;

        cout << "IHA olusturuldu." << endl;
    }

    void gorevHazirligiKontrol() {
        cout << "IHA durumu: ";
        if (agirlik <= 10 && pil >= 50 && gps == 1 && ruzgar <= 20)
            cout << "Goreve hazir." << endl;
        else
            cout << "Goreve hazir degil." << endl;
    }

    // -----------------------------
    // Dosyaya yazma fonksiyonu
    // ofstream &dosya : CALL BY REFERENCE!
    // Çünkü dosya akışı kopyalanamaz!
    // -----------------------------
    void dosyayaYaz(ofstream &dosya) {

        // << operatörü (insertion operator)
        // Değerleri DOSYANIN içine yazar.
        dosya << agirlik << " "
              << pil << " "
              << gps << " "
              << ruzgar << endl;
    }

    // -----------------------------
    // Dosyadan okuma fonksiyonu
    // ifstream &dosya : CALL BY REFERENCE
    // -----------------------------
    void dosyadanOku(ifstream &dosya) {

        // >> operatörü (extraction operator)
        // Dosyadaki değerleri TEK TEK değişkenlere aktarır.
        dosya >> agirlik >> pil >> gps >> ruzgar;
    }


    ~IHA() {
        cout << "IHA testi tamamlandi ve bellekten silindi." << endl;
    }
};


```



---
 **1. Dosya İşlemleri için Kullanılan Kütüphane**

`#include <fstream>`
- **ifstream** → dosyadan **okuma**
- **ofstream** → dosyaya **yazma**
- **fstream** → hem okuma hem yazma
---
**Dosyaya Yazma İşlemi (ofstream)**
Sınıf İçindeki Fonksiyon:

`void dosyayaYaz(ofstream &dosya)`

- Dosya nesnesi **call by reference** ile gönderiliyor.
- `&` kullanılması çok önemli çünkü:
    - Dosya akışı (file stream) kopyalanamaz.
    - Kopyalansaydı tek bir dosyaya iki akış aynı anda yazmaya çalışırdı → hata.
    - Bu yüzden **dosya akışı referansla gönderilir**.

---
`<<` Operatörü (Out Stream Operator)

`dosya << agirlik << " " << pil << " " << gps << " " << ruzgar << endl;`

Bu işlem şu anlama gelir:
- Değeri **dosyanın içine gönder**.
- `<<` ekran için (cout) de kullanılır, dosya için de.
- Aynı operatör, farklı yerde farklı iş yapar → **operator overloading** sayesinde.

---
**3. Dosyadan Okuma İşlemi (ifstream)**

Sınıf içindeki fonksiyon:

`void dosyadanOku(ifstream &dosya)`

- Yine **call by reference** ile dosya nesnesi alınır.
- Çünkü ifstream de kopyalanamaz.
---
5 . Operatörü (In Stream Operator)

`dosya >> agirlik >> pil >> gps >> ruzgar;`

Bu ifade:

- Dosyadaki ilk sayıyı `agirlik` içine aktar,
- Sonraki sayıyı `pil` içine aktar,
- Sonraki sayıyı `gps` içine aktar,
- Sonraki sayıyı `ruzgar` içine aktar,

şeklinde çalışır.

---
**4. Call by Reference Kullanımının Önemi**

Hem yazma fonksiyonunda:
`void dosyayaYaz(ofstream &dosya)`

Hem okuma fonksiyonunda:
`void dosyadanOku(ifstream &dosya)`

**Dosya nesnesi referansla gönderilmek zorundadır.**  
Çünkü:

- Dosya akışları **kopyalanamaz**. (copy constructor yok)
- Ana dosya akışı üzerinde işlem yapılması gerekir.
- Kopya oluşturulursa dosya iki kez açılmış gibi olur → undefined behavior.

Yani burada **call by reference zorunlu bir kullanım**.

---
main() İçindeki Kullanımlar

```cpp
int main() {

// 6 adet IHA nesnesi oluşturuluyor ve constructor ile başlangıç değerleri veriliyor
    IHA ihalar[6] = {
        IHA(8, 80, 1, 15),
        IHA(12, 60, 1, 18),
        IHA(9, 40, 1, 10),
        IHA(10, 90, 1, 20),
        IHA(11, 55, 1, 25),
        IHA(7, 70, 1, 12)
    };

    // Yazmak için dosya açılıyor
    ofstream dosyaYaz("ihalar.txt");

    // Dosya açılamazsa hata ver ve programı bitir
    if (!dosyaYaz) {
        cout << "Dosya acilamadi!" << endl;
        return 1;
    }

    // Her bir IHA nesnesini dosyaya yaz
    for (int i = 0; i < 6; i++)
        ihalar[i].dosyayaYaz(dosyaYaz);

    // Yazma işlemi bitti, dosya kapatılıyor
    dosyaYaz.close();


    // Şimdi aynı dosya okuma için açılıyor
    ifstream dosyaOku("ihalar.txt");

    // Dosya açılamazsa hata ver
    if (!dosyaOku) {
        cout << "Dosya acilamadi!" << endl;
        return 1;
    }

    // Dosyadan okuyup doldurmak için boş bir IHA dizisi oluşturuluyor
    IHA ihalarOku[6];

    // Dosyadan 6 adet IHA bilgisi okunuyor ve her nesneye aktarılıyor
    for (int i = 0; i < 6; i++)
        ihalarOku[i].dosyadanOku(dosyaOku);

    // Okuma dosyası kapatılıyor
    dosyaOku.close();


    // Okunan IHA'ların görev hazırlıkları kontrol ediliyor
    for (int i = 0; i < 6; i++)
        ihalarOku[i].gorevHazirligiKontrol();

    // Program başarıyla bitti
    return 0;
}

```

## Ek notlar

Yazılımda genel isimlendirmeler aşağıdaki gibi yapılır. Bu ismlendirme kurallarını yazılımcılar projelerinde tercih eder

 **PascalCase**
 
- Her kelime büyük harfle başlar.
- Sınıf isimlerinde çoğunlukla kullanılır.

Örnekler:
- `SinifIsmi`
- `IHAKontrolSistemi`
- `MotorHizSensoru`

 **camelCase**

- İlk kelime küçük, sonraki kelimeler büyük harfle başlar.
- Değişken ve fonksiyon isimlerinde çok yaygın.

Örnekler:

- `motorHizi`
- `pilSeviyesi`
- `gorevKontrolEt()`

 **snake_case**

- Tüm harfler küçük, kelimeler alt çizgi ile ayrılır.

Örnekler:

- `motor_hizi`
- `gps_sinyal_gucu`
- `max_hiz_degeri`

