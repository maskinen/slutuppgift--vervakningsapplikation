import json  # Importerar json-modulen för att arbeta med JSON-data.
import tkinter as tk  # Importerar tkinter-modulen som 'tk' för att skapa grafiska användargränssnitt (GUI).
from tkinter import messagebox  # Importerar 'messagebox' från tkinter för att visa popup-meddelanden.
from my_logging import Logger  # Importerar en loggningsklass 'Logger' från en extern fil 'my_logging'.

logger = Logger()  # Skapar en instans av Logger för att logga händelser.
alarms = []  # Skapar en lista för att lagra konfigurerade larm.

def save_alarms():
    """Sparar larm till en JSON-fil."""
    try:
        with open('alarms.json', 'w') as file:  # Öppnar (eller skapar) en JSON-fil för skrivning.
            json.dump(alarms, file)  # Skriver larm-listan till filen i JSON-format.
        logger.log_event("Larm sparade till alarms.json")  # Loggar att larm har sparats.
    except Exception as e:  # Fångar alla undantag som kan uppstå.
        logger.log_event(f"Fel vid sparande av larm: {e}")  # Loggar felmeddelande.
        print(f"Fel vid sparande av larm: {e}")  # Skriver ut felmeddelande i konsolen.

def load_alarms():
    """Laddar larm från JSON-fil om de finns."""
    global alarms  # Anger att 'alarms' är en global variabel.
    try:
        with open('alarms.json', 'r') as file:  # Öppnar JSON-filen för läsning.
            alarms = json.load(file)  # Laddar larm-listan från filen.
        logger.log_event("Tidigare larm laddade från alarms.json")  # Loggar att larm har laddats.
    except FileNotFoundError:  # Fångar om filen inte hittas.
        logger.log_event("Ingen tidigare larmfil funnen.")  # Loggar att ingen fil hittades.
    except Exception as e:  # Fångar alla andra undantag.
        logger.log_event(f"Fel vid laddning av larm: {e}")  # Loggar felmeddelande.

def alarm_menu(parent):
    """Skapar en meny för att ställa in larm."""
    alarm_window = tk.Toplevel(parent)  # Skapar ett nytt fönster för larmmenyn.
    alarm_window.title("Skapa larm")  # Sätter titeln på larmfönstret.

    tk.Label(alarm_window, text="Välj ett område att ställa larm för:").pack()  # Skapar en etikett med instruktioner.
    # Skapar knappar för olika larmtyper och kopplar dem till funktionen 'set_alarm'.
    tk.Button(alarm_window, text="CPU användning", command=lambda: set_alarm("CPU")).pack()  
    tk.Button(alarm_window, text="Minnesanvändning", command=lambda: set_alarm("Minnesanvändning")).pack()
    tk.Button(alarm_window, text="Diskanvändning", command=lambda: set_alarm("Diskanvändning")).pack()
    tk.Button(alarm_window, text="Tillbaka till huvudmenyn", command=alarm_window.destroy).pack()  # Knapp för att stänga larmfönstret.

def set_alarm(alarm_type):
    """Funktionen för att ställa in ett larm av en viss typ."""
    def confirm_alarm():
        """Bekräftar och sparar det inställda larmet."""
        try:
            level = int(alarm_level.get())  # Hämtar och konverterar inmatat värde till heltal.
            if 1 <= level <= 100:  # Kontrollerar om värdet ligger inom det tillåtna intervallet.
                alarms.append(f"{alarm_type} larm {level}%")  # Lägger till det nya larmet i larm-listan.
                messagebox.showinfo("Larm satt", f"Larm för {alarm_type} satt till {level}%!")  # Visar bekräftelse för användaren.
                save_alarms()  # Sparar larm till JSON-fil.
                alarm_window.destroy()  # Stänger larmfönstret.
                logger.log_event(f"Larm konfigurerat: {alarm_type} {level}%")  # Loggar att larm har konfigurerats.
            else:
                messagebox.showerror("Felaktigt värde", "Nivån måste vara mellan 1 och 100.")  # Visar felmeddelande om värdet är ogiltigt.
        except ValueError:  # Fångar om inmatningen inte kan konverteras till heltal.
            messagebox.showerror("Felaktigt värde", "Mata in en giltig siffra.")  # Visar felmeddelande för ogiltig inmatning.

    alarm_window = tk.Toplevel()  # Skapar ett nytt fönster för att ställa in larm.
    alarm_window.title(f"Ställ in {alarm_type} larm")  # Sätter titeln för larmfönstret.

    tk.Label(alarm_window, text=f"Ställ in nivå för {alarm_type} mellan 1-100%:").pack()  # Skapar en etikett med instruktioner för inmatning.
    alarm_level = tk.Entry(alarm_window)  # Skapar ett inmatningsfält för larmnivån.
    alarm_level.pack()  # Lägger till inmatningsfältet i fönstret.

    tk.Button(alarm_window, text="Bekräfta", command=confirm_alarm).pack()  # Knapp för att bekräfta larminställning.
    tk.Button(alarm_window, text="Avbryt", command=alarm_window.destroy).pack()  # Knapp för att stänga larmfönstret.

def show_alarms():
    """Visar alla konfigurerade larm i en popup-meddelande."""
    if alarms:  # Kontrollerar om det finns några larm i listan.
        alarms_str = "\n".join(sorted(alarms))  # Sorterar och formaterar larmen som en sträng.
        messagebox.showinfo("Visa larm", f"Konfigurerade larm:\n{alarms_str}")  # Visar larmen i en popup.
    else:
        messagebox.showinfo("Visa larm", "Inga larm konfigurerade ännu.")  # Visar meddelande om inga larm finns.

def remove_alarm():
    """Öppnar en meny för att ta bort ett konfigurerat larm."""
    if not alarms:  # Kontrollerar om det inte finns några larm.
        messagebox.showinfo("Ta bort larm", "Inga larm att ta bort.")  # Meddelar användaren om att inga larm finns.
        return  # Avslutar funktionen om inga larm finns.

    alarm_window = tk.Toplevel()  # Skapar ett nytt fönster för att ta bort larm.
    alarm_window.title("Ta bort larm")  # Sätter titeln på larmfönstret.

    tk.Label(alarm_window, text="Välj ett konfigurerat larm att ta bort:").pack()  # Skapar en etikett med instruktioner.
    # Skapar knappar för varje konfigurerat larm som användaren kan ta bort.
    for idx, alarm in enumerate(alarms, 1):  # Itererar över larm-listan med index.
        tk.Button(alarm_window, text=alarm, command=lambda i=idx: confirm_remove_alarm(i, alarm_window)).pack()

    tk.Button(alarm_window, text="Avbryt", command=alarm_window.destroy).pack()  # Knapp för att stänga larmfönstret.

def confirm_remove_alarm(index, window):
    """Bekräftar borttagning av ett larm och uppdaterar larmlistan."""
    removed_alarm = alarms.pop(index - 1)  # Tar bort larmet med angivet index från listan.
    save_alarms()  # Sparar ändrad larmlista till JSON-fil efter borttagning.
    messagebox.showinfo("Larm borttaget", f"{removed_alarm} borttaget.")  # Meddelar användaren att larmet har tagits bort.
    logger.log_event(f"Larm borttaget: {removed_alarm}")  # Loggar borttagningen av larmet.
    window.destroy()  # Stänger fönstret.

def check_cpu_alarm(current_cpu_usage):
    """Kontrollerar om aktuell CPU-användning överstiger något aktivt larm."""
    active_alarms = [alarm for alarm in alarms if 'CPU' in alarm]  # Filtrerar larm-listan för att få aktiva CPU-larm.
    if active_alarms:  # Kontrollerar om det finns några aktiva CPU-larm.
        max_alarm = max([int(alarm.split()[-1].replace('%', '')) for alarm in active_alarms])  # Hittar det högsta larmet i procent.
        if current_cpu_usage >= max_alarm:  # Kontrollerar om aktuell CPU-användning överstiger larmnivån.
            logger.log_event(f"VARNING, LARM AKTIVERAT, CPU ANVÄNDNING {current_cpu_usage}% ÖVERSTIGER {max_alarm}%")  # Loggar att larmet har aktiverats.