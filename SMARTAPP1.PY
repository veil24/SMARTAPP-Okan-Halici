"""
Voer per dag in:
Temp Celsius
Windsnelheid m/s
Luchtvochtigheid 0-100%
- Geen lege waarde
"""

#Alle gevraagde functies

def bereken_gemiddelde():
    with open("dagdata.txt", "r") as file:
        regels = file.readlines()
    totaal = 0.0
    count = 0
    for regel in regels:
        delen = regel.strip().split(";")
        temp = float(delen[1])
        totaal += temp
        count += 1 
    return totaal / count

def fahrenheit (graden_celsius):
    waarde = 32 + graden_celsius * 1.8
    return waarde


def gevoelstemperatuur(temp_celcius, windsnelheid, luchtvochtigheid):
    gevoelstemperatuur = temp_celcius - luchtvochtigheid / 100 * windsnelheid
    return gevoelstemperatuur

def data_opslaan(resultaat):
    dagnr, temp, wind, vocht = resultaat
    regel_nieuw = f"{dagnr};{temp};{wind};{vocht}\n"

    file = open("dagdata.txt", "r")
    regels = file.readlines()
    file.close()
    #Add gevonden zodat als ik dubbele data heb dat ik het niet 2 keer append
    gevonden = False
    for regel in regels:
        if regel.split(";")[0] == str(dagnr):
            
            melding = input("Je hebt al data opgeslagen voor deze dag wil je deze vervangen?(Y/N): ").strip()
            gevonden = True
            if melding.upper() == "Y": 
                regels.remove(regel)
                regels.append(regel_nieuw)
                print("Data vervangen")
            else:
                print("Data ongewijzigd")
    #Dus als niks is toegevoegd dan:
    if gevonden == False:
        regels.append(regel_nieuw)
        print("Nieuwe dagdata toegevoegd.")

       # Schrijf de aangepaste inhoud (alle regels) terug naar het bestand

    file = open("dagdata.txt", "w")
    file.writelines(regels)
    file.close()

def weerrapport(temp_celcius, windsnelheid, luchtvochtigheid):
    gevoel = gevoelstemperatuur(temp_celcius, windsnelheid, luchtvochtigheid)
    if gevoel < 0 and windsnelheid > 10:
        return "Het is heel koud en het stormt! Verwarming helemaal aan!"
    if gevoel < 0 and windsnelheid <= 10:
        return "Het is behoorlijk koud! Verwarming aan op de benedenverdieping!"
    if 0 <= gevoel < 10 and windsnelheid > 12:
        return "Het is best koud en het waait; verwarming aan en roosters dicht!"
    if 0 <= gevoel < 10 and windsnelheid <= 12:
        return "Het is een beetje koud, elektrische kachel op de benedenverdieping aan!"
    if 10 <= gevoel < 22:
        return "Heerlijk weer, niet te koud of te warm."
    else:
        return "Warm! Airco aan!"
   
    #Checks

    
while True: 
    dag = input("Voer een dag in om te starten (1-7), Als dit je eerste dag is begin bij 1: ").strip()
    
    #Error check of het een int is
    try:   
        dag = int(dag) 
    except ValueError:
        print("Geen geldige nummer, probeer opnieuw:\n")
        continue

    #Maximaal 7 dagen check
    if dag < 1 or dag > 7:
        print("Ons programma heeft een opslaglimiet van 7 dagen, begin bij dag 1 aub")
        continue
    else:
        break
        



def metingen(dag):
    

    #Print request
    print(f"\nVoer alstublieft voor dag {(dag)} in: \n\n")
    
    #Userinput waarden totdat deze goed zijn ingevoerd
    while True:
        celsius = input("Het temperatuur in Celsius:  ").strip()
        windsnelheid = input("De windsnelheid in meters per secode: ").strip()
        luchtvochtigheid = input("Luchtvochtigheid (0 - 100%) : ").strip()

    # Probeer de waardes in floats om te zetten, lukt dit allemaal goed break uit de loop: 
        try:
            celsius = float(celsius)
            windsnelheid = float(windsnelheid)
            luchtvochtigheid = float(luchtvochtigheid)

            #luchtvochtigheid moet in procenten dus 0-100 en windsnelheid kan niet negatief zijn: 
            if 0 <= luchtvochtigheid <= 100 and windsnelheid >= 0:
                break
            else: 
                print("Voer voor luchtvochtigheid een percentage tussen 0-100 alstublieft.\n")
        #Value error = als iemand een str invoer ook "" (leeg) geeft het aan:
        except ValueError: 
            print(
f"""Je waardes kloppen niet, gebruik voer een geldig nummer in en gebruik '.' voor decimalen.
probeer opnieuw:       
""")
            
    #lijst voor om data makkelijk op te slaan
    resultaat = [
dag, celsius, windsnelheid, luchtvochtigheid
    ]


    return resultaat


resultaat = metingen(dag)
data_opslaan(resultaat)
#uitvoer functie + 
def rapport():
    dagnummer = resultaat[0]
    temperatuur = resultaat[1]
    windsnelheid = resultaat[2]
    luchtvochtigheid = resultaat[3]
    gemiddelde = bereken_gemiddelde()
    fahren = fahrenheit(temperatuur)
    toestand = weerrapport(temperatuur, windsnelheid, luchtvochtigheid)
    return(f"""
Jouw rapport voor dag {dagnummer}:
Temperatuur: {temperatuur} Celsius / {fahren} Fahrenheit
Windsnelheid: {windsnelheid} m/s
Luchtvochtigheid: {luchtvochtigheid} %  
Toestand: {toestand}  
Gemiddelde temp tot nu toe: {round(gemiddelde,1)}     
________________________________________________________
________________________________________________________
""")


print (rapport())














        
    

    
    


