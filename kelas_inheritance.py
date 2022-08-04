# mencoba membuat kelas dengan Py.

class orang ():
    tempat = "bumi"
    tatsurya = "matahari"
    def __init__(self, nama, alamat):
        self.nama = nama
        self.alamat = alamat
        print ("Hello Kelas!!!")
    def jalan(self):
        print (f"kita mulai ya mas {self.nama} yang rumahnya di {self.alamat}!!!! ")

# kunyuk = orang("marjo","kalianget")
# kunyuk2 = orang("gunawan","kertek")
# kunyuk2.jalan()
# kunyuk.jalan()

def wanita(param, param1):
    pass


class wanita (orang):
    kelakuan = "bejat"
    def bintang(self):
        print (f"lu tinggal di {super().tempat} dalam tatasurya {super().tatsurya}")
        print (f"atau bisa pake konsep gini {self.nama} yang tinggal di {self.alamat} yang kelakuannya {self.kelakuan}")

coba = wanita("nonong","surinong")
coba.bintang()
coba.jalan()

