import shelve

berkas = open('L200190180.txt', 'r')
F = shelve.open('kegiatan1.data')
print (F['Data'][2])
print (F['Data'][0])
print (F['Data'][1])
