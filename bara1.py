class Buku:
    def __init__(self, id_buku, judul, penulis, tahun):
        self.id_buku = id_buku
        self.judul = judul
        self.penulis = penulis
        self.tahun = tahun
    
    def __str__(self):
        return f"ID: {self.id_buku}, Judul: {self.judul}, Penulis: {self.penulis}, Tahun: {self.tahun}"

class Peminjaman:
    def __init__(self, id_peminjaman, buku, nama_peminjam, tanggal_pinjam, tanggal_kembali=None):
        self.id_peminjaman = id_peminjaman
        self.buku = buku
        self.nama_peminjam = nama_peminjam
        self.tanggal_pinjam = tanggal_pinjam
        self.tanggal_kembali = tanggal_kembali
    
    def __str__(self):
        kembali = self.tanggal_kembali if self.tanggal_kembali else "Belum dikembalikan"
        return (f"ID Peminjaman: {self.id_peminjaman}, Buku: {self.buku.judul}, "
                f"Peminjam: {self.nama_peminjam}, Tanggal Pinjam: {self.tanggal_pinjam}, "
                f"Tanggal Kembali: {kembali}")

# List buku
daftar_buku = []

# Fungsi CRUD Buku
def tambah_buku(id_buku, judul, penulis, tahun):
    buku_baru = Buku(id_buku, judul, penulis, tahun)
    daftar_buku.append(buku_baru)
    print("Buku berhasil ditambahkan.")

def lihat_buku():
    if not daftar_buku:
        print("Belum ada buku.")
    else:
        print("Daftar Buku:")
        for buku in daftar_buku:
            print(buku)

def cari_buku(id_buku):
    for buku in daftar_buku:
        if buku.id_buku == id_buku:
            return buku
    return None

def hapus_buku(id_buku):
    global daftar_buku
    buku = cari_buku(id_buku)
    if buku:
        daftar_buku = [b for b in daftar_buku if b.id_buku != id_buku]
        print("Buku berhasil dihapus.")
    else:
        print("Buku tidak ditemukan.")

# Contoh penggunaan
if __name__ == "__main__":
    tambah_buku("B001", "Pemrograman Python", "Andi", 2020)
    tambah_buku("B002", "Belajar Data Science", "Budi", 2021)
    
    lihat_buku()

    buku = cari_buku("B001")
    if buku:
        print("Buku ditemukan:", buku)
    else:
        print("Buku tidak ditemukan.")
    
    hapus_buku("B002")
    lihat_buku()