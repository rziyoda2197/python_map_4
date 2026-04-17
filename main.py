sozlar = ["kitob", "daftar", "ruchka", "kompyuter", "telefon"]
natija = list(map(lambda s: str(len(s)) + " harf", sozlar))
print(natija)

ismlar = ["Ali", "Vali", "Sardor", "Ziyoda", "Madina"]
natija = list(map(len, ismlar))
print(natija)

sozlar = ["salom", "hayr", "python", "map", "lambda"]
natija = list(map(lambda s: len(s)**2, sozlar))
print(natija)
