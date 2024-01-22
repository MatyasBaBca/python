def zadej_liche_cislo():
    while True:
        try:
            X = int(input("Zadej liché přirozené číslo X: "))
            if X > 0 and X % 2 != 0:
                return X
            else:
                print("Zadáno číslo není liché přirozené. Zkus to znovu.")
        except ValueError:
            print("Neplatný vstup. Zkus to znovu.")

def vypis_radky_cisel(X):
    for i in range(1, 2*X, 2):
        print(" ".join(map(str, range(1, i + 1))))

if __name__ == "__main__":
    X = zadej_liche_cislo()
    vypis_radky_cisel(X)
