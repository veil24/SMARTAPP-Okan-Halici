def aantal_dagen(inputFile):
    file = open(inputFile, "r") 
    dagen = len(file.readlines()) - 1 #Want regel 1 zijn kolomnamen
    file.close()
  
    
    return dagen

def auto_bereken(inputFile, outputFile):
    file = open(inputFile, "r")
    lijnen = file.readlines()
    file.close()
    geldige_lijnen = lijnen[1:]
    output = []
    for lijn in geldige_lijnen:
        lijn = lijn.strip()
        datum, personen, setpoint, buiten_temp, neerslag = lijn.split(" ") 
        personen = float(personen)
        setpoint = float(setpoint)
        buiten_temp = float(buiten_temp)
        neerslag = float(neerslag)
        verschil = setpoint - buiten_temp

        if verschil >= 20:
            cv_ketel = 100
        elif verschil >= 10:
            cv_ketel = 50
        else:
            cv_ketel = 0
        
        stand = personen + 1
        if stand > 4:
            stand = 4
        
        if neerslag < 3: 
            bewatering = True
        else: 
            bewatering = False
        
        output_regel = f"{datum};{cv_ketel};{stand};{bewatering}"
        output.append(output_regel)

    file2 = open(outputFile, "w")
    for regel in output:
        file2.write(f"{regel}\n")
    file2.close()  
    



def overwrite_settings(outputFile):
    file = open(outputFile, "r")
    regels = file.readlines()
    file.close()

    
    regelnr = 1  
    print("Beschikbare data en instellingen:")
    for regel in regels:
        print(f"{regelnr}. {regel.strip()}")
        regelnr += 1

    datum_keuze = input("Voer de nummer van de datum in die je wilt overschrijven: ").strip()
    try:
        datum_keuze = int(datum_keuze)
    except ValueError:
        print("Fout: ongeldige invoer, geen geldig nummer.")
        return -3
    datum_keuze = int(datum_keuze)

    if datum_keuze < 1 or datum_keuze > len(regels):
        print("Fout: een datum voor deze nummerkeuze bestaat niet")
        return -1

    index = datum_keuze - 1 #want txt regels starten met 0

    datum, cv_ketel, stand, bewatering = regels[index].strip().split(";")
    print(f"""
Huidige waarden voor {datum}:

CV-ketel= {cv_ketel},
Ventilatiestand= {stand},
Bewatering= {bewatering}
""")

    print(f""" 
Welk systeem wil je overschrijven?
1: CV-ketel (0-100%)
2: Ventilatie (1-4)
3: Bewatering (Aan (1) / Uit (0))
""")
    verandering = input("Voer hier je keuze in (1-3): ").strip()

    if verandering not in ("1", "2", "3"):
        print("Ongeldige keuze.")
        return -3
    
    nieuwe_waarde = input("Voer de nieuwe waarde in: ").strip()


    if verandering == "1":
        try:
            nieuwe_waarde = int(nieuwe_waarde)
        except ValueError:
            print("Error: ongeldige waarde voor CV-ketel.")
            return -3

        if nieuwe_waarde < 0 or nieuwe_waarde > 100:
            print("De waarde moet tussen de 0 en 100 liggen voor de CV Ketel")
            return -3
        
        cv_ketel = str(nieuwe_waarde)

    elif verandering == "2":
        try:
            nieuwe_waarde = int(nieuwe_waarde)
        except ValueError:
            print("Error: ongeldige waarde voor Ventilatiestand.")
            return -3

        if nieuwe_waarde < 0 or nieuwe_waarde > 4:
            print("De waarde moet tussen de 0 en 4 liggen voor de Ventilatiestand.")
            return -3

        stand = str(nieuwe_waarde)

    else: 
        if nieuwe_waarde not in ("0", "1"):
            print("Error: ongeldige waarde voor Bewatering, voer een 1 voor Aan in en een 0 voor Uit")
            return -3

        if nieuwe_waarde == "1":
            bewatering = True
        else:
            bewatering = False

    #De juiste regel opnieuw structureren
    regels[index] = f"{datum};{cv_ketel};{stand};{bewatering}\n"
  

    file = open(outputFile, "w")
    file.writelines(regels)
    file.close()

    print("Succesvol data overgeschreven")
    return 0
    


def smart_app_controller(inputFile, outputFile):
    while True:
        print("""
Welkom bij de Smart App Menu.
Kies een van de volgende opties:
1: Aantal dagen weergeven
2: Automatisch alle actuatoren berekenen en naar uitvoerbestand schrijven
3: Waarde overschrijven in het uitvoerbestand
4: Stoppen
""")
        keuze = input("Voer je keuze in (1-4): ").strip()

        if keuze == "1":
            aantal = aantal_dagen(inputFile)
            print(f"Aantal dagen in bestand: {aantal}")

        elif keuze == "2":
            auto_bereken(inputFile, outputFile)
            print(f"Berekening afgerond en resultaten opgeslagen in {outputFile}")

        elif keuze == "3":
            result = overwrite_settings(outputFile)
            if result == 0:
                print("Overschrijven gelukt.")
            elif result == -1:
                print("Datum niet gevonden.")
            elif result == -3:
                print("Ongeldige invoer.")
            # je kunt andere retour‐codes nog interpreteren

        elif keuze == "4":
            print("Programma wordt gestopt. Tot ziens!")
            break

        else:
            print("Ongeldige keuze, probeer opnieuw.")

smart_app_controller("input.txt", "output.txt")
