
urutan_kedatangan = ["Ningguang", "Hutao", "Xiao", "Childe"]

kebiasaan = {
    "Ningguang": "Memeriksa kue",
    "Hutao": "Memberikan kado",
    "Xiao": "Memotret pertama kali",
    "Childe": "Meletakkan air mineral"
}


foto_xiao = "Kue utuh di meja"


tersangka = None


for teman in urutan_kedatangan:
    if kebiasaan[teman] == "Memotret pertama kali" and foto_xiao == "Kue utuh di meja":
        tersangka = teman
        break


if tersangka:
    print(f"Berdasarkan investigasi, {tersangka} adalah tersangka yang paling mungkin mengambil kue.")
else:
    print("Tidak ada yang dapat diidentifikasi sebagai tersangka.")
