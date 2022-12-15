# import library
from cryptography.fernet import Fernet


# key generation
key = Fernet.generate_key()
 
# membaca string kunci
with open('UAS_SKD/filekey.key', 'wb') as filekey:
   filekey.write(key)   


# menggunakan kunci
fernet = Fernet(key)
 
# membaca file csv
with open('UAS_SKD/file_csv.csv', 'rb') as file:
    original = file.read()
     
# enkripsi csv
encrypted = fernet.encrypt(original)
 
# simpan file enkripsi
with open('UAS_SKD/file_tes_encrypted.csv', 'wb') as encrypted_file:
    encrypted_file.write(encrypted)


#DEKRIPSI
    
# menggunakan kunci sebelumnya
fernet = Fernet(key)

# membuka file hasil enkrpisi
with open('UAS_SKD/file_tes_encrypted.csv', 'rb') as enc_file:
	encrypted = enc_file.read()

# proses dekripsi 
decrypted = fernet.decrypt(encrypted)

# cek kesamaan hasil dekripsi
with open('UAS_SKD/file_tes_decrypted.csv', 'wb') as dec_file:
	dec_file.write(decrypted)
