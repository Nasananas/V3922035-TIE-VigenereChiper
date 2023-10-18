def vigenere_encrypt(plain_text, key):
    encrypted_text = ""
    key_length = len(key)
    
    for i in range(len(plain_text)):
        char = plain_text[i]
        if char.isalpha():
            # Mendapatkan indeks huruf dalam alfabet (0-25)
            char_idx = ord(char.lower()) - ord('a')
            
            # Mendapatkan indeks huruf dalam kunci
            key_char = key[i % key_length]
            key_idx = ord(key_char.lower()) - ord('a')
            
            # Mengenkripsi karakter
            encrypted_idx = (char_idx + key_idx) % 26
            encrypted_char = chr(encrypted_idx + ord('a'))
            
            # Mempertahankan huruf kapital jika huruf aslinya kapital
            if char.isupper():
                encrypted_char = encrypted_char.upper()
            
            encrypted_text += encrypted_char
        else:
            # Menambahkan karakter non-huruf langsung ke teks terenkripsi
            encrypted_text += char
    
    return encrypted_text

def vigenere_decrypt(encrypted_text, key):
    decrypted_text = ""
    key_length = len(key)
    
    for i in range(len(encrypted_text)):
        char = encrypted_text[i]
        if char.isalpha():
            # Mendapatkan indeks huruf dalam alfabet (0-25)
            char_idx = ord(char.lower()) - ord('a')
            
            # Mendapatkan indeks huruf dalam kunci
            key_char = key[i % key_length]
            key_idx = ord(key_char.lower()) - ord('a')
            
            # Mendekripsi karakter
            decrypted_idx = (char_idx - key_idx) % 26
            decrypted_char = chr(decrypted_idx + ord('a'))
            
            # Mempertahankan huruf kapital jika huruf aslinya kapital
            if char.isupper():
                decrypted_char = decrypted_char.upper()
            
            decrypted_text += decrypted_char
        else:
            # Menambahkan karakter non-huruf langsung ke teks terdekripsi
            decrypted_text += char
    
    return decrypted_text

# Input nama dan kunci dari pengguna
nama = input("Masukkan nama: ")
kunci = input("Masukkan kunci: ")

# Enkripsi teks
teks_terenkripsi = vigenere_encrypt(nama, kunci)
print("Teks Terenkripsi:", teks_terenkripsi)

# Dekripsi teks
teks_terdekripsi = vigenere_decrypt(teks_terenkripsi, kunci)
print("Teks Terdekripsi:", teks_terdekripsi)
