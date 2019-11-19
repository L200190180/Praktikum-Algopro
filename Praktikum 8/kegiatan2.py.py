data = {'nama':'fakhri', 'nim':'L200190180', 'umur':'18', 'hobi':'ngegame', 'asal':'purwodadi', 'sekolah':'ums', 'golongan_darah':'A'}
def nama():
    print('nama:',data['nama'])
def nim():
    print('nim:',data ['nim'])
def umur():
    print('umur:',data['umur'])
def hobi():
    print('hobi:',data ['hobi'])
def asal():
    print('asal:',data['asal'])
def sekolah():
    print('sekolah',data ['sekolah'])
def golongan_darah():
    print('golongan darah:',data['golongan_darah'])

b = """Pilihan yang tersedia :
b menampilkan bantuan ini
1 menampilkan nama
2 menampilkan nim
3 menampilkan umur
4 menampilkan hobi
5 menampilkan asal
6 menampilkan sekolah
7 menampilkan golongan darah
k keluar
"""
print(b)

k = "Terima kasih"
x = input('pilihan yang tersedia: ')
while x != 'k':
    if x == 'b':
        print(b)
        print(" ")
        x = input('pilihan yang tersedia: ')
    elif x == '1':
        nama()
        print(" ")
        x = input('pilihan yang tersedia: ')
    elif x == '2':
        nim()
        print(" ")
        x = input('pilihan yang tersedia: ')
    elif x == '3':
        umur()
        print(" ")
        x = input('pilihan yang tersedia: ')
    elif x == '4':
        hobi()
        print(" ")
        x = input('pilihan yang tersedia: ')
    elif x == '5':
        asal()
        print(" ")
        x = input('pilihan yang tersedia: ')
    elif x == '6':
        sekolah()
        print(" ")
        x = input('pilihan yang tersedia: ')
    elif x == '7':
        golongan_darah()
        print(" ")
        x = input('pilihan yang tersedia: ')
print(k)




    


