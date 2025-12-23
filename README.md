# Zipper-128 (Collatz Rolling XOR)

Collatz dizilerinden türetilmiş 128 bitlik kayan anahtar üreten, örnek amaçlı bir simetrik XOR şifreleme uygulaması. Aynı fonksiyon hem şifreleme hem de çözme için kullanılır; algoritma deterministiktir, verilen `n1`, `n2` ve başlangıç değeri `k1` ile aynı çıktıyı üretir.

## Nasıl çalışır?
- `CollatzCipher.process_data` veriyi 16 baytlık bloklar hâlinde işler ve her blok için yeni bir 128 bit anahtar üretir.
- `generate_block_key` iki Collatz yolundan (S1, S2) 64’er bit parite bilgisi toplar, bitleri fermuar (zipper) mantığıyla birbirine geçirir ve 16 baytlık anahtar üretir.
- Başlangıç durumu: `s1 = n1 * k1`, `s2 = n2 * k1`, ardından 50 adımlık “burn-in” uygulanır.
- Çıktı: Girdi baytları ile anahtar baytlarının XOR’lanmış hâli. Aynı `k1` ile çalıştırıldığında tekrar geri çözer.

## Gereksinimler
- Python 3.10+ (standart kütüphane dışında bağımlılık yok)

## Hızlı başlangıç
```bash
python Zipper-128.py
```
Örnek çıktı:
```
Orijinal Mesaj: Bu mesaj Collatz kayan algoritması ile şifrelenmiştir.
K1 (IV): 2755836934
Şifreli (Hex): 703cb35cf64107662c725eff5ded55f3acaf027f2d5e44f9e44126e2af70...
Çözülen Mesaj: Bu mesaj Collatz kayan algoritması ile şifrelenmiştir.
```

## Parametreler
- `n1`, `n2`: Gizli anahtar bileşenleri (büyük tamsayılar).
- `k1`: 32 bitlik IV/başlangıç değeri (her mesaj için rastgele üretin ve alıcıya iletin).
- `burn_in`: İlk adımların atlanması için kullanılan ısınma süresi (varsayılan 50).

## Kütüphane olarak kullanma
Bu dosya adında tire (`-`) içerdiği için doğrudan modül olarak içe aktarmak yerine dosyayı `zipper_128.py` olarak yeniden adlandırmanız önerilir. Sonrasında:
```python
from zipper_128 import CollatzCipher

cipher = CollatzCipher(n1, n2, burn_in=50)
ciphertext = cipher.process_data(b"merhaba", k1)
plaintext = cipher.process_data(ciphertext, k1)
```

## Güvenlik notu
Bu uygulama eğitim/deney amaçlıdır. Modern, incelenmiş kriptografik primitiflerin yerini tutmaz ve üretim ortamlarında kullanılmamalıdır.
