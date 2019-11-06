## Program Akun
## Dibuat oleh Fakhri L200190180
import random
angka = random.randint(0,1000)

Nama = 'Fakhri Setyo Utomo'
TanggalLahir = '17 Juli 2001'
NamaSingkat = Nama[0] + '.' + Nama[7] + '.' + Nama[13:18]
Username = Nama[0] + TanggalLahir[0:2] + TanggalLahir[8:14]
Password = Nama[0:3] + str(angka)
