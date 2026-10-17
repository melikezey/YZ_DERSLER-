ham_nem_verileri = [45, 48, None, 50, 52, None, 47]

temiz_nem_verileri = []

for nem in ham_nem_verileri:
    if nem is not None:
        temiz_nem_verileri.append(nem)

print("Ham Sensör Verisi:", ham_nem_verileri)
print("Eksik Veriler Ayıklandıktan Sonra:", temiz_nem_verileri)

ortalama_nem = sum(temiz_nem_verileri) / len(temiz_nem_verileri)
print("Temiz Verilerin Nem Ortalaması:", round(ortalama_nem, 1))
