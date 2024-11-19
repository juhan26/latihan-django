class Person(object):
    def __init__(self, nama, alamat):
        self.nama = nama
        self.alamat = alamat
        
    def tampil(self):
            print("Nama saya", self.nama,"dan saya Berasal dari", self.alamat)