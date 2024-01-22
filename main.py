import re

def kontrola_hesla(heslo):
    # Kontrola délky hesla
    if 6 <= len(heslo) <= 16:
        # Kontrola malého písmena
        if re.search("[a-z]", heslo):
            # Kontrola velkého písmena
            if re.search("[A-Z]", heslo):
                # Kontrola číslice
                if re.search("[0-9]", heslo):
                    # Kontrola speciálního znaku
                    if re.search("[$#@]", heslo):
                        print("Heslo je platné.")
                        return True
                    else:
                        print("Heslo musí obsahovat nejméně jeden ze znaků: $, #, @.")
                else:
                    print("Heslo musí obsahovat nejméně jednu číslici.")
            else:
                print("Heslo musí obsahovat nejméně jedno velké písmeno.")
        else:
            print("Heslo musí obsahovat nejméně jedno malé písmeno.")
    else:
        print("Heslo musí mít délku mezi 6 a 16 znaky.")

    return False

heslo = input("Zadejte heslo: ")
kontrola_hesla(heslo)
