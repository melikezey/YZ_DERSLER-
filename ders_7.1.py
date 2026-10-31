def istem_kalite_puani(prompt):
    skor = 0
    kriterler = {
        'Rol Tanımı': ['sen bir', 'uzman', 'rolün'],
        'Format Belirtimi': ['tablo', 'liste', 'madde', 'kod'],
        'Kısıtlama': ['en fazla', 'adım adım', 'haricinde', 'sadece'],
        'Yeterli Uzunluk': [len(prompt) > 40]
    }
    for kriter, anahtarlar in kriterler.items():
        if any(k in prompt.lower() if isinstance(k,str)else k for k in anahtarlar):
            skor += 25

    return skor

kotu = 'bana kod yaz'
iyi = 'Sen bir Python uzmanısın. Sıralama algoritmasını adım adım liste olarak yaz.'

print(f'Kötü istem Kalite skoru: {istem_kalite_puani(kotu)} / 100')
print(f'İyi istem Kalite Skoru: {istem_kalite_puani(iyi)} / 100')
