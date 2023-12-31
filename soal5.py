def generate_usernames(full_name):
    
    full_name_no_space = ''.join(full_name.split())

    
    all_usernames = []

    
    for length in range(1, 7):
        
        for i in range(len(full_name_no_space) - length + 1):
            username = full_name_no_space[i:i + length]
            all_usernames.append(username)

    return all_usernames


nama_lengkap = "Naip Lovyu"


usernames = generate_usernames(nama_lengkap)


print("Jumlah kombinasi username yang mungkin:", len(usernames))
print("Contoh beberapa username:", usernames[:10])  
