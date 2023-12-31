from collections import Counter

def analisis_anak(nama_anak):
    # Menghitung jumlah kemunculan setiap nama anak
    counter_anak = Counter(nama_anak)

    # Mengurutkan nama anak berdasarkan jumlah kemunculan (dari paling banyak ke paling sedikit)
    anak_terbanyak = counter_anak.most_common()

    # Menampilkan hasil
    if anak_terbanyak[0][1] == anak_terbanyak[-1][1]:
        print("Semuanya anak baik")
    else:
        nama_anak_nakal = [nama for nama, jumlah in anak_terbanyak if jumlah == anak_terbanyak[0][1]]
        print(f"{', '.join(nama_anak_nakal)} Nackal")

# Test case 1
nama_anak_1 = ["Bagas", "Dimas", "Bagas", "Bagas", "Indra", "Gilang", "Gilang", "Hana", "Fajar", "Fajar"]
analisis_anak(nama_anak_1)

# Test case 2
nama_anak_2 = ["Bagas", "Dimas", "Fajar", "Bagas", "Indra", "Gilang", "Gilang", "Bagas", "Fajar", "Fajar"]
analisis_anak(nama_anak_2)

# Test case 3
nama_anak_3 = ["Aisyah", "Bagas", "Dewi", "Dimas", "Eka", "Fajar", "Gilang", "Hana", "Indra", "Jihan"]
analisis_anak(nama_anak_3)
