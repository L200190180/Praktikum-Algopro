berkas = open('L200190180.txt', 'w')
berkas.write('L200190180\n')
berkas.write('17-07-2001\n')
berkas.write('Fakhri Setyo Utomo\n')
berkas.write('Purwodadi')
berkas.close()


berkas = open('L200190180.txt', 'r')
NIM = berkas.readline()
TTL = berkas.readline()
Nama = berkas.readline()
Kota = berkas.readline()

print (Nama)
print (Kota,TTL)
print (NIM)
