# import getpass karena modul ini digunakan untuk memasukkan kata sandi secara aman.
import getpass

# Dictionary dengan data karyawan
employees = {
    1:  {'Nama': 'Abiyyu Garibaldi', 'Umur': 28, 'Departemen': 'HR', 'Nomor Induk Karyawan': '0101514001', 'e-mail': 'abiyyu@tp.co.id', 'Status Perkawinan': 'Menikah'},
    2:  {'Nama': 'Alfiansyah', 'Umur': 30, 'Departemen': 'Accounting', 'Nomor Induk Karyawan': '0101514002', 'e-mail': 'alfi@tp.co.id', 'Status Perkawinan': 'Belum Menikah'},
    3:  {'Nama': 'Anggitaridha Septirendini', 'Umur': 28, 'Departemen': 'IT', 'Nomor Induk Karyawan': '0101514003', 'e-mail': 'anggitaridha@tp.co.id', 'Status Perkawinan': 'Menikah'},
    4:  {'Nama': 'Annisa Rahmah', 'Umur': 27, 'Departemen': 'Accounting', 'Nomor Induk Karyawan': '0101514004', 'e-mail': 'annisa@tp.co.id', 'Status Perkawinan': 'Belum Menikah'},
    5:  {'Nama': 'Aprillia Apuadji', 'Umur': 27, 'Departemen': 'HR', 'Nomor Induk Karyawan': '0101514005', 'e-mail': 'aprill@tp.co.id', 'Status Perkawinan': 'Belum Menikah'},
    6:  {'Nama': 'Ari Kurniawan', 'Umur': 25, 'Departemen': 'IT', 'Nomor Induk Karyawan': '0101514006', 'e-mail': 'ari@tp.co.id', 'Status Perkawinan': 'Belum Menikah'},
    7:  {'Nama': 'Azhar Fahreza Nasution', 'Umur': 28, 'Departemen': 'Sales', 'Nomor Induk Karyawan': '0101514007', 'e-mail': 'azhar@tp.co.id', 'Status Perkawinan': 'Belum Menikah'},
    8:  {'Nama': 'Bari Pradana', 'Umur': 35, 'Departemen': 'Accounting', 'Nomor Induk Karyawan': '0101514008', 'e-mail': 'bari@tp.co.id', 'Status Perkawinan': 'Menikah'},
    9:  {'Nama': 'Biastomo Adi', 'Umur': 34, 'Departemen': 'Operational', 'Nomor Induk Karyawan': '0101514009', 'e-mail': 'biastomo@tp.co.id', 'Status Perkawinan': 'Menikah'},
    10: {'Nama': 'Bentang Fahmi', 'Umur': 29, 'Departemen': 'HR', 'Nomor Induk Karyawan': '0101514010', 'e-mail': 'bentang@tp.co.id', 'Status Perkawinan': 'Menikah'},
    11: {'Nama': 'Bulan Kencana', 'Umur': 33, 'Departemen': 'Transportasi', 'Nomor Induk Karyawan': '0101514011', 'e-mail': 'bulan@tp.co.id', 'Status Perkawinan': 'Belum Menikah'},
    12: {'Nama': 'Chaerunnisa', 'Umur': 28, 'Departemen': 'HR', 'Nomor Induk Karyawan': '0101514012', 'e-mail': 'chaerunnisa@tp.co.id', 'Status Perkawinan': 'Menikah'},
    13: {'Nama': 'Doni Triaji', 'Umur': 31, 'Departemen': 'Sales', 'Nomor Induk Karyawan': '0101514013', 'e-mail': 'doni@tp.co.id', 'Status Perkawinan': 'Menikah'},
    14: {'Nama': 'Elsa Anna', 'Umur': 36, 'Departemen': 'Transportasi', 'Nomor Induk Karyawan': '0101514014', 'e-mail': 'elsa@tp.co.id', 'Status Perkawinan': 'Menikah'},
    15: {'Nama': 'Fikri Ali', 'Umur': 28, 'Departemen': 'Operational', 'Nomor Induk Karyawan': '0101514015', 'e-mail': 'fikri@tp.co.id', 'Status Perkawinan': 'Menikah'},
    16: {'Nama': 'Gerald Syadza', 'Umur': 38, 'Departemen': 'Sales', 'Nomor Induk Karyawan': '0101514016', 'e-mail': 'gerald@tp.co.id', 'Status Perkawinan': 'Menikah'},
    17: {'Nama': 'Hans Luber', 'Umur': 32, 'Departemen': 'IT', 'Nomor Induk Karyawan': '0101514017', 'e-mail': 'hans@tp.co.id', 'Status Perkawinan': 'Menikah'},
    18: {'Nama': 'Humaira Azzahra', 'Umur': 22, 'Departemen': 'Operational', 'Nomor Induk Karyawan': '0101514018', 'e-mail': 'humaira@tp.co.id', 'Status Perkawinan': 'Belum Menikah'},
    19: {'Nama': 'Indra Mulky', 'Umur': 34, 'Departemen': 'Sales', 'Nomor Induk Karyawan': '0101514019', 'e-mail': 'indra@tp.co.id', 'Status Perkawinan': 'Belum Menikah'},
    20: {'Nama': 'Jaka Saputra', 'Umur': 34, 'Departemen': 'Accounting', 'Nomor Induk Karyawan': '0101514020', 'e-mail': 'jaka@tp.co.id', 'Status Perkawinan': 'Menikah'},
    21: {'Nama': 'Indah Agustin', 'Umur': 27, 'Departemen': 'Sales', 'Nomor Induk Karyawan': '0101514021', 'e-mail': 'indah@tp.co.id', 'Status Perkawinan': 'Belum Menikah'},
    22: {'Nama': 'Jihan Hana', 'Umur': 28, 'Departemen': 'Accounting', 'Nomor Induk Karyawan': '0101514022', 'e-mail': 'jihan@tp.co.id', 'Status Perkawinan': 'Menikah'},
    23: {'Nama': 'Jasmine Baidah', 'Umur': 38, 'Departemen': 'Operational', 'Nomor Induk Karyawan': '0101514023', 'e-mail': 'jasmine@tp.co.id', 'Status Perkawinan': 'Menikah'},
    24: {'Nama': 'Marcia Devana', 'Umur': 27, 'Departemen': 'HR', 'Nomor Induk Karyawan': '0101514024', 'e-mail': 'marcia@tp.co.id', 'Status Perkawinan': 'Menikah'},
    25: {'Nama': 'Marsha Violita', 'Umur': 33, 'Departemen': 'Sales', 'Nomor Induk Karyawan': '0101514025', 'e-mail': 'marsha@tp.co.id', 'Status Perkawinan': 'Menikah'},
    26: {'Nama': 'Marvi Rosadi', 'Umur': 34, 'Departemen': 'Operational', 'Nomor Induk Karyawan': '0101514026', 'e-mail': 'marvi@tp.co.id', 'Status Perkawinan': 'Menikah'},
    27: {'Nama': 'Nizar Ridho', 'Umur': 29, 'Departemen': 'Accounting', 'Nomor Induk Karyawan': '0101514027', 'e-mail': 'nizar@tp.co.id', 'Status Perkawinan': 'Belum Menikah'},
    28: {'Nama': 'Septiananda Aditya', 'Umur': 28, 'Departemen': 'Transportasi', 'Nomor Induk Karyawan': '0101514028', 'e-mail': 'septian@tp.co.id', 'Status Perkawinan': 'Menikah'},
    29: {'Nama': 'Silma Pratiwi', 'Umur': 28, 'Departemen': 'HR', 'Nomor Induk Karyawan': '0101514029', 'e-mail': 'silma@tp.co.id', 'Status Perkawinan': 'Menikah'},
    30: {'Nama': 'Tegar Cahyo', 'Umur': 28, 'Departemen': 'Accounting', 'Nomor Induk Karyawan': '0101514030', 'e-mail': 'tegar@tp.co.id', 'Status Perkawinan': 'Belum Menikah'},
}

# EmployeeManagement: Kelas yang mengelola operasi terkait karyawan.
class EmployeeManagement:
    def __init__(self):                      # init: Inisialisasi objek, mengatur data karyawan, menentukan ID berikutnya, dan menetapkan data login.
        self.employees = employees
        self.next_id = max(self.employees.keys()) + 1
        # Data login
        self.users = {
            'admin': 'password',  # username: password
            'user1': '123456',
            'user2': 'password123',
            'chiaihchii': '20maret',  # Tambahkan pasangan username dan password ini
            # Tambahkan pasangan username dan password yang diinginkan di sini
        }

# login: Memeriksa apakah username dan password cocok dengan data yang ada, mengembalikan True jika berhasil, False jika gagal.
    def login(self, username, password):
        if self.users.get(username) == password:       
            print("\n      ----*** Login berhasil! ***----\n\n")
            return True
        else:
            print("Login gagal.")
            return False

# Detail fungsi untuk menambah karyawan
    def add_employee(self):
        print("\n\nKetik 'cancel' untuk kembali ke main menu.\n")
        nama = input("Masukkan Nama: ")
        if nama.lower() == 'cancel':
            return

        while True:
            umur = input("Masukkan Umur: ")
            if umur.lower() == 'cancel':
                return
            try:
                umur = int(umur)
                break
            except ValueError:
                print("Umur harus berupa angka. Silakan coba lagi.")

        departemen = input("Masukkan Departemen: ")
        if departemen.lower() == 'cancel':
            return

        nomor_induk = input("Masukkan Nomor Induk Karyawan: ")
        if nomor_induk.lower() == 'cancel':
            return

        # Cek duplikasi berdasarkan Nomor Induk Karyawan
        for emp_id, employee in self.employees.items():
            if employee['Nomor Induk Karyawan'] == nomor_induk:
                print(f"\nKaryawan dengan Nomor Induk Karyawan {nomor_induk} sudah ada dalam sistem.\n")
                print(f"ID: {emp_id}")
                print(f"Nama: {employee['Nama']}")
                print(f"Umur: {employee['Umur']}")
                print(f"Departemen: {employee['Departemen']}")
                print(f"Nomor Induk Karyawan: {employee['Nomor Induk Karyawan']}")
                print(f"e-mail: {employee['e-mail']}")
                print(f"Status Perkawinan: {employee['Status Perkawinan']}")
                return

        email = input("Masukkan e-mail: ")
        if email.lower() == 'cancel':
            return

        status_perkawinan = input("Masukkan Status Perkawinan: ")
        if status_perkawinan.lower() == 'cancel':
            return

        print("\nData yang dimasukkan:")
        print(f"Nama: {nama}")
        print(f"Umur: {umur}")
        print(f"Departemen: {departemen}")
        print(f"Nomor Induk Karyawan: {nomor_induk}")
        print(f"e-mail: {email}")
        print(f"Status Perkawinan: {status_perkawinan}")

        confirmation = input("\nApakah Anda yakin ingin menambahkan karyawan ini? (y/n): ").lower()
        if confirmation == 'y':
            self.employees[self.next_id] = {
                'Nama': nama,
                'Umur': umur,
                'Departemen': departemen,
                'Nomor Induk Karyawan': nomor_induk,
                'e-mail': email,
                'Status Perkawinan': status_perkawinan
            }
            print(f"Karyawan dengan ID {self.next_id} berhasil ditambahkan.")
            self.next_id += 1
        else:
            print("Penambahan karyawan dibatalkan.")

# Menampilkan daftar karyawan
    def list_employees(self):                  #  list_employees: Menampilkan semua karyawan yang ada dalam format tabel.
        header = f"{'ID':<5} {'Nama':<25} {'Umur':<5} {'Departemen':<15} {'Nomor Induk Karyawan':<20} {'e-mail':<25} {'Status Perkawinan':<15}"
        print(f"\n{header}")
        print("=" * len(header))
        for id, data in self.employees.items():
            row = f"{id:<5} {data['Nama']:<25} {data['Umur']:<5} {data['Departemen']:<15} {data['Nomor Induk Karyawan']:<20} {data['e-mail']:<25} {data['Status Perkawinan']:<15}"
            print(row)

# Mencari karyawan berdasarkan ID, Nomor Induk Karyawan, atau Nama
    def search_employee(self):
        search_term = input("Masukkan ID, Nomor Induk Karyawan, atau Nama karyawan yang akan dicari: ")
        found_employees = []

        # Search for employees by ID, Nomor Induk Karyawan, or Nama
        for id, data in self.employees.items():
            if str(id) == search_term or data['Nomor Induk Karyawan'] == search_term or search_term.lower() in data['Nama'].lower():
                found_employees.append(id)

        if found_employees:
            print("\nData karyawan ditemukan:")
            for emp_id in found_employees:
                print(f"ID: {emp_id} | Nama: {self.employees[emp_id]['Nama']} | Nomor Induk Karyawan: {self.employees[emp_id]['Nomor Induk Karyawan']}")
            
            if len(found_employees) > 1:
                while True:
                    selected_id = input("\nMasukkan ID atau Nomor Induk Karyawan dari karyawan yang ingin dilihat: ")
                    for emp_id in found_employees:
                        if str(emp_id) == selected_id or self.employees[emp_id]['Nomor Induk Karyawan'] == selected_id:
                            found_employee_id = emp_id
                            break
                    else:
                        print("\n!!!Pilihan tidak valid. Silakan coba lagi!!!")
                        continue
                    break
            else:
                found_employee_id = found_employees[0]

            print("\nData karyawan yang dipilih:\n")
            self.display_employee_details(found_employee_id)
        else:
            print("\n!!!Karyawan tidak ditemukan!!!")

# Menampilkan detail karyawan berdasarkan ID
    def display_employee_details(self, employee_id):
        print("\nData karyawan:\n")
        print(f"ID: {employee_id}")
        print(f"Nama: {self.employees[employee_id]['Nama']}")
        print(f"Umur: {self.employees[employee_id]['Umur']}")
        print(f"Departemen: {self.employees[employee_id]['Departemen']}")
        print(f"Nomor Induk Karyawan: {self.employees[employee_id]['Nomor Induk Karyawan']}")
        print(f"e-mail: {self.employees[employee_id]['e-mail']}")
        print(f"Status Perkawinan: {self.employees[employee_id]['Status Perkawinan']}")

# Memperbarui data karyawan
    def update_employee(self):
        search_term = input("\nMasukkan ID, Nomor Induk Karyawan, atau Nama karyawan yang akan diperbarui: ")
        found_employees = []

        # Search for employees by ID, Nomor Induk Karyawan, or Nama
        for id, data in self.employees.items():
            if str(id) == search_term or data['Nomor Induk Karyawan'] == search_term or search_term.lower() in data['Nama'].lower():
                found_employees.append(id)

        if found_employees:
            print("\nData karyawan ditemukan:")
            for emp_id in found_employees:
                print(f"ID: {emp_id} | Nama: {self.employees[emp_id]['Nama']} | Nomor Induk Karyawan: {self.employees[emp_id]['Nomor Induk Karyawan']}")
            
            if len(found_employees) > 1:
                while True:
                    selected_id = input("\nMasukkan ID atau Nomor Induk Karyawan dari karyawan yang ingin diperbarui: ")
                    for emp_id in found_employees:
                        if str(emp_id) == selected_id or self.employees[emp_id]['Nomor Induk Karyawan'] == selected_id:
                            found_employee_id = emp_id
                            break
                    else:
                        print("\n!!!Pilihan tidak valid. Silakan coba lagi!!!")
                        continue
                    break
            else:
                found_employee_id = found_employees[0]

            print("\nData karyawan yang dipilih:\n")
            self.display_employee_details(found_employee_id)

            while True:
                print("\nPilih atribut yang ingin diubah:")
                print("1. Nama")
                print("2. Umur")
                print("3. Departemen")
                print("4. Nomor Induk Karyawan")
                print("5. e-mail")
                print("6. Status Perkawinan")
                print("7. Kembali ke menu utama")

                choice = input("Pilih atribut yang akan diubah (1-7): ")

                if choice == '1':
                    nama = input("Masukkan Nama baru: ")
                    if nama.lower() == 'cancel':
                        return
                    self.employees[found_employee_id]['Nama'] = nama
                elif choice == '2':
                    while True:
                        umur = input("Masukkan Umur baru: ")
                        if umur.lower() == 'cancel':
                            return
                        try:
                            umur = int(umur)
                            break
                        except ValueError:
                            print("Umur harus berupa angka. Silakan coba lagi.")
                    self.employees[found_employee_id]['Umur'] = umur
                elif choice == '3':
                    departemen = input("Masukkan Departemen baru: ")
                    if departemen.lower() == 'cancel':
                        return
                    self.employees[found_employee_id]['Departemen'] = departemen
                elif choice == '4':
                    nomor_induk = input("Masukkan Nomor Induk Karyawan baru: ")
                    if nomor_induk.lower() == 'cancel':
                        return
                    self.employees[found_employee_id]['Nomor Induk Karyawan'] = nomor_induk
                elif choice == '5':
                    email = input("Masukkan e-mail baru: ")
                    if email.lower() == 'cancel':
                        return
                    self.employees[found_employee_id]['e-mail'] = email
                elif choice == '6':
                    status_perkawinan = input("Masukkan Status Perkawinan baru: ")
                    if status_perkawinan.lower() == 'cancel':
                        return
                    self.employees[found_employee_id]['Status Perkawinan'] = status_perkawinan
                elif choice == '7':
                    print("Kembali ke menu utama.")
                    return
                else:
                    print("Pilihan tidak valid. Silakan coba lagi.")
                    continue

                confirmation = input("\nApakah Anda yakin ingin memperbarui data ini? (y/n): ").lower()
                if confirmation == 'y':
                    print(f"Data karyawan dengan ID {found_employee_id} berhasil diperbarui.")
                    self.display_employee_details(found_employee_id)
                else:
                    print("Perubahan dibatalkan.")
        else:
            print("\n!!!Karyawan tidak ditemukan!!!")

# Menghapus karyawan berdasarkan ID, Nomor Induk Karyawan, atau Nama
    def delete_employee(self):
        search_term = input("Masukkan ID, Nomor Induk Karyawan, atau Nama karyawan yang akan dihapus: ")
        found_employees = []

        # Search for employees by ID, Nomor Induk Karyawan, or Nama
        for id, data in self.employees.items():
            if str(id) == search_term or data['Nomor Induk Karyawan'] == search_term or search_term.lower() in data['Nama'].lower():
                found_employees.append(id)

        if found_employees:
            print("\nData karyawan ditemukan:")
            for emp_id in found_employees:
                print(f"ID: {emp_id} | Nama: {self.employees[emp_id]['Nama']} | Nomor Induk Karyawan: {self.employees[emp_id]['Nomor Induk Karyawan']}")

            if len(found_employees) > 1:
                while True:
                    selected_id = input("\nMasukkan ID atau Nomor Induk Karyawan dari karyawan yang ingin dihapus: ")
                    for emp_id in found_employees:
                        if str(emp_id) == selected_id or self.employees[emp_id]['Nomor Induk Karyawan'] == selected_id:
                            found_employee_id = emp_id
                            break
                    else:
                        print("\n!!!Pilihan tidak valid. Silakan coba lagi!!!")
                        continue
                    break
            else:
                found_employee_id = found_employees[0]

            print("\nData karyawan yang dipilih:\n")
            self.display_employee_details(found_employee_id)

            confirmation = input("\nApakah Anda yakin ingin menghapus karyawan ini? (y/n): ").lower()
            if confirmation == 'y':
                del self.employees[found_employee_id]
                print(f"Karyawan dengan ID {found_employee_id} berhasil dihapus.")
            else:
                print("Penghapusan karyawan dibatalkan.")
        else:
            print("\n!!!Karyawan tidak ditemukan!!!")

# Mengurutkan karyawan berdasarkan kriteria tertentu
    def sort_employee(self, key):
        valid_keys = ['nama', 'umur', 'departemen']
        if key.lower() not in valid_keys:
            print("Kriteria pengurutan tidak valid. Silakan coba lagi.")
            return

        key = key.lower()

        sorted_employees = sorted(self.employees.items(), key=lambda x: x[1][key.capitalize()])

        if key == 'nama':
            header = f"\n{'Nama':<25}"
            print(header)
            print("=" * len(header))
            for id, data in sorted_employees:
                row = f"{data['Nama']:<25}"
                print(row)
        elif key == 'umur':
            header = f"\n{'Nama':<25} {'Umur':<5}"
            print(header)
            print("=" * len(header))
            for id, data in sorted_employees:
                row = f"{data['Nama']:<25} {data['Umur']:<5}"
                print(row)
        elif key == 'departemen':
            header = f"\n{'Nama':<25} {'Departemen':<15}"
            print(header)
            print("=" * len(header))
            for id, data in sorted_employees:
                row = f"{data['Nama']:<25} {data['Departemen']:<15}"
                print(row)

# Menampilkan statistik karyawan seperti total karyawan, usia rata-rata, dan distribusi departemen.
    def employee_statistics(self):
        total_employees = len(self.employees)
        total_age = sum(data['Umur'] for data in self.employees.values())
        average_age = total_age / total_employees if total_employees > 0 else 0

        department_distribution = {}
        for data in self.employees.values():
            department = data['Departemen']
            department_distribution[department] = department_distribution.get(department, 0) + 1

        print("\nStatistik Karyawan:")
        print(f"Total Karyawan: {total_employees}")
        print(f"Usia Rata-Rata: {average_age:.2f}")
        print("Distribusi Departemen:")
        for department, count in department_distribution.items():
            print(f"- {department}: {count}")

# Fungsi utama untuk menjalankan program
def main():
    print("=====================================")
    print("     Sistem Manajemen Karyawan")
    print("=====================================\n")
    print("        Silahkan Login untuk melanjutkan!\n")

    employee_manager = EmployeeManagement()
    
    attempts = 0
    max_attempts = 3

    while attempts < max_attempts:
        username = input("Masukkan username: ")
        password = getpass.getpass("Masukkan password: ")

        if employee_manager.login(username, password):
            while True:
                print("\n==================================================================")
                print("||  Selamat Datang di Sistem Manajemen Karyawan PT Tri Pudji!  ||")
                print("==================================================================\n")
                print("\nSilahkan pilih menu yang anda inginkan")
                print("\nMenu:")
                print("1. Tambah Karyawan")
                print("2. Lihat Daftar Karyawan")
                print("3. Perbarui Karyawan")
                print("4. Hapus Karyawan")
                print("5. Urutkan Karyawan")
                print("6. Statistik Karyawan")
                print("7. Keluar")

                choice = input("Pilih menu (1-7): ")

                if choice == '1':
                    employee_manager.add_employee()
                elif choice == '2':
                    print("\nPilih opsi:")
                    print("1. Cari Karyawan")
                    print("2. Daftar Seluruh Karyawan")
                    sub_choice = input("Pilih opsi (1-2): ")
                    if sub_choice == '1':
                        employee_manager.search_employee()
                    elif sub_choice == '2':
                        employee_manager.list_employees()
                    else:
                        print("\n\n !!!Pilihan tidak valid. Silakan coba lagi!!!")
                elif choice == '3':
                    employee_manager.update_employee()
                elif choice == '4':
                    employee_manager.delete_employee()
                elif choice == '5':
                    key = input("Masukkan kriteria pengurutan (Nama/Umur/Departemen): ")
                    employee_manager.sort_employee(key)
                elif choice == '6':
                    employee_manager.employee_statistics()
                elif choice == '7':
                    print("Keluar dari program. Terima kasih atas waktunya. Sampai jumpa lagi!")
                    return
                else:
                    print("\n\n !!!Pilihan tidak valid. Silakan coba lagi!!!")
        else:
            attempts += 1
            print(f"Login gagal. Anda memiliki {max_attempts - attempts} kesempatan lagi.")
    
    print("Anda telah gagal login 3 kali. Program berakhir.")

# Memastikan bahwa fungsi main() hanya dijalankan jika file ini dieksekusi sebagai skrip utama.
if __name__ == "__main__":
    main()
