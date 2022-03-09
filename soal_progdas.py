def garis():
    print("-------------------------------------")

def sort_asc(array):
    n = len(array)
    for i in range(n):
        for j in range(n-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array

def sort_desc(array):
    n = len(array)
    for i in range(n):
        for j in range(n-i-1):
            if array[j] < array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array

def rata_rata(angka):
    return sum(angka)/len(angka)

garis()
print("Masukan Nama dan Nilai kalian")
nama = input("Nama : ")
nilai_1 = int(input("Nilai 1 : "))
nilai_2 = int(input("Nilai 2 : "))
nilai_3 = int(input("Nilai 3 : "))
nilai_4 = int(input("Nilai 4 : "))
nilai_5 = int(input("Nilai 5 : "))
nilai_6 = int(input("Nilai 6 : "))
nilai_7 = int(input("Nilai 7 : "))
nilai_8 = int(input("Nilai 8 : "))
nilai_9 = int(input("Nilai 9 : "))
nilai_10 = int(input("Nilai 10 : "))
nama_lengkap = [nama]
angka = [nilai_1, nilai_2, nilai_3, nilai_4,  nilai_5,  nilai_6,  nilai_7,  nilai_8,  nilai_9,  nilai_10]
garis()
print()

print("------Hasil Akhir------")
print("Urutan Angka Ascending : ",(sort_asc(angka)))
print("Urutan Angka Descending : ",(sort_desc(angka)))

print("Nama anda adalah : ",(nama))
print("Angka Terbesar : ",max(angka))
print("Angka Terkecil : ",min(angka))
print("Rata Ratanya : ",round(rata_rata(angka),2))
