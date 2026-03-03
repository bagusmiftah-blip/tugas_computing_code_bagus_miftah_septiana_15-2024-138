import time
import multiprocessing

def hitung_kuadrat(n):
    return n * n

if __name__ == "__main__":
    data = list(range(1, 10_000_000))

    start = time.time()

    # Membuat pool sesuai jumlah core CPU
    with multiprocessing.Pool() as pool:
        hasil = pool.map(hitung_kuadrat, data)

    end = time.time()

    print("Total data:", len(hasil))
    print("Waktu eksekusi parallel:", end - start, "detik")
