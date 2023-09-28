# Fungsi untuk menghitung nilai akhir mahasiswa
def hitung_nilai_akhir(uts, uas):
    # Hitung nilai akhir dengan rumus tertentu (misalnya rata-rata)
    nilai_akhir = (uts + uas) / 2
    return nilai_akhir

# Fungsi untuk menghitung nilai akhir semua mahasiswa
def hitung_semua_nilai_akhir(data_mahasiswa):
    data_nilai_akhir = {}
    for nama, nilai in data_mahasiswa.items():
        uts = nilai["uts"]
        uas = nilai["uas"]
        nilai_akhir = hitung_nilai_akhir(uts, uas)
        data_nilai_akhir[nama] = nilai_akhir
    return data_nilai_akhir

# Fungsi untuk menampilkan hasil nilai akhir
def tampilkan_nilai_akhir(data_nilai_akhir):
    print("Hasil Nilai Akhir Mahasiswa:")
    for nama, nilai_akhir in data_nilai_akhir.items():
        print("Nama: {}\tNilai Akhir: {:.2f}".format(nama, nilai_akhir))

# Program utama
def main():
    data_mahasiswa = {
        "Ardan": {"uts": 80, "uas": 85},
        "Tyo": {"uts": 75, "uas": 90},
        "Rahmandaries.": {"uts": 90, "uas": 78},
        # Tambahkan data mahasiswa lainnya di sini
    }

    data_nilai_akhir = hitung_semua_nilai_akhir(data_mahasiswa)

    tampilkan_nilai_akhir(data_nilai_akhir)

if __name__ == "__main__":
    main()
