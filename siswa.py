from person import Person

class Siswa(Person):
    def __init__(self, nama, alamat, nim):
        super().__init__(nama, alamat)
        self.nim = nim
        
    def tampil(self):
        print("Nama:", self.nama,"alamat:" ,self.alamat,"NIM:", self.nim)
        