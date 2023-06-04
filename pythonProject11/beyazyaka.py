from calisan import Calisan

class BeyazYaka(Calisan):
    def __init__(self, tc_no, ad, soyad, yas, cinsiyet, uyruk, sektor, tecrube, maas, tesvik_primi):
        super().__init__(tc_no, ad, soyad, yas, cinsiyet, uyruk, sektor, tecrube, maas)
        self.__tesvik_primi = tesvik_primi

    def get_tesvik_primi(self):
        return self.__tesvik_primi

    def set_tesvik_primi(self, tesvik_primi):
        self.__tesvik_primi = tesvik_primi


    def zam_hakki(self):
        try:
            if self.get_tecrube() <= 2:
                return self.get_tesvik_primi()
            elif 2 < self.get_tecrube() <= 4 and self.get_maas() < 15000:
                return (self.get_maas() % self.get_tecrube()) * 5 + self.get_tesvik_primi()
            elif self.get_tecrube() > 4 and self.get_maas() < 25000:
                return (self.get_maas() % self.get_tecrube()) * 4 + self.get_tesvik_primi()
            else:
                return 0
        except Exception as e:
            print(f"Hata: {str(e)}")
            return None

    def __str__(self):
        yeni_maas = self.zam_hakki() + self.get_maas()
        if yeni_maas == self.get_maas():
            yeni_maas = self.get_maas()
        return f"{super().__str__()}\nTeşvik Prim: {self.__tesvik_primi}\nYeni Maaş: {yeni_maas}"
