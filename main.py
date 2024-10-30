import tkinter as tk  # Importerar tkinter-modulen som 'tk' för att skapa GUI-komponenter.
from menu import main_menu  # Importerar funktionen 'main_menu' från filen 'menu' för att visa huvudmenyn.

def main():
    root = tk.Tk()  # Skapar huvudfönstret för tkinter-applikationen.
    root.title("Övervakningsapplikation")  # Sätter titeln för huvudfönstret.
    main_menu(root)  # Kallar på funktionen 'main_menu' för att visa applikationens huvudmeny i fönstret.
    root.mainloop()  # Startar huvudloopen för tkinter, vilket håller fönstret öppet och aktivt.

if __name__ == "__main__":  # Kontrollerar om skriptet körs direkt.
    main()  # Kör funktionen 'main' för att starta applikationen.
