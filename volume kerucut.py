class kerucut:
    def __init__(self, jari_jari, tinggi):
        self.jari_jari = jari_jari
        self.tinggi = tinggi
    
    def menghitung(self):
        return 1/3 * 3.14 * self.jari_jari * self.jari_jari * self.tinggi

    def menampilkan(self):
        print("volume kerucut : ", self.menghitung())

print("===== volume kerucut ====")
jari_jari = input("Jari-jari : ")
jari_jari = input("Jari-jari :")
tinggi = input("Tinggi   :")
volume = kerucut(int(jari_jari), int(tinggi))
volume.menampilkan()