import tkinter as tk  # Importerar tkinter-modulen som 'tk' för att skapa GUI-komponenter.
from monitoring import start_monitoring, list_active_monitoring  # Importerar funktioner för att starta och lista övervakning från 'monitoring'.
from alarm import remove_alarm, alarm_menu, show_alarms  # Importerar larmfunktioner från 'alarm' för att hantera, visa och skapa larm.
from alarm_storage import save_alarms, load_alarms  # Importerar funktioner för att spara och ladda larm från 'alarm_storage'.
from monitoring_mode import start_monitoring_mode  # Importerar funktionen för att starta övervakningsläge från 'monitoring_mode'.

def main_menu(root):
    # Funktion som skapar huvudmenyn i applikationen.
    tk.Label(root, text="Välj ett alternativ:").pack()  # Skapar en etikett med instruktioner för användaren.

    # Skapar knappar som användaren kan klicka på för att utföra olika åtgärder.
    tk.Button(root, text="Starta övervakning", command=start_monitoring).pack()  # Startar övervakning.
    tk.Button(root, text="Lista aktiv övervakning", command=list_active_monitoring).pack()  # Listar pågående övervakning.
    tk.Button(root, text="Skapa larm", command=lambda: alarm_menu(root)).pack()  # Öppnar menyn för att skapa larm.
    tk.Button(root, text="Visa larm", command=show_alarms).pack()  # Visar en lista över konfigurerade larm.
    tk.Button(root, text="Ta bort larm", command=remove_alarm).pack()  # Låter användaren ta bort ett larm.
    tk.Button(root, text="Spara larm", command=save_alarms).pack()  # Sparar alla larm till en fil.
    tk.Button(root, text="Ladda larm", command=load_alarms).pack()  # Laddar larm från en fil.
    
    # Lägg till en avslutningsknapp under knappen för att ladda larm
    tk.Button(root, text="Avsluta", command=root.quit).pack()  # Knapp för att avsluta programmet