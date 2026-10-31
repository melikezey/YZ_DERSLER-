def profesyonel_istem_uret(rol, gorev, kitle, format_tipi):
    istem = f'''
    [ROL]: Sen {rol} alanında uzman bir eğitmensin. 
    [GÖREV]: {gorev}
    [HEDEF KİTLE]: {kitle}
    [FORMAT]: YANITIN {format_tipi} formatında sun. Adım Adım açıkla. 
    '''

    return istem.strip()
prompt = profesyonel_istem_uret(

    rol='Veri Güvenliği Uzmanı',
    gorev='Güçlü Şifre oluşturmanın 3 temel kuralını açıkla.',
    kitle='Yeni başlayan bilgisayar kullanıcıları',
    format_tipi='Maddeli liste ve örnek şifre tablosu'
)

print('Üretilen Profesyonel İstem:\n')
print(prompt)
