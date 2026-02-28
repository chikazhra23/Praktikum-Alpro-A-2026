print("=== REGISTRASI PESERTA SEMINAR ===")

# =========================
# Custom Exception
# =========================

class NamaError(Exception):
    pass

class UmurError(Exception):
    pass


# =========================
# Validasi Nama
# =========================

while True:
    try:
        nama = input("Nama lengkap: ")

        if len(nama) < 3:
            raise NamaError("Nama terlalu pendek! Minimal 3 karakter.")

        break

    except NamaError as e:
        print(f"  [ERROR] {e}")

    finally:
        print("Proses input selesai.")


# =========================
# Validasi Umur
# =========================

while True:
    try:
        umur = int(input("Umur: "))

        if umur < 17 or umur > 60:
            raise UmurError("Umur tidak memenuhi syarat (17-60 tahun).")

        break

    except ValueError:
        print("  [ERROR] Umur harus berupa angka!")

    except UmurError as e:
        print(f"  [ERROR] {e}")

    finally:
        print("Proses input selesai.")


# =========================
# Validasi Email
# =========================

while True:
    try:
        email = input("Email: ")

        if "@" not in email:
            raise ValueError("Email tidak valid! Harus mengandung '@'.")

        break

    except ValueError as e:
        print(f"  [ERROR] {e}")

    finally:
        print("Proses input selesai.")


# =========================
# Validasi No HP
# =========================

while True:
    try:
        no_hp = input("No HP: ")

        if not no_hp.isdigit():
            raise ValueError("No HP harus berupa angka!")

        if len(no_hp) < 10 or len(no_hp) > 13:
            raise ValueError("No HP tidak valid! Harus 10-13 digit angka.")

        break

    except ValueError as e:
        print(f"  [ERROR] {e}")

    finally:
        print("Proses input selesai.")


# =========================
# Output Data
# =========================

print("\n=== DATA PESERTA ===")
print(f"Nama   : {nama}")
print(f"Umur   : {umur} tahun")
print(f"Email  : {email}")
print(f"No HP  : {no_hp}")
print("Status : TERDAFTAR")