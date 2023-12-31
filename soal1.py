a = int(input("Masukkan jumlah nilai :"))
b = []
for i in range (a):
    c = int(input("Masukan nilai:"))
    b.append(c)

print("nilai tertinggi : ",max(b))
print("nilai terendah : ",min(b))
print("nilai rata-rata : ",(sum(b)/a))
