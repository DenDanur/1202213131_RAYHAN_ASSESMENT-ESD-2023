def cekpalindrom(input_str):
    cleaned_str = input_str.replace(" ", "").lower()
    return cleaned_str == cleaned_str[::-1]


a = input("masukkan kata :")

if cekpalindrom(a):
    print("suka blyat")
else:
    print("eureeka!")