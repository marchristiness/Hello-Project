# nomor 2

# buka file, read, dan split berdasarkan new line
data = open('hore.txt', 'r')
data = data.read().splitlines()

# deklarasi dictionary dan proses data, lalu masukkan
# ke dictionary
data_nilai = {}
for nilai in data:
    # split berdasarkan tab, ambil index pertama sebagai nim dan
    # evaluasi sisa elemen list agar menjadi int
    siswa = nilai.split('\t')
    nim = siswa[0]
    semua_nilai = [int(siswa[i]) for i in range(1, len(siswa))]

    # masukkan nim dan data nilai ke dict, nim sebagai key dan
    # data nilai berupa list int sebagai value
    data_nilai.update({nim: semua_nilai})

# daftar deklarasi fungsi
def indeks(nomor_induk: str, daftar_nilai: dict):
    # coba ambil data dari dict berdasarkan nim yang dioper sebagai parameter,
    # apabila KeyError (tidak ada key dengan nama demikian) dalam dict yang di-pass
    # kepada fungsi maka akhiri proses data dan return Error kepada user; untuk support main program
    try:
        # string baru yang akan diisi indeks nilai, dimulai dengan nim.
        # format sesuai dengan file txt tetapi nilai diganti dgn indeks
        nama_nilai = nomor_induk
        # coba ambil data dari dict dengan key nomor induk, jika error
        # maka proses akan berhenti dan tidak akan masuk for loop. variable nama
        # adalah list yang berisi nilai mhs berupa angka
        nama = daftar_nilai[nomor_induk]
        # loop tiap skor yang berada dalam list data nilai yang di-assign pada
        # variable 'nama' di atas
        for skor in nama:
            if skor > 80:
                nama_nilai += "\tA"
            elif skor > 70:
                nama_nilai += "\tAB"
            elif skor > 65:
                nama_nilai += "\tB"
            elif skor > 60:
                nama_nilai += "\tBC"
            elif skor > 50:
                nama_nilai += "\tC"
            elif skor > 40:
                nama_nilai += "\tD"
            else:
                nama_nilai += "\tE"
        # apabila berhasil, maka return string baru, dengan format:
        # "NIM\tindeks CLO1\tindeks CLO2\tindeks CLO3\tindeks CLO4; \t = tab"
        # contoh:
        # "Maria    A   AB  AB   A"
        return nama_nilai
    except KeyError:
        raise KeyError


def report(daftar_nilai: dict):
    # dict tambahan untuk menyimpan jumlah siswa dengan nilai A dan AB
    # pada tiap matkul
    jumlah_A_AB = {'CLO1': [0, 0], 'CLO2': [0, 0], 'CLO3': [0, 0], 'CLO4': [0, 0]}
    # list untuk menyimpan siswa dengan nilai yg sdh diubah ke indeks nilai
    indeks_siswa = []
    for siswa_siswi in daftar_nilai.items():
        # gunakan fungsi indeks utk ubah nilai jadi indeks nilai & append list
        murid_sekarang = indeks(siswa_siswi[0], daftar_nilai)
        indeks_siswa.append(murid_sekarang)
        # enumerate digunakan sbg counter utk melihat index
        # skrg saat iterasi
        for index, scores in enumerate(siswa_siswi[1]):
            # matkul sekarang, dimulai dari CLO1 sampai terakhir CLO4
            # untuk ambil dan update data dari dict tambahan di atas
            matkul = f"CLO{index + 1}"
            if scores > 80:
                jumlah_A_AB[matkul][0] = jumlah_A_AB[matkul][0] + 1
            elif scores > 70:
                jumlah_A_AB[matkul][1] = jumlah_A_AB[matkul][1] + 1
    # return list indeks siswa dan jumlah nilai A dan AB tiap matkul
    return indeks_siswa, jumlah_A_AB


# fungsi tambahan untuk mengeprint report
def print_report(data_yg_akan_diprint: tuple):
    # langsung assign pada 2 variable karena parameter berupa tuple, indeks_murid
    # berupa list dan banyak_A_AB_murid berupa dict, lalu print masing"
    indeks_murid, banyak_A_AB_murid = data_yg_akan_diprint
    print("\nIndeks nilai semua mahasiswa: ")
    for i in indeks_murid:
        print(i)
    print("\nLaporan jumlah mahasiswa terbaik pada setiap mata kuliah:")
    for j in banyak_A_AB_murid.items():
        print(f"\nMata kuliah = {j[0][:3]} {j[0][-1]}\n"
              f"Nilai A = {j[1][0]} mahasiswa\n"
              f"Nilai AB = {j[1][1]} mahasiswa")

# main program
print(data_nilai)
for nim, nilai in data_nilai.items():
    print(f"{nim}: {nilai}")
nim = str(input("\nInput nim yang akan dianalisa, \n"
                "(ketik 'semua' dan tekan Enter pada keyboard apabila ingin menampilkan semua nim) = "))
laporan = report(data_nilai)
if 'semua' in nim.lower():
    print("\nSemua mahasiswa dengan indeks nilai masing-masing dan juga banyaknya mahasiswa yang "
          "\nmendapatkan nilai A dan AB pada setiap mata kuliah dapat dilihat pada laporan berikut: ")
    print_report(laporan)
else:
    try:
        indks = indeks(nim, data_nilai)
        print(f"\nMahasiswa dengan nim {nim} mempunyai data indeks nilai sebagai berikut:\n"
              f"{indks}")
        print("\nSemua mahasiswa dengan indeks nilai masing-masing dan juga banyaknya mahasiswa yang "
              "\nmendapatkan nilai A dan AB pada setiap mata kuliah dapat dilihat pada laporan berikut: ")
        print_report(laporan)
    except KeyError:
        print("Tidak ada mahasiswa dengan nim tersebut, silakan coba lagi.")
