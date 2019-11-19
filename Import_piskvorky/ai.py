def tah_hrace(herni_pole):
    while True:
        cislo_policka = input("Zadej cislo policka 0-19: ")
        cislo_policka = int(cislo_policka)
        if cislo_policka < 0 or cislo_policka > 19:
            print("Prosim zadej cislo v rozmezi 0-19.")
        elif herni_pole[cislo_policka] != "-":
            print("Policko {} je obsazene, vyber prosim jine.".format(cislo_policka))
        else:
            return tah(herni_pole, cislo_policka, "x")