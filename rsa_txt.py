#import library
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import binascii

#import file yang akan dienkripsi
file_enc = open("UAS_SKD/file_txt.txt", "r")

print('=====================================================')
print('==== Enkripsi & Dekripsi File with RSA Algorithm ====')
print('=====================================================')

#membaca file yang akan dienkripsi
read = file_enc.readlines()
print (read[0])
teks = str(read[0]) 

#mengubah text menjadi binnary
teks_binary = teks.encode()
print(teks_binary)

#generate key
keyPair = RSA.generate(3072)

#membuat public key
pubKey = keyPair.publickey()
pubKeyPEM = pubKey.exportKey()
key2 = pubKeyPEM.decode('ascii')

privKeyPEM = keyPair.exportKey()

#proses enkripsi dan menampilkan hasil enkripsi
encryptor = PKCS1_OAEP.new(pubKey)
encrypted = encryptor.encrypt(teks_binary)
print("Encrypted:", binascii.hexlify(encrypted))
cipher_ascii = binascii.hexlify(encrypted)
cipherteks = cipher_ascii.decode()

#proses dekripsi dan menampilkan hasil enkripsi
decryptor = PKCS1_OAEP.new(keyPair)
decrypted = decryptor.decrypt(encrypted)
plainteks = decrypted.decode()
print('Decrypted:', plainteks)

#membuat file key
file_dec = open("pkey.txt", "a")
file_dec.write(key2)