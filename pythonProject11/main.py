import pandas as pd
from insanlar import Insan
from issiz import Issiz
from calisan import Calisan
from maviyaka import MaviYaka
from beyazyaka import BeyazYaka

# Insan sınıfı için 2 nesne oluşturma
try:
    insan1 = Insan("1235557840", "Aylin", "Yıldırım", 33, "kadın", "Türk")
    insan2 = Insan("9876563010", "Berkay", "Çevik", 24, "erkek", "Türk")
    print("İnsan sınıfı kişileri\n")
    print(insan1)
    print()
    print(insan2)
    print("----------")

# Issiz sınıfı için 3 nesne oluşturma
    tecrube_dict = {"mavi yaka": 5, "beyaz yaka": 3, "yonetici": 2}
    issiz1 = Issiz("0977654421", "John", "Carol", 29, "erkek", "İngiliz", tecrube_dict)
    tecrube_dict2 = {"mavi yaka": 8, "beyaz yaka": 2,"yonetici": 3}
    issiz2 = Issiz("1122334455", "Mehmet", "Kaya", 30, "erkek", "Türk", tecrube_dict2)
    tecrube_dict3 = {"mavi yaka": 0, "beyaz yaka":0,"yonetici": 4}
    issiz3 = Issiz("9888593210", "Fatma", "Pak", 26, "kadın", "Türk", tecrube_dict3)
    print("İşsiz sınıfı kişileri\n")
    print(issiz1)
    print()
    print(issiz2)
    print()
    print(issiz3)
    print("---------")

# Calisan sınıfı için 3 nesne oluşturma
    calisan1 = Calisan("1737547890", "Su", "Ural", 30, "kadın", "Türk", "Muhasebe", 36,998)
    zam1 = calisan1.get_maas()*calisan1.zam_hakki()/100
    calisan2 = Calisan("1876343290", "Tuba", "Akdeniz", 25, "kadın", "Türk", "Teknoloji", 12, 3400)
    zam2 = calisan2.get_maas()*calisan2.zam_hakki()/100
    calisan3 = Calisan("5278906274", "Melek", "Şahin", 29, "kadın", "Türk", "Diğer", 24, 2223)
    zam3 = calisan3.get_maas()*calisan3.zam_hakki()/100
    print("Çalışan sınıfı kişileri\n")
    print(calisan1)
    print()
    print(calisan2)
    print()
    print(calisan3)
    print("---------")

# MaviYaka sınıfı için 3 nesne oluşturma
    mavi_yaka1 = MaviYaka("1441567890", "Yusuf", "Aktaş", 34, "erkek", "Türk", "Teknoloji", 4,14052,0.5)
    zam4 = mavi_yaka1.get_maas()*mavi_yaka1.zam_hakki()/100
    mavi_yaka2 = MaviYaka("3176543210", "Sıla", "Gökdeniz", 25, "kadın", "Türk", "Muhasebe",2,10221,0.2)
    zam5 = mavi_yaka2.get_maas()*mavi_yaka2.zam_hakki()/100
    mavi_yaka3 = MaviYaka("5673901634", "Baran", "Erdoğdu", 37, "erkek", "Türk", "Diğer", 8,30000,0.4)
    zam6 = mavi_yaka3.get_maas()*mavi_yaka3.zam_hakki()/100
    print("Mavi yaka sınıfı kişileri\n")
    print(mavi_yaka1)
    print()
    print(mavi_yaka2)
    print()
    print(mavi_yaka3)
    print("---------")


    # BeyazYaka sınıfı için 3 nesne oluşturma
    beyaz_yaka1 = BeyazYaka("1234567890", "Alican", "Akbaba", 28, "erkek", "Türk", "İnşaat",2,14910,1900)
    zam7 = beyaz_yaka1.zam_hakki()
    beyaz_yaka2 = BeyazYaka("9876543210", "Berk", "Kara", 45, "erkek", "Türk", "Teknoloji",4,14073,1450)
    zam8 = beyaz_yaka2.zam_hakki()
    beyaz_yaka3 = BeyazYaka("5678901234", "Sudenur", "Şemik", 40, "kadın", "Türk", "Diğer",6,20050,2000 )
    zam9 = beyaz_yaka3.zam_hakki()
    print("Beyaz yaka sınıfı kişileri\n")
    print(beyaz_yaka1)
    print()
    print(beyaz_yaka2)
    print()
    print(beyaz_yaka3)
    print()

    data = {
        'nesne_degeri': ['Çalışan', 'Çalışan', 'Çalışan', 'Mavi Yaka', 'Mavi Yaka', 'Mavi Yaka', 'Beyaz Yaka', 'Beyaz Yaka','Beyaz Yaka'],
        'tc_no': [calisan1.get_tc_no(), calisan2.get_tc_no(), calisan3.get_tc_no(), mavi_yaka1.get_tc_no(), mavi_yaka2.get_tc_no(), mavi_yaka3.get_tc_no(), beyaz_yaka1.get_tc_no(), beyaz_yaka2.get_tc_no(), beyaz_yaka3.get_tc_no()],
        'ad': [calisan1.get_ad(), calisan2.get_ad(), calisan3.get_ad(), mavi_yaka1.get_ad(), mavi_yaka2.get_ad(), mavi_yaka3.get_ad(), beyaz_yaka1.get_ad(),beyaz_yaka2.get_ad(), beyaz_yaka3.get_ad()],
        'soyad': [calisan1.get_soyad(), calisan2.get_soyad(), calisan3.get_soyad(), mavi_yaka1.get_soyad(), mavi_yaka2.get_soyad(), mavi_yaka3.get_soyad(),beyaz_yaka1.get_soyad(), beyaz_yaka2.get_soyad(), beyaz_yaka3.get_soyad()],
        'yas': [calisan1.get_yas(), calisan2.get_yas(), calisan3.get_yas(), mavi_yaka1.get_yas(), mavi_yaka2.get_yas(), mavi_yaka3.get_yas(), beyaz_yaka1.get_yas(),beyaz_yaka2.get_yas(), beyaz_yaka3.get_yas()],
        'cinsiyet': [calisan1.get_cinsiyet(), calisan2.get_cinsiyet(), calisan3.get_cinsiyet(), mavi_yaka1.get_cinsiyet(), mavi_yaka2.get_cinsiyet(), mavi_yaka3.get_cinsiyet(), beyaz_yaka1.get_cinsiyet(), beyaz_yaka2.get_cinsiyet(), beyaz_yaka3.get_cinsiyet()],
        'uyruk': [calisan1.get_uyruk(), calisan2.get_uyruk(), calisan3.get_uyruk(), mavi_yaka1.get_uyruk(), mavi_yaka2.get_uyruk(), mavi_yaka3.get_uyruk(),beyaz_yaka1.get_uyruk(), beyaz_yaka2.get_uyruk(), beyaz_yaka3.get_uyruk()],
        'sektor': [calisan1.get_sektor(), calisan2.get_sektor(), calisan3.get_sektor(), mavi_yaka1.get_sektor(), mavi_yaka2.get_sektor(), mavi_yaka3.get_sektor(), beyaz_yaka1.get_sektor(), beyaz_yaka2.get_sektor(), beyaz_yaka3.get_sektor()],
        'tecrube': [calisan1.get_tecrube()/12, calisan2.get_tecrube()/12, calisan3.get_tecrube()/12, mavi_yaka1.get_tecrube(), mavi_yaka2.get_tecrube(),mavi_yaka3.get_tecrube(), beyaz_yaka1.get_tecrube(), beyaz_yaka2.get_tecrube(), beyaz_yaka3.get_tecrube()],
        'maas': [calisan1.get_maas(), calisan2.get_maas(), calisan3.get_maas(), mavi_yaka1.get_maas(),mavi_yaka2.get_maas(), mavi_yaka3.get_maas(),beyaz_yaka1.get_maas(), beyaz_yaka2.get_maas(), beyaz_yaka3.get_maas()],
        'yipranma_payi': [0, 0, 0, mavi_yaka1.get_yipranma_payi(),mavi_yaka2.get_yipranma_payi(), mavi_yaka3.get_yipranma_payi(), 0, 0, 0],
        'tesvik_primi': [0, 0, 0, 0, 0, 0, beyaz_yaka1.get_tesvik_primi(), beyaz_yaka2.get_tesvik_primi(), beyaz_yaka3.get_tesvik_primi()],
        'yeni_maaslar': [calisan1.get_maas()+zam1, calisan2.get_maas()+zam2, calisan3.get_maas()+zam3, mavi_yaka1.get_maas()+zam4, mavi_yaka2.get_maas()+zam5,mavi_yaka3.get_maas()+zam6,beyaz_yaka1.get_maas()+zam7,beyaz_yaka2.get_maas()+zam8,beyaz_yaka3.get_maas()+zam9]
    }

    df = pd.DataFrame(data)     #dataframe oluşturma

    df.fillna(0)
    print(df)

    gruplar = df.groupby('nesne_degeri')
    sonuclar = gruplar.agg({'tecrube': 'mean', 'yeni_maaslar': 'mean'})
    print(sonuclar)
    print()

    maasi_fazlalar = df[df['maas'] > 15000]  #maaşı fazla olanları bulma
    toplam_sayi = len(maasi_fazlalar)
    print("Maaşı 15000 TL üzerinde olanların toplam sayısı:", toplam_sayi)
    print()

    siralamam = df.sort_values('yeni_maaslar')
    print(siralamam)
    print()

    by_tecrubelers = df[(df['nesne_degeri'] == 'Beyaz Yaka') & (df['tecrube'] > 3)]
    secilen_by = by_tecrubelers.loc[:,['ad', 'soyad', 'tecrube', 'yeni_maaslar']]  #belirli sütunları alma
    print(secilen_by)
    print()

    ymaasi_fazla = df[df['yeni_maaslar'] > 10000]
    secilen_sutunlar = ymaasi_fazla.loc[2:5, ['ad', 'soyad', 'tc_no', 'yeni_maaslar']]  #belirli satırları alma
    print(secilen_sutunlar)
    print()

    yeni_df = df[['ad', 'soyad', 'sektor', 'yeni_maaslar']]
    print(yeni_df)

except Exception as e:
    print(f"Hata: {str(e)}")
