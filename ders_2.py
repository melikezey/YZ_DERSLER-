mesafe = 77
hiz = 55

if mesafe < 30 and hiz > 15:
    print("📏 Mesafe:", mesafe, "cm")
    print("💨 Hız:", hiz, "km/h")
    print("⚠️ Aksiyon: Araç çok yakın ve hızlı! Bariyer açık tutuluyor.")

elif mesafe < 50 and hiz <= 15:
    print("📏 Mesafe:", mesafe, "cm")
    print("💨 Hız:", hiz, "km/h")
    print("🚗 Aksiyon: Araç yaklaşıyor. 🚧 Bariyer açılıyor.")

else:
    print("📏 Mesafe:", mesafe, "cm")
    print("💨 Hız:", hiz, "km/h")
    print("🔒 Aksiyon: Araç yeterince uzakta. Bariyer kapalı.")
