def hitung_kembalian(total_pembayaran, total_belanja):
    pecahan = [100000, 50000, 20000, 10000, 5000, 2000, 1000, 500, 200, 100]
    kembalian = total_pembayaran - total_belanja

    hasil_kembalian = {}

    for nilai in pecahan:
        if kembalian >= nilai:
            jumlah = kembalian // nilai
            kembalian %= nilai
            hasil_kembalian[str(nilai)] = jumlah

    return hasil_kembalian

# Test case 1
total_pembayaran_1 = 10000
total_belanja_1 = 7500
hasil_kembalian_1 = hitung_kembalian(total_pembayaran_1, total_belanja_1)
print(hasil_kembalian_1)

# Test case 2
total_pembayaran_2 = 5000
total_belanja_2 = 1100
hasil_kembalian_2 = hitung_kembalian(total_pembayaran_2, total_belanja_2)
print(hasil_kembalian_2)

# Test case 3
total_pembayaran_3 = 178000
total_belanja_3 = 90500
hasil_kembalian_3 = hitung_kembalian(total_pembayaran_3, total_belanja_3)
print(hasil_kembalian_3)
