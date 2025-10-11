"""
Voer per dag in:
Temp Celsius
Windsnelheid m/s
Luchtvochtigheid 0-100%
- Geen lege waarde
"""
start = 0

def fahrenheit (g_celsius):
    waarde = 32 + g_celsius * 1.8
    return waarde


while True: 
    dag = input("Voer een dag in om te starten 1-7: ").strip()
     
    #Error check of het een int is
    try: 
        dag = int(dag)
    except ValueError:
        print("Geen geldige nummer, probeer opnieuw:\n")

    #Maximaal 7 dagen check
    if dag < 0 or dag > 7:
        print("Ons programma heeft een opslaglimiet van 7 dagen per gebruiker, begin bij dag 1 aub")
    else:
        break
        



def metingen(dag):
    
    


    #Print request
    print(f"\nVoer alstublieft voor dag {(dag)} in: \n\n")
    
    #Userinput waarden totdat deze goed zijn ingevoerd
    while True:
        celsius = input("Het temperatuur in Celsius:  ").strip()
        windsnelheid = input("De windsnelheid in meters per secode: ").strip()
        luchtvochtigheid = input("Luchtvochtigheid 0 - 100% : ").strip()

    # Probeer de waardes in floats om te zetten, lukt dit allemaal goed break uit de loop: 
        try:
            celsius = float(celsius)
            windsnelheid = float(windsnelheid)
            luchtvochtigheid = float(luchtvochtigheid)

            #luchtvochtigheid moet in procenten dus 0-100: 
            if 0 <= luchtvochtigheid <= 100:
                break
            else: 
                print("Voer voor luchtvochtigheid een percentage tussen 0-100 alstublieft.\n")
        #Value error = als iemand een str invoer ookt "" (leeg) geeft het aan:
        except ValueError: 
            print(
f"""Je waardes kloppen niet, gebruik voer een geldig nummer in en gebruik '.' voor decimalen.
probeer opnieuw:       
""")
    #Dict voor data 
    resultaat = {

    #nested dict, omdat dag altijd 3 waardes gaat hebben die kunnen verschillen
    #Zo kan ik straks dag makkelijk in een txt omzetten

    f"dag {dag}":
    {"celcius": celsius,
    "windsnelheid": windsnelheid,
    "luchtvochtigheid": luchtvochtigheid}
   
    }


    return resultaat
    

print(metingen(dag))

        
        
    

    
    


