# Importeer TKinter voor GUI
import tkinter as tk
from tkinter import *
from tkinter import filedialog



#  Varriabelen die te gebruiken zijn over alle methoden
opdracht1 = "IP-adressen"
opdracht2 = "Mailadressen"
opdracht3 = "Entiteiten"

root = tk.Tk()

# Main Methode
def main():
    # Varriabelen
    # Globale 
    global var
    global L1
    global L1Text
    # Normale
    var = IntVar()
    L1Text = StringVar()
    # Labels
    welkomLabel = tk.Label(root, text = "Welkom bij de applicatie Groep7. Selecteer wat u wilt doen en klik op Volgende")
    L1 = tk.Label(root, textvariable=L1Text)
    # Buttons 
    B1 = Button(root, text="Volgende", command=lambda: keuze())
    # Radiobuttons voor keuze met waarde 
    R1 = Radiobutton(root, text=opdracht1, variable=var, value=3)
    R2 = Radiobutton(root, text=opdracht2, variable=var, value=2)
    R3 = Radiobutton(root, text=opdracht3, variable=var, value=3)
    # Plaats gewenste varriabelen in venster
    # Labels
    welkomLabel.pack()
    L1.pack()
    # Button
    B1.pack(anchor=E)
    # Radio-buttons voor keuze te maken
    R1.pack(anchor=W)
    R2.pack(anchor=W)
    R3.pack(anchor=W)

    root.mainloop()
    
# Aangeven welke keuze is gemaakt
def keuzePrint(opdracht):

    L1Text.set("U heeft gekozen voor: " + opdracht)

def get_output_filename(input_file_name):
    """ replace the suffix of the file with .rst """
    return input_file_name.rpartition(".")[0]


def button_go_callback():
    """ what to do when the "Go" button is pressed """
    input_file = Entry.get(entry)
    if input_file.rsplit(".")[-1] != "E01" or input_file.rsplit(".")[-1] != "e01" or input_file.rsplit(".")[-1] != "DD" or input_file.rsplit(".")[-1] != "dd" or input_file.rsplit(".")[-1] != "RAW" or input_file.rsplit(".")[-1] != "raw":
        statusText.set("Bestandsnaam heeft niet de '.E01', .'dd' of '.raw' extensie.")
        message.configure(fg="red")
        return
    else:
        if input_file.rsplit(".")[-1] == "E01" or input_file.rsplit(".")[-1] == "e01":
            table_contents = read_E01(input_file)
            if table_contents is None:
                statusText.set("Error reading file `{}'".format(input_file))
                message.configure(fg="red")
                return
            output_file = get_output_filename(input_file)
            if write_table(output_file, table_contents):
                statusText.set("Output is in {}".format(output_file))
                message.configure(fg="black")
            else:
                statusText.set("Writing file "
                               "`{}' did not succeed".format(output_file))
                message.configure(fg="red")

        elif input_file.rsplit(".")[-1] == "DD" or input_file.rsplit(".")[-1] == "dd":
            table_contents = read_E01(input_file)
            if table_contents is None:
                statusText.set("Error reading file `{}'".format(input_file))
                message.configure(fg="red")
                return
            output_file = get_output_filename(input_file)
            if write_table(output_file, table_contents):
                statusText.set("Output is in {}".format(output_file))
                message.configure(fg="black")
            else:
                statusText.set("Writing file "
                               "`{}' did not succeed".format(output_file))
                message.configure(fg="red")

        elif input_file.rsplit(".")[-1] != "RAW" or input_file.rsplit(".")[-1] != "raw":
            table_contents = read_E01(input_file)
            if table_contents is None:
                statusText.set("Error reading file `{}'".format(input_file))
                message.configure(fg="red")
                return
        output_file = get_output_filename(input_file)
        if write_table(output_file, table_contents):
                statusText.set("Output is in {}".format(output_file))
                message.configure(fg="black")
        else:
            statusText.set("Writing file "
                           "`{}' did not succeed".format(output_file))
            message.configure(fg="red")
def button_browse_callback():

    """ What to do when the Browse button is pressed """
    filename = filedialog.askopenfilename()
    e1 = Entry(frame)
    e1.pack()
    e1.delete(0, END)
    e1.insert(0, filename)

# Methode voor het aangeven van het bestand
def gui():
    # Globale varriabelen
    global frame
    global statusText
    global entry
    global message

    # Varriabelen met gewenste argumenten
    # Hoofdvenster
    root = Tk()
    # Frame in hoofdvenster
    frame = Frame(root)
    
    # Tekst voor label
    statusText = StringVar(root)
    statusText.set("Druk op Bladeren om het bestand in te laden en druk op Volgende.")
    # Labels
    message = Label(root, textvariable=statusText)
    label = Label(root, text="Bestand: ")
    # Entry
    entry = Entry(frame, width=50)
    # Afstand
    separator = Frame(root, height=2, bd=1, relief=SUNKEN)

    # Buttons
    button_go = Button(root,
                       text="Volgende",
                       command= lambda :button_go_callback())
    button_browse = Button(root,
                           text="Bladeren",
                           command= lambda : button_browse_callback())
    button_exit = Button(root,
                         text="Exit",
                         command=sys.exit)
 

    
    # De gewenste varriabelen in venster plaatsen
    
    # Frame
    frame.pack()
    # Labels
    message.pack()
    label.pack()
    # Knoppen
    button_go.pack()
    button_browse.pack()
    button_exit.pack()
    # Entry
    entry.pack()
    # Afstand
    separator.pack(fill=X, padx=5, pady=5)
    

def button_browse_callback():
    filename = filedialog.askopenfilename()
    entry.delete(0, END)
    entry.insert(0, filename)

# Juiste methode aanroepen
def keuze():
    global selectie
    selectie = var.get()
    if selectie == 1:
        keuzePrint(opdracht1)
        gui()

    elif selectie == 2:
        keuzePrint(opdracht2)
        gui()

    elif selectie == 3:
        keuzePrint(opdracht3)
        gui()




if __name__ == '__main__':
    main()
