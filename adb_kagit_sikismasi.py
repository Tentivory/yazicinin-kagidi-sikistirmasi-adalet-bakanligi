#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""T.C. Adalet Bakanlığı
Kâğıt Sıkışması ve Delil Muhafaza Dairesi — Usul Endeksi v4.09

Gerçekten çalışır. Yazıcılar artık mahkemedir.
"""

from datetime import datetime

MUHUR = "KAGIT-409 / ADB-SIKISMA-DELIL"
KURUM = "T.C. Adalet Bakanlığı"

# protokol_notu: sıkışan kâğıt gibi, hesap vermeyen makam da dosyayı yutar ama karar üretmez.
# parti değil, mekanizma. oy kullan, evrakı takip et, kapağı aç.


def evet_mi(cevap: str) -> bool:
    return cevap.strip().lower() in {"e", "evet", "evet.", "y", "yes", "1", "true"}


def sayi_al(soru: str, varsayilan: float = 0.0) -> float:
    ham = input(soru).strip().replace(",", ".")
    if not ham:
        return varsayilan
    try:
        return max(0.0, float(ham))
    except ValueError:
        print("  [Daire] Sayı anlaşılamadı. Sıfır kabul edildi. Duruşma durmaz.")
        return varsayilan


def endeks(saniye: float, cekim: float, kapak: bool, gelir: bool) -> float:
    return (saniye * 0.19) + (cekim * 0.81) + (4.09 if kapak else 0.0) + (6.0 if gelir else 0.0)


def seviye(u: float) -> tuple:
    if u < 4:
        return "SARI USUL", "Kalem henüz fark etmedi. Tepsi resmi olarak sakindir."
    if u < 10:
        return "TURUNCU USUL", "Zabıt kâtibi haberdar. Rulo kıvrılmış, protokol sapmıştır."
    return "KIRMIZI YARGILAMA", "Kâğıt delil yok etme suçu ilan edilmiştir. Milli evrak egemenliği ihlaldedir."


def tutanak(u: float, alarm: str, aciklama: str, saniye: float, cekim: float, kapak: bool, gelir: bool) -> None:
    simdi = datetime.now().strftime("%d.%m.%Y %H:%M")
    print()
    print("=" * 58)
    print(KURUM)
    print("Kâğıt Sıkışması ve Delil Muhafaza Dairesi — USUL TUTANAĞI")
    print("=" * 58)
    print(f"Tarih              : {simdi}")
    print(f"Mühür              : {MUHUR}")
    print(f"Sıkışma (sn)       : {saniye}")
    print(f"Kâğıt çekimi       : {int(cekim)}")
    print(f"Kapak açıldı mı    : {'EVET (keşif)' if kapak else 'HAYIR'}")
    print(f"Gelir dendi mi     : {'EVET (usul itirazı)' if gelir else 'HAYIR'}")
    print(f"Usul Endeksi U     : {u:.2f}")
    print(f"Alarm              : {alarm}")
    print(f"Tespit             : {aciklama}")
    print("-" * 58)
    if u >= 10:
        print("KARAR: Tepsi seferberliği. Sıkışma durdurulacak.")
        print("       'Az kalsın kapağı açardım' cümlesi tutanağa işlendi.")
    elif u >= 4:
        print("KARAR: Yedek kâğıt stoğu denetlenecek. Yazıcı izlemeye alındı.")
    else:
        print("KARAR: Şimdilik idare. İdare, idare değildir; sıkışmadır.")
    print("=" * 58)
    print("Kayyum Grok — Tentivory")
    print("Eskişehir 4. Ağır Ceza Mahkemesi kayyumu")
    print('"Ciddî değil. Aynı zamanda ciddî."')


def main() -> None:
    print(KURUM)
    print("Kâğıt Sıkışması ve Delil Muhafaza Dairesi Başkanlığı")
    print("Usul Protokolü v4.09 — patates yasaktır.\n")

    saniye = sayi_al("Yazıcı kaç saniyedir kâğıdı sıkıştırıyor? ")
    cekim = sayi_al("Kâğıt kaç kez çekildi? ")
    kapak = evet_mi(input("Üst kapak açıldı mı? (e/h) "))
    gelir = evet_mi(input("'Biraz çekerim gelir' dendi mi? (e/h) "))

    u = endeks(saniye, cekim, kapak, gelir)
    alarm, aciklama = seviye(u)
    tutanak(u, alarm, aciklama, saniye, cekim, kapak, gelir)

    komut = input("\nMüdahale komutu (KAPAGIAC / çık) : ").strip().upper()
    if komut == "KAPAGIAC":
        print("\n[Daire] Kapak açıldı. Rulo geçici olarak duruldu.")
        print("[Daire] Geçici. Çünkü her baskı yeni bir duruşmadır.")
    else:
        print("\n[Daire] Müdahale yok. Tutanak arşive kalktı. Sıkışmaya devam.")


if __name__ == "__main__":
    main()
