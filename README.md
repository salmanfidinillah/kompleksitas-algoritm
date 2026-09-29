# Kompleksitas Algoritma

Program Python ini dibuat berdasarkan worksheet **Menghitung Operasi dan Rumus T(n)**.
Kasus yang digunakan adalah pencarian nama mahasiswa secara linear.

## Model perhitungan

- `c1`: `langkah = 0` dihitung 1 kali.
- `c2`: `langkah += 1` dihitung setiap nama diperiksa.
- `c3`: `nama == target` dihitung setiap perbandingan.
- `c4`: `return langkah` dihitung 1 kali.

Jika target berada pada posisi ke-`k`, jumlah operasinya:

```text
T(k) = 1 + k + k + 1 = 2k + 2
```

Untuk target di posisi terakhir, `k = n`, sehingga `T(n) = 2n + 2`.

## Menjalankan program

Pastikan Python 3.10 atau yang lebih baru sudah terpasang, lalu jalankan:

```bash
python kompleksitas_algoritma.py
```

Program menampilkan rincian operasi untuk contoh target `Eka` di posisi ke-5 dan
tabel pola untuk `n = 5, 10, 20, 50, 100`.

## Dosen

Hardika Khusnuliawati, S.Kom., M.Kom
