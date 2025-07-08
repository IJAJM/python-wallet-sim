class Koin:
    def __init__(self, nama, jumlah):
        self.nama = nama
        self.jumlah = jumlah

class Dompet:
    def __init__(self, nama):
        self.nama = nama
        self.koin = {}

    def tambah_koin(self, koin, jumlah):
        if koin.nama in self.koin:
            self.koin[koin.nama] += jumlah
        else:
            self.koin[koin.nama] = jumlah

    def kurangi_koin(self, koin, jumlah):
        if koin.nama in self.koin:
            if self.koin[koin.nama] >= jumlah:
                self.koin[koin.nama] -= jumlah
            else:
                print("Saldo tidak cukup")
        else:
            print("Koin tidak ada di dompet")

    def cek_saldo(self):
        print(f"Saldo dompet {self.nama}:")
        for koin, jumlah in self.koin.items():
            print(f"{koin}: {jumlah}")

# Membuat koin
koin1 = Koin("KoinA", 100)

# Membuat dompet
dompet1 = Dompet("Dompet1")
dompet2 = Dompet("Dompet2")

# Menambah koin ke dompet1
dompet1.tambah_koin(koin1, 50)

# Mentransfer koin dari dompet1 ke dompet2
dompet1.kurangi_koin(koin1, 20)
dompet2.tambah_koin(koin1, 20)

# Cek saldo
dompet1.cek_saldo()
dompet2.cek_saldo()
