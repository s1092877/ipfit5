# Importeer TKinter voor GUI
import tkinter as tk
from tkinter import *
from tkinter import filedialog

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

def get_output_filename(input_file_name):
    """ replace the suffix of the file with .rst """
    return input_file_name.rpartition(".")[0]

def gui():
    def button_go_callback():
        """ what to do when the "Go" button is pressed """
        input_file = entry.get()
        if input_file.rsplit(".")[-1] != "E01":
            statusText.set("Filename must end in `.E01'")
            message.configure(fg="red")
            return
        else:
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
        entry.delete(0, END)
        entry.insert(0, filename)

    root = Tk()
    frame = Frame(root)
    frame.pack()

    statusText = StringVar(root)
    statusText.set("Press Browse button or enter E01 filename, "
                   "then press the Go button")

    label = Label(root, text="E01: ")
    label.pack()
    entry = Entry(root, width=50)
    entry.pack()
    separator = Frame(root, height=2, bd=1, relief=SUNKEN)
    separator.pack(fill=X, padx=5, pady=5)

    button_go = Button(root,
                       text="Go",
                       command=button_go_callback)
    button_browse = Button(root,
                           text="Browse",
                           command=button_browse_callback)
    button_exit = Button(root,
                         text="Exit",
                         command=sys.exit)
    button_go.pack()
    button_browse.pack()
    button_exit.pack()

    separator = Frame(root, height=2, bd=1, relief=SUNKEN)
    separator.pack(fill=X, padx=5, pady=5)

    message = Label(root, textvariable=statusText)
    message.pack()

def keuze():
    global selectie
    selectie = var.get()
    if selectie == 1:
        keuzePrint(opdracht1)
        gui()
        button_browse = Button(root,
                               text="Browse",
                               command=button_browse_callback)
    elif selectie == 2:
        keuzePrint(opdracht2)
        gui()
        button_browse = Button(root,
                               text="Browse",
                               command=button_browse_callback)
    elif selectie == 3:
        keuzePrint(opdracht3)
        gui()
        button_browse = Button(root,
                               text="Browse",
                               command=button_browse_callback)
    else:
        print("Geen keuze")



if __name__ == '__main__':
    main()