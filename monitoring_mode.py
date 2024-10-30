import psutil  # Importerar psutil-modulen för att få information om systemets CPU-användning.
from alarm import alarms  # Importerar listan 'alarms' från 'alarm'-modulen för att hämta aktiva larm.
from my_logging import Logger  # Importerar Logger-klassen från my_logging för att logga händelser.

logger = Logger()  # Skapar en instans av Logger för att logga händelser.

def start_monitoring_mode():
    # Funktion för att starta övervakningsläge som kontinuerligt övervakar CPU-användningen.
    while True:  # Startar en oändlig loop för att kontinuerligt övervaka CPU-användningen.
        cpu_usage = psutil.cpu_percent(interval=1)  # Hämtar CPU-användning som procent, med en fördröjning på 1 sekund.

        # Kontrollerar om några larm är konfigurerade.
        if alarms:
            for alarm in alarms:  # Loopar igenom alla konfigurerade larm.
                # Kontrollerar om larmet gäller CPU och om CPU-användningen överstiger larmets gräns.
                if "CPU" in alarm and int(alarm.split()[2].replace("%", "")) < cpu_usage:
                    logger.log_event(f"VARNING, LARM AKTIVERAT: CPU ANVÄNDNING ÖVERSTIGER {cpu_usage}%")  # Loggar varningen.

        # Väntar på användarens input för att avsluta övervakningsläget.
        input("Övervakning är aktiv, tryck på valfri tangent för att återgå till menyn.")  # Visar meddelande till användaren.
        break  # Avslutar loopen och återgår till huvudmenyn.