
# UTS Dasar Komputer dan Pemrograman
# Kelompok D - Kontrol
# Monitoring Error terhadap Setpoint

# 1. DATA INPUT
setpoint = 50

data_output = [
    50, 49, 47, 45, 43,
    52, 54, 57, 51, 48,
    46, 44, 53, 55, 42,
    48, 47, 45, 44, 60
]


# 2. FUNCTION UNTUK MENENTUKAN STATUS
def tentukan_status(error):
    if error <= 2:
        return "STABIL"
    elif error <= 5:
        return "WARNING"
    else:
        return "TIDAK STABIL"


# 3. FUNCTION UNTUK MENGHITUNG ERROR
def hitung_error(setpoint, output):
    error = abs(setpoint - output)
    return error


# 4. FUNCTION UNTUK MENGHITUNG RINGKASAN
def hitung_ringkasan(data_error):
    total = len(data_error)
    stabil = 0
    warning = 0
    tidak_stabil = 0

    for error in data_error:
        if error <= 2:
            stabil += 1
        elif error <= 5:
            warning += 1
        else:
            tidak_stabil += 1

    rata_rata = sum(data_error) / total
    error_maksimum = max(data_error)
    error_minimum = min(data_error)

    return total, stabil, warning, tidak_stabil, rata_rata, error_maksimum, error_minimum


# 5. PROSES DATA DAN MENAMPILKAN HASIL
def tampilkan_data(setpoint, data_output):
    daftar_error = []

    print("==========================================")
    print(" MONITORING ERROR TERHADAP SETPOINT")
    print("==========================================")
    print("Setpoint:", setpoint)
    print("------------------------------------------")
    print("No | Output | Error | Status")
    print("------------------------------------------")

    for i in range(len(data_output)):
        output = data_output[i]

        error = hitung_error(setpoint, output)
        status = tentukan_status(error)

        daftar_error.append(error)

        print(i + 1, "|", output, "|", error, "|", status)

    print("------------------------------------------")

    # Menghitung ringkasan
    hasil = hitung_ringkasan(daftar_error)

    total = hasil[0]
    stabil = hasil[1]
    warning = hasil[2]
    tidak_stabil = hasil[3]
    rata_rata = hasil[4]
    error_maksimum = hasil[5]
    error_minimum = hasil[6]

    print("\n========== RINGKASAN HASIL ==========")
    print("Total data       :", total)
    print("Jumlah STABIL    :", stabil)
    print("Jumlah WARNING   :", warning)
    print("Jumlah TIDAK STABIL:", tidak_stabil)
    print("Rata-rata error  :", round(rata_rata, 2))
    print("Error maksimum   :", error_maksimum)
    print("Error minimum    :", error_minimum)
    print("=====================================")


# 6. MENJALANKAN PROGRAM
tampilkan_data(setpoint, data_output)
