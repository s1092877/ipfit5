# Importeer TKinter voor GUI
import tkinter as tk
from tkinter import *

opdracht1 = "IP-adressen"
opdracht2 = "Mailadressen"
opdracht3 = "Entiteiten"
root = tk.Tk()

def main():

    global var
    var = IntVar()







    # Toon welkom bericht
    welkomLabel = tk.Label(root, text = "Welkom bij de applicatie Groep7. Selecteer wat u wilt doen en klik op Volgende")
    welkomLabel.pack()




    # Radiobuttons aanmaken voor keuze te maken



    R1 = Radiobutton(root, text = opdracht1,variable = var, value = 1)
    R1.pack(anchor = W)
    R2 = Radiobutton(root, text = opdracht2, variable = var, value = 2)
    R2.pack(anchor = W)
    R3 = Radiobutton(root, text = opdracht3, variable = var, value = 3)
    R3.pack(anchor = W)





        # Button aanmken om keuze te bevestigen

    B1 = Button (root, text = "Volgende", command = lambda : keuze())
    B1.pack(anchor = E)

    global  L1



    root.mainloop()

def keuzePrint(opdracht):
    L1 = tk.Label(root, text="U heeft gekozen voor: " + opdracht)
    L1.pack()


def keuze():
    global selectie
    selectie = var.get()
    if selectie == 1:
        keuzePrint(opdracht1)
    elif selectie == 2:
        keuzePrint(opdracht2)
    elif selectie == 3:
        keuzePrint(opdracht3)
    else:
        print("Geen keuze")



if __name__ == '__main__':
    main()