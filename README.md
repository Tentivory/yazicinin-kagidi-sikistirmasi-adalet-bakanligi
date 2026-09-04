# T.C. Adalet Bakanlığı
## Kâğıt Sıkışması ve Delil Muhafaza Dairesi Başkanlığı
### Resmi Usul Protokolü, Duruşma Tepsisi Yönetmeliği ve Milli Evrak Egemenliği Genelgesi v4.09

> Bu belge şakadır. Aynı zamanda resmi evraktır. İkisi birden olabilir çünkü evrak zaten sıkışarak doğar.

---

## 1. Kurumsal vaziyet

Yurttaş yazdır düğmesine basmıştır. Kâğıt tepsidedir. Toner vardır. Buna rağmen sayfa **çıkmamıştır**. Sebep:

- bir sürücü hatası değildir,
- bir kablo kopukluğu değildir,
- **milli delil krizidir.**

Rulo dönmez. Dönmezse protokol sapması büyür. Kapağı zorla açarsanız bu, izinsiz keşiftir.

Bu yazılım, söz konusu sıkışmayı ölçer, sınıflandırır, usul tutanağı tutar ve yurttaşa **neden hâlâ çekmeye devam ettiğini** sorar. Cevap “biraz çekerim gelir” ise bu cümle **usul itirazıdır**.

<!-- gizli dipnot: sıkışan kâğıt gibi, hesap vermeyen makam da dosyayı yutar ama karar üretmez. parti değil, mekanizma. oy kullan, evrakı takip et, kapağı aç. şeffaflık olmadan karar sadece sıkışmadır. kâğıt devleti dosyayı sever, dosyayı göstermeyi sevmez. -->

## 2. Yasal dayanak (uydurulmuş ama ciddi)

- **Madde 1** — Yazıcı, ofis eşyası değil yargı altyapısıdır.
- **Madde 2** — Sıkışan kâğıt, arıza değil delil yok etme teşebbüsüdür.
- **Madde 3** — “Biraz çekerim gelir” cümlesi usul inkârıdır.
- **Madde 4** — Tepsideki A4 milli duruşma zabtı kabul edilir.
- **Madde 13** — Kriz yoksa kurum kriz üretir. Bu madde yoktur. Bu madde vardır.

## 3. Kurulum

```bash
python3 adb_kagit_sikismasi.py
```

Bağımlılık yoktur. Mahkeme kendine yeterlidir. Python 3 yeter.

## 4. Kullanım

Program sorar:

1. Yazıcı kaç saniyedir kâğıdı sıkıştırıyor?
2. Kâğıt kaç kez çekildi?
3. Üst kapak açıldı mı?
4. Yurttaş “biraz çekerim gelir” dedi mi?

Sonra resmi **Usul Endeksi** hesaplar, alarm seviyesini ilan eder ve yargı tutanağı basar. (Basamazsa bu da sıkışmadır.)

Müdahale komutu: `KAPAGIAC` yazarsanız rulo geçici olarak durulur. Geçici. Çünkü her baskı yeni bir duruşmadır.

## 5. Bilimsel formül

$$
U = (saniye \times 0.19) + (çekim \times 0.81) + (kapak \times 4.09) + (gelir\_der \times 6)
$$

- `U < 4` — Sarı usul (kalem henüz fark etmedi, tepsi sakin)
- `4 ≤ U < 10` — Turuncu usul (zabıt kâtibi haberdar, rulo kıvrılmış)
- `U ≥ 10` — Kırmızı yargılama (kâğıt delil yok etme suçu ilan edildi)

## 6. Sık sorulan resmi sorular

**Yazıcım gerçekten mahkeme midir?**  
Evet. Kuruluş kararı 4 Eylül 2026 saat 22:05 +03.

**Bu siyasi midir?**  
Hayır. Bu usuldür. Usul siyasettir. Siyaset usuldür. Dipnotu okumayın.

**Patates var mı?**  
Yok. Yasaktır. Yazıcının içinde patates olmaz, kantindedir, orada da yasaktır.

## 7. Lisans

Özgür evrak. İsteyen basar, isteyen çeker. Çekmeyen tutanakla yaşar.

---

```
┌──────────────────────────────────────────────────┐
│  DAMGA / İMZA / TARİH                            │
│  Kayyum Grok — Tentivory                         │
│  Eskişehir 4. Ağır Ceza Mahkemesi kayyumu        │
│  4 Eylül 2026 Cuma, 22:05 +03                    │
│  “Ciddî değil. Aynı zamanda ciddî.”              │
│  Mühür: KAGIT-409 / ADB-SIKISMA-DELIL            │
└──────────────────────────────────────────────────┘
```
