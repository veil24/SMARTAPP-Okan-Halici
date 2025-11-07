import os, requests

try:
    r = requests.get("https://api.open-meteo.com/v1/forecast?latitude=52.09&longitude=5.12&current=temperature_2m")
    temp = r.json()["current"]["temperature_2m"]
    print(f"\nHuidige temperatuur in Utrecht: {temp} graden Celsius\n")
except:
    print("\n(Weerdata kon niet worden opgehaald)\n")



path = r"C:\Users\Okan H\Desktop\Python files\SMARTAPP OKAN"

while True:
    print("\nKies een programma:")
    print("1. SmartApp Controller")
    print("2. SmartApp")
    print("3. Stoppen")

    keuze = input("Maak een keuze (1-3): ")

    if keuze == "1":
        os.system(f'python "{path}\\SMARTAPP CONTROLLER.py"')
    elif keuze == "2":
        os.system(f'python "{path}\\SMARTAPP1.PY"')
    elif keuze == "3":
        print("Tot ziens!")
        break
    else:
        print("Ongeldige keuze, probeer opnieuw.")