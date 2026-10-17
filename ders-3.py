import time

yasakli_kelimeler = ["kazandiniz", "bedava", "hemen tıkla", "kredi"]

while True:
    gelen_mesaj = input("Mesajınızı giriniz: ")

    is_spam = False

    for kelime in yasakli_kelimeler:
        if kelime in gelen_mesaj.lower():
            is_spam = True
            break

    print("Mesaj kontrol ediliyor...")
    time.sleep(1)

    if is_spam:
        print("Sonuç: Bu mesaj SPAM olarak engellendi.")
    else:
        print("Sonuç: Bu mesaj GÜVENLİ.")

    print()
