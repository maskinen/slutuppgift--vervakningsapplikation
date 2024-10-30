import json  # Importerar json-modulen för att arbeta med JSON-data.
from my_logging import Logger  # Importerar en loggningsklass 'Logger' från en extern fil 'my_logging'.
import tkinter as tk  # Importerar tkinter-modulen som 'tk' för att skapa grafiska användargränssnitt (GUI).
from tkinter import messagebox  # Importerar messagebox från tkinter för att visa meddelanderutor.

logger = Logger()  # Skapar en instans av Logger för att logga händelser.
alarms = []  # Skapar en global variabel för att lagra konfigurerade larm.

def save_alarms():
    """Sparar larm till en JSON-fil."""
    try:
        if not alarms:  # Kontrollerar om larm-listan är tom.
            print("Inga larm att spara.")  # Skriver ut meddelande för att indikera att inga larm finns.
        else:
            with open('alarms.json', 'w') as file:  # Öppnar (eller skapar) en JSON-fil för skrivning.
                json.dump(alarms, file)  # Skriver larm-listan till filen i JSON-format.
            logger.log_event("Larm sparade till alarms.json")  # Loggar händelsen att larmen sparades.
            print("Larm sparade till alarms.json")  # Skriver ut bekräftelse för felsökning.
    except Exception as e:  # Fångar alla undantag som kan uppstå.
        logger.log_event(f"Fel vid sparande av larm: {e}")  # Loggar felmeddelande.
        print(f"Fel vid sparande av larm: {e}")  # Skriver ut felmeddelande i konsolen.

def load_alarms():
    """Laddar larm från JSON-fil och visar i en messagebox om de finns."""
    global alarms  # Anger att 'alarms' är en global variabel.
    try:
        with open('alarms.json', 'r') as file:  # Öppnar JSON-filen för läsning.
            alarms = json.load(file)  # Laddar larm-listan från filen.
        
        if alarms:  # Kontrollerar om det finns några larm i listan.
            # Skapa en sträng med alla sparade larm och visa dem i en messagebox.
            alarms_text = "\n".join([str(alarm) for alarm in alarms])  # Formaterar larmen som en sträng.
            messagebox.showinfo("Sparade Larm", f"Laddade larm:\n{alarms_text}")  # Visar larmen i en popup.
            logger.log_event("Tidigare larm laddade från alarms.json")  # Loggar att larm har laddats.
        else:
            messagebox.showinfo("Sparade Larm", "Inga sparade larm hittades.")  # Meddelar användaren om inga larm finns.
            print("Inga larm hittades i filen.")  # Skriver ut meddelande för felsökning.
    except FileNotFoundError:  # Fångar om filen inte hittas.
        messagebox.showinfo("Fel", "Ingen tidigare larmfil funnen.")  # Meddelar användaren om att filen inte hittades.
        logger.log_event("Ingen tidigare larmfil funnen.")  # Loggar att ingen fil hittades.
    except Exception as e:  # Fångar alla andra undantag.
        logger.log_event(f"Fel vid laddning av larm: {e}")  # Loggar felmeddelande.
        print(f"Fel vid laddning av larm: {e}")  # Skriver ut felmeddelande i konsolen.
