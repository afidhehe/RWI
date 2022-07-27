# mencoba membuat kelas dengan Py.

class orang ():
    def __init__(self, nama, alamat):
        self.nama = nama
        self.alamat = alamat
        print ("Hello Kelas!!!")
    def jalan(self):
        print (f"kita mulai ya mas {self.nama} yang rumahnya di {self.alamat}!!!! ")

kunyuk = orang("marjo","kalianget")
kunyuk2 = orang("gunawan","kertek")
kunyuk2.jalan()
kunyuk.jalan()
