try:
    
    #memasukkan lokasi menyimpan file yang akan dienkripsi beserta nama filenya
    path = input(r'Masukkan Lokasi penyimpanan Image : ')
     
    #memasukkan kunci yang digunakan untuk enkripsi
    print('Note : Key untuk dekripsi harus sama dengan key enkripsi')
    key = int(input('Masukkan key yang sama dengan enkripsi : '))
        
    print('Lokasi penyimpanan file : ', path)
    print('Masukkan Key Deskripsi : ', key)
     
    fin = open(path, 'rb')
     
    #membaca file 
    image = fin.read()
    fin.close()
        
    #mengubah bentuk file image
    image = bytearray(image)
 
    #proses dekripsi image   
    for index, values in enumerate(image):
        image[index] = values ^ key
     
    fin = open(path, 'wb')
     
    #jika image berhasil didekripsi:    
    fin.write(image)
    fin.close()
    print('Dekripsi Sukses!')
 
#menampilkan error jika code/file tidak dapat terbaca 
except Exception:
    print('Error caught : ', Exception.__name__)