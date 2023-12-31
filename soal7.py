def decrypt_chat(encrypted_text):
    decrypted_text = ""
    for char in encrypted_text:
        # Mengecek apakah karakter adalah huruf alfabet
        if char.isalpha():
            # Mendekripsi karakter dengan menggeser ke kiri sebanyak 5 langkah
            decrypted_char = chr((ord(char) - 5 - ord('A')) % 26 + ord('A')) if char.isupper() else \
                             chr((ord(char) - 5 - ord('a')) % 26 + ord('a'))
            decrypted_text += decrypted_char
        else:
            # Menambahkan karakter non-alfabet tanpa perubahan
            decrypted_text += char

    return decrypted_text

# Isi Chat yang dienkripsi
encrypted_chat = """
xfqfr bfmdz
gjxtp lzj rfz ifkyfw jxi snm
gwt, gjxtp qz rfz rfpfs in bfwlty lfp?
fpz xfdfsl pfrz, rfz lfp ofin ufhfwpz
dfsl pnwnr xynhpjw otrtp pz pnhp ifwn lwzu
"""

# Mendekripsi isi chat
decrypted_chat = decrypt_chat(encrypted_chat)

# Menampilkan hasil dekripsi
print("Isi Chat yang Didekripsi:")
print(decrypted_chat)
