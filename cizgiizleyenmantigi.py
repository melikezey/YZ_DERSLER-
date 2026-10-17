while True:
    sol_sensor = int(input("Sol sensör (0 veya 1): "))
    sag_sensor = int(input("Sağ sensör (0 veya 1): "))

    if sol_sensor == 1 and sag_sensor == 0:
        hareket = "Sola Dön"
    elif sol_sensor == 0 and sag_sensor == 1:
        hareket = "Sağa Dön"
    elif sol_sensor == 1 and sag_sensor == 1:
        hareket = "Düz Git"
    else:
        hareket = "Dur ve çizgi ara"

    print("Robotun Aksiyonu:", hareket)
    print()
