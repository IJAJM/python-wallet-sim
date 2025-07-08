# 🪙 PyDompet — Simulasi Dompet dan Koin Sederhana

Simulasi sederhana menggunakan Python untuk menyimpan, menambah, dan mentransfer koin antar dompet virtual.

## 🚀 Fitur

- Membuat objek `Koin` dan `Dompet`
- Menambah koin ke dompet
- Mengurangi (mentransfer) koin dari satu dompet ke dompet lain
- Mengecek saldo semua jenis koin di dompet

## 🧠 Contoh Penggunaan

```python
# Membuat koin
koin1 = Koin("KoinA", 100)

# Membuat dompet
dompet1 = Dompet("Dompet1")
dompet2 = Dompet("Dompet2")

# Menambah koin ke dompet1
dompet1.tambah_koin(koin1, 50)

# Transfer ke dompet2
dompet1.kurangi_koin(koin1, 20)
dompet2.tambah_koin(koin1, 20)

# Cek saldo
dompet1.cek_saldo()
dompet2.cek_saldo()
