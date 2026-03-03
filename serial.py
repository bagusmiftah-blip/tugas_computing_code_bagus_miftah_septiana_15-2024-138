# Program Serial Computing
# Menghitung total, rata-rata, nilai maksimum, dan minimum secara berurutan

def serial_computing(data):
    total = 0
    maksimum = data[0]
    minimum = data[0]

    # Proses dilakukan satu per satu (serial)
    for angka in data:
        total += angka
        
        if angka > maksimum:
            maksimum = angka
            
        if angka < minimum:
            minimum = angka

    rata_rata = total / len(data)

    return total, rata_rata, maksimum, minimum


# Program utama
if __name__ == "__main__":
    data = [10, 25, 7, 40, 15, 3, 22]

    total, rata_rata, maksimum, minimum = serial_computing(data)

    print("Data:", data)
    print("Total:", total)
    print("Rata-rata:", rata_rata)
    print("Nilai Maksimum:", maksimum)
    print("Nilai Minimum:", minimum)
