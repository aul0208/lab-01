import json

class Jsonku:
    def __init__(self, file):
        self.file = file

    def baca(self):
        try:
            with open(self.file, 'r') as file:
                data = json.load(file)
            return data
        except FileNotFoundError:
            print("File tidak ditemukan.")
            return None
        except json.JSONDecodeError:
            print("File JSON tidak valid.")
            return None
        
    def tulis(self, data):
        with open(self.file, 'w') as file:
            json.dump(data, file, indent=4)
        print("Data berhasil ditulis ke dalam file.")
    
    def update(self, key, value):
        data = self.baca()
        if data:
            data[key] = value
            self.tulis(data)
            print("Data berhasil diupdate.")
        else:
            print("Tidak dapat menghapus data atau data tidak ditemukan.")

    def delete(self, key):
        data = self.baca()
        if data and key in data:
            del data[key]
            self.tulis(data)
            print("Data berhasil dihapus.")
        else:
            print("Tidak dapat menghapus data atau data tidak ditemukan.")

if __name__ == "__main__":
     file = "data.json"
     jsonku = Jsonku(file)

     # Demonstrasi fungsi-fungsi dari kelas jsonku
     jsonku.tulis({"judul" : "Aku","Pengarang":"M.syaifudin","tahun_terbit": 2004, "hobi": "membaca"})

     data = jsonku.baca()
     print("Data sebelum update:", data)

     jsonku.update("tahun_terbit", 2002)
     data = jsonku.baca()
     print("Data setelah penghapusan hobi:", data)

     jsonku.delete("hobi")
     data = jsonku.baca()
     print("Data setelah penghapusan hobi:", data)


