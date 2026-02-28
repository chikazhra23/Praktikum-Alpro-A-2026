try:
    angka1 = float(input("Masukkan angka pertama: "))
    angka2 = float(input("Masukkan angka kedua: "))

    hasil = angka1 / angka2
    print(f"Hasil pembagian: {hasil}")

except ValueError:
    print("Error: Input harus berupa angka!")

except ZeroDivisionError:
    print("Error: Tidak bisa membagi dengan nol!")

except Exception as e:
    print(f"Error tidak terduga: {e}")

finally:
    print("Program selesai.")