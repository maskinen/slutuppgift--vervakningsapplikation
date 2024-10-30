import logging  # Importerar logging-modulen för att hantera loggning av händelser.
import os  # Importerar os-modulen för att hantera fil- och katalogrelaterade operationer.
from datetime import datetime  # Importerar datetime för att skapa tidsstämplar i loggfilnamnet.

class Logger:
    # Definierar klassen Logger som hanterar skapande och loggning av händelser till en loggfil.

    def __init__(self):
        # Initialiserar Logger-instansen och skapar en loggfil.
        self.__log_filename = self.setup_logging()  # Kallar på funktionen setup_logging för att skapa loggfilen.

    def setup_logging(self):
        """Skapar en dynamisk loggfil i mappen 'loggfiler' baserat på datum och tid."""
        log_dir = "loggfiler"  # Definierar katalogen där loggfilerna ska sparas.

        # Skapar mappen "loggfiler" om den inte redan finns.
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)  # Skapar loggfiler-mappen om den saknas.

        # Skapar ett loggfilnamn baserat på aktuell tid och datum.
        log_filename = os.path.join(log_dir, datetime.now().strftime('%Y-%m-%d_%H-%M-%S_logfile.log'))
        try:
            # Konfigurerar loggningen för att skriva till den nyskapade loggfilen.
            logging.basicConfig(
                filename=log_filename,  # Anger loggfilens väg.
                level=logging.INFO,  # Sätter loggnivån till INFO.
                format='%(asctime)s_%(message)s',  # Definierar formatet för loggmeddelandena.
                datefmt='%d/%m/%Y_%H:%M:%S'  # Sätter datumformatet för tidsstämpeln.
            )
            logging.info("Loggning har startat.")  # Loggar att loggningen har startat.
        except Exception as e:
            # Hanterar eventuella fel som uppstår vid loggkonfiguration.
            print(f"Fel vid konfiguration av loggning: {e}")
        return log_filename  # Returnerar loggfilens namn och sökväg.

    def log_event(self, event):
        """Loggar ett händelse med tidsstämpel."""
        try:
            logging.info(event)  # Loggar det givna händelsemeddelandet.
        except Exception as e:
            # Hanterar eventuella fel som uppstår vid loggning av händelsen.
            print(f"Fel vid loggning av händelse: {e}")

# Exempel på hur denna klass kan användas:
if __name__ == "__main__":
    logger = Logger()  # Skapar en instans av Logger.
    logger.log_event("Programmet har startat.")  # Loggar en startmeddelande för programmet.