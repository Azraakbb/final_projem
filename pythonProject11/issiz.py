from insanlar import Insan

class Issiz(Insan):
    def __init__(self, tc_no, ad, soyad, yas, cinsiyet, uyruk, tecrube_dict):
        super().__init__(tc_no, ad, soyad, yas, cinsiyet, uyruk)
        self.__tecrube_dict = tecrube_dict

    def get_tecrube_dict(self):
        return self.__tecrube_dict

    def set_tecrube_dict(self, tecrube_dict):
        self.__tecrube_dict = tecrube_dict

    def statu_bul(self):
        mavi_yaka = self.__tecrube_dict.get("mavi yaka", 0)
        beyaz_yaka = self.__tecrube_dict.get("beyaz yaka", 0)
        yonetici = self.__tecrube_dict.get("yonetici", 0)

        mavi_yaka_etkisi = mavi_yaka * 0.20
        beyaz_yaka_etkisi = beyaz_yaka * 0.35
        yonetici_etkisi = yonetici * 0.45

        max_etki = max(mavi_yaka_etkisi, beyaz_yaka_etkisi, yonetici_etkisi)

        if max_etki == mavi_yaka_etkisi:
            return "mavi yaka"
        elif max_etki == beyaz_yaka_etkisi:
            return "beyaz yaka"
        else:
            return "yonetici"

    def __str__(self):
        return f"{super().__str__()}\nStatü: {self.statu_bul()}"