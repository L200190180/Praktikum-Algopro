import shelve
berkas = open('L200190180.txt', 'r')
NIM = berkas.readline()
TTL = berkas.readline()
Nama = berkas.readline()
Kota = berkas.readline()
TTL = Kota + TTL

F = shelve.open('kegiatan1.data')
F['Data'] = [NIM, TTL, Nama, Kota]
F.close()
