ogrenci_listesi = []

a = input("Öğrenci isimlerini girin (isimleri virgülle ayırın): ")

isimler = a.split(",")
ogrenci_listesi.extend(isimler)

print("Öğrenci Listesi:", ogrenci_listesi)
