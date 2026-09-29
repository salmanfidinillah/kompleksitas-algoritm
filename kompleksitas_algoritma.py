"""Menghitung operasi pada algoritma pencarian nama mahasiswa.

Model penghitungan mengikuti worksheet:
    c1: langkah = 0       -> 1 operasi
    c2: langkah += 1       -> 1 operasi setiap nama diperiksa
    c3: nama == target     -> 1 operasi setiap perbandingan
    c4: return langkah     -> 1 operasi

Jika target ditemukan pada posisi ke-k, pola jumlah operasinya adalah
T(k) = 1 + k + k + 1 = 2k + 2.
"""

from dataclasses import dataclass


@dataclass
class HasilPencarian:
    """Ringkasan hasil pencarian dan rincian operasinya."""

    target: str
    posisi: int | None
    langkah: int
    inisialisasi: int
    penambahan_langkah: int
    perbandingan: int
    return_value: int

    @property
    def total_operasi(self) -> int:
        """Total operasi sesuai model pada worksheet."""

        return (
            self.inisialisasi
            + self.penambahan_langkah
            + self.perbandingan
            + self.return_value
        )


def cari_nama(nama_mahasiswa: list[str], target: str) -> HasilPencarian:
    """Cari *target* secara linear dan hitung operasi yang dilakukan.

    Pencarian berhenti saat target ditemukan. Jika target tidak ada, seluruh
    daftar diperiksa dan fungsi tetap mengembalikan jumlah langkahnya.
    """

    langkah = 0  # c1: 1 operasi
    penambahan_langkah = 0
    perbandingan = 0
    posisi = None

    for indeks, nama in enumerate(nama_mahasiswa, start=1):
        langkah += 1  # c2
        penambahan_langkah += 1

        perbandingan += 1  # c3: nama == target
        if nama == target:
            posisi = indeks
            break

    return HasilPencarian(
        target=target,
        posisi=posisi,
        langkah=langkah,
        inisialisasi=1,
        penambahan_langkah=penambahan_langkah,
        perbandingan=perbandingan,
        return_value=1,  # c4: return langkah
    )


def buat_daftar(n: int) -> list[str]:
    """Buat daftar nama dengan target berada di posisi terakhir."""

    if n < 1:
        raise ValueError("n harus lebih besar atau sama dengan 1")

    return [f"Mahasiswa-{indeks}" for indeks in range(1, n)] + [f"Target-{n}"]


def tampilkan_rincian(hasil: HasilPencarian) -> None:
    """Tampilkan rincian operasi untuk satu hasil pencarian."""

    print(f"Target                 : {hasil.target}")
    print(f"Posisi target          : {hasil.posisi or 'tidak ditemukan'}")
    print(f"c1 - langkah = 0       : {hasil.inisialisasi} kali")
    print(f"c2 - langkah += 1      : {hasil.penambahan_langkah} kali")
    print(f"c3 - nama == target    : {hasil.perbandingan} kali")
    print(f"c4 - return langkah    : {hasil.return_value} kali")
    print(f"Total operasi          : {hasil.total_operasi}")


def tampilkan_tabel_target_terakhir() -> None:
    """Tampilkan pola T(n) untuk target di posisi terakhir."""

    print("\nPola T(n) untuk target di posisi terakhir")
    print("n     Operasi aktual     Rumus 2n + 2")
    print("-" * 39)

    for n in (5, 10, 20, 50, 100):
        hasil = cari_nama(buat_daftar(n), f"Target-{n}")
        print(f"{n:<5} {hasil.total_operasi:<19} {2 * n + 2}")


def main() -> None:
    """Jalankan contoh worksheet dan tabel pola kompleksitas."""

    daftar_contoh = ["Andi", "Budi", "Citra", "Dina", "Eka"]
    hasil_contoh = cari_nama(daftar_contoh, "Eka")

    print("=== Pencarian Nama Mahasiswa ===")
    tampilkan_rincian(hasil_contoh)
    tampilkan_tabel_target_terakhir()


if __name__ == "__main__":
    main()
