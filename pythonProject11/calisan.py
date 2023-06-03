from insanlar import Insan

class Calisan(Insan):
    def __init__(self, tc_no, ad, soyad, yas, cinsiyet, uyruk, sektor, tecrube, maas):
        super().__init__(tc_no, ad, soyad, yas, cinsiyet, uyruk)
        self.__sektor = sektor
        self.__tecrube = tecrube
        self.__maas = maas

    def get_sektor(self):
        return self.__sektor

    def set_sektor(self, sektor):
        self.__sektor = sektor

    def get_tecrube(self):
        return self.__tecrube

    def set_tecrube(self, tecrube):
        self.__tecrube = tecrube

    def get_maas(self):
        return self.__maas

    def set_maas(self, maas):
        self.__maas = maas

    def kontrol_sektor(self, sektor):
        sektorler = ["teknoloji", "muhasebe", "inşaat", "diğer"]
        if sektor in sektorler:
            return sektor
        else:
            return "diğer"

    def zam_hakki(self):
        try:
            if self.__tecrube <= 24:
                return 0
            elif 24 < self.__tecrube <= 48 and self.__maas < 15000:
                return self.__maas % self.__tecrube
            elif self.__tecrube > 48 and self.__maas < 25000:
                return (self.__maas % self.__tecrube) / 2
            else:
                return 0
        except:
            print("hata! tecrübe değerini kontrol et")

    def __str__(self):
        yeni_maas = float(self.__maas) + self.zam_hakki()
        if yeni_maas == self.__maas:
            yeni_maas = self.__maas
        return f"Ad: {self.get_ad()}\nSoyad: {self.get_soyad()}\nTecrübe: {self.__tecrube}\nYeni Maaş: {yeni_maas}"
