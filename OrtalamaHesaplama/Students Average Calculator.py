# Ortalama hesaplayıcı:
# Program showing students' average and passing grades according to their midterm and final grades.
# Öğrencilerin Vize ve final notlarına göre ortalamasını ve geçip kaldığını gösteren program.
vize: int = 0
final: int = 0
sonuc: int = 0
ort: int = 0
isim = ""
i: int = 0

ogrenciVeNot = {}
ogrenciListesi = ["akif", "emre", "aykut"]
sayac = 0
# dönğü
for isim in ogrenciListesi:

    vize = int(input("Vize puanınızı giriniz : "))
    final = int(input("Final puanınızı giriniz : "))

    while vize > 100 or final > 100:
        print(ogrenciListesi[sayac], "Girdiğiniz puan geçersizdir! ")
        vize = int(input("Vize puanınızı giriniz : "))
        final = int(input("Final puanınızı giriniz : "))

    # ortalama hesaplama

    ort: int = (vize * 0.4) + (final * 0.6)
    print(ort)

    if final >= 50:
        if ort >= 50 and ort < 70:
            print(ogrenciListesi[sayac], "CC ile geçtiniz. ")
            a = "CC"
        elif ort >= 70 and ort < 85:
            print(ogrenciListesi[sayac], "BB ile geçtiniz. ")
            a = "BB"
        elif ort >= 85 and ort <= 100:
            print(ogrenciListesi[sayac], "AA ile geçtiniz. ")
            a = "AA"
        else:
            print(ogrenciListesi[sayac], "FF ile Kaldınız")
            a = "FF"
    else:
        print(ogrenciListesi[sayac], "Final notunuz 50'nin altında , Kaldınız.")
        a = "FF"
    ogrenciVeNot.update({ogrenciListesi[sayac]: [ort, a]})
    sayac += 1
print(ogrenciVeNot)
