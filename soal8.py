# Daftar produk beserta kategori dan harga
produk_list = [
    {"nama": "TV", "kategori": "elektronik", "harga": 1000},
    {"nama": "headphone", "kategori": "elektronik", "harga": 200},
    {"nama": "baju", "kategori": "fashion", "harga": 50},
    {"nama": "gitar", "kategori": "musik", "harga": 300},
    {"nama": "sepatu", "kategori": "olahraga", "harga": 80},
    {"nama": "kamera", "kategori": "elektronik", "harga": 600},
]

# Daftar pelanggan beserta minat dan barang yang telah dibeli
pelanggan_data = {
    "Rina": {"minat": ["elektronik", "musik"], "beli": ["TV", "headphone"]},
    "Budi": {"minat": ["fashion", "musik"], "beli": ["baju", "gitar"]},
    "Hartono": {"minat": ["olahraga", "elektronik"], "beli": ["sepatu", "kamera"]},
}

# Fungsi untuk memberikan rekomendasi produk berdasarkan minat pelanggan
def rekomendasi_produk(pelanggan):
    minat_pelanggan = set(pelanggan_data[pelanggan]["minat"])
    produk_rekomendasi = []

    for produk in produk_list:
        if produk["kategori"] in minat_pelanggan and produk["nama"] not in pelanggan_data[pelanggan]["beli"]:
            produk_rekomendasi.append(produk["nama"])

    return produk_rekomendasi

# Menampilkan rekomendasi produk untuk setiap pelanggan
for pelanggan in pelanggan_data:
    hasil_rekomendasi = rekomendasi_produk(pelanggan)
    print(f"{pelanggan}: {hasil_rekomendasi}")
