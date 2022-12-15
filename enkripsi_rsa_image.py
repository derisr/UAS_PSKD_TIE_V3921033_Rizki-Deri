try:

    #memasukkan lokasi menyimpan file yang akan dienkripsi beserta nama filenya
    path = input(r'Masukkan Lokasi penyimpanan Image : ')
    
    #memasukkan kunci enkripsi berupa angka
    key = int(input('Masukkan key enkripsi (integer) : '))
    
    print('Lokasi penyimpanan file : ', path)
    print('Masukkan Key Enskripsi : ', key) 
    
    fin = open(path, 'rb')
    #membaca file 
    image = fin.read()
    fin.close()
     
    #mengubah bentuk file image
    image = bytearray(image)

    #proses enkripsi image   
    for index, values in enumerate(image):
        image[index] = values ^ key
 
    fin = open(path, 'wb')

    #jika image berhasil dienkripsi:    
    fin.write(image)
    fin.close()
    print('Enskripsi Sukses!')
  
#menampilkan error jika code/file tidak dapat terbaca
except Exception:
    print('Error caught : ', Exception.__name__)