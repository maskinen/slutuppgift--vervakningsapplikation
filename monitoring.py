import psutil  # Importerar psutil-modulen för att få systeminformation om CPU, minne och disk.
from tkinter import messagebox  # Importerar messagebox från tkinter för att visa meddelanden i GUI.
from my_logging import Logger  # Importerar Logger-klassen från my_logging för att logga händelser.

logger = Logger()  # Skapar en instans av Logger för att logga händelser.

def start_monitoring():
    # Funktion för att starta övervakningen och logga händelsen.
    logger.log_event("Övervakning startad")  # Loggar att övervakningen har startats.
    messagebox.showinfo("Starta övervakning", "Övervakning startad!")  # Visar ett meddelande om att övervakningen startats.

def list_active_monitoring():
    # Funktion för att lista aktiv övervakning.
    logger.log_event("Listar aktiv övervakning")  # Loggar att den aktiva övervakningen listas.

    # Hämtar och lagrar information om CPU, minne och disk.
    cpu_info = get_cpu_usage()  # Hämtar CPU-användning.
    memory_info = get_memory_usage()  # Hämtar minnesanvändning.
    disk_info = get_disk_usage()  # Hämtar diskanvändning.

    # Samlar informationen och visar den i ett meddelande.
    result = f"{cpu_info}\n{memory_info}\n{disk_info}"  # Formaterar informationen.
    messagebox.showinfo("Aktiv övervakning", result)  # Visar den aktiva övervakningen i en messagebox.

def get_cpu_usage():
    # Funktion för att hämta CPU-användning.
    cpu_usage = psutil.cpu_percent(interval=1)  # Hämtar CPU-användning som procent.
    logger.log_event(f"CPU-användning: {cpu_usage}%")  # Loggar CPU-användningen.
    return f"CPU Användning: {cpu_usage}%"  # Returnerar formaterad CPU-användning.

def get_memory_usage():
    # Funktion för att hämta minnesanvändning.
    memory = psutil.virtual_memory()  # Hämtar information om minnesanvändning.
    used_memory = memory.used / (1024 ** 3)  # Konverterar använt minne till GB.
    total_memory = memory.total / (1024 ** 3)  # Konverterar totalt minne till GB.
    logger.log_event(f"Minnesanvändning: {memory.percent}% ({used_memory:.2f} GB out of {total_memory:.2f} GB used)")  # Loggar minnesanvändningen.
    return f"Minnesanvändning: {memory.percent}% ({used_memory:.2f} GB out of {total_memory:.2f} GB used)"  # Returnerar formaterad minnesanvändning.

def get_disk_usage():
    # Funktion för att hämta diskanvändning.
    disk = psutil.disk_usage('/')  # Hämtar information om diskanvändning.
    used_disk = disk.used / (1024 ** 3)  # Konverterar använd disk till GB.
    total_disk = disk.total / (1024 ** 3)  # Konverterar total disk till GB.
    logger.log_event(f"Diskanvändning: {disk.percent}% ({used_disk:.2f} GB out of {total_disk:.2f} GB used)")  # Loggar diskanvändningen.
    return f"Diskanvändning: {disk.percent}% ({used_disk:.2f} GB out of {total_disk:.2f} GB used)"  # Returnerar formaterad diskanvändning.