"""
A program to automate the task to rename photos from laboratory test.
The program get the names of the photos from a CSV file and then rename the photos inside a folder.
"""

# import the required libraries
from tkinter import *
from tkinter import filedialog, messagebox
import os
import csv


# create variables
names = []

# create an instance of tkinter frame
window = Tk()
window.wm_title("Renomeador de fotos do Salt Spray")

# set the geometry of tkinter frame
window.geometry("700x200")


# function to read the csv file with the names and save it into a list
def get_names():
    file = filedialog.askopenfile(mode='r', filetypes=[("csv files", "*.csv")])
    if file:
        ent1.insert(END, file.name)
        f = open(file.name)
        csv_f = csv.reader(f)
        for row in csv_f:
            names.append(row)
        f.close()
    else:
        messagebox.showerror("Erro", "Selecione um arquivo csv!")


# function to get the path where the photos to be renamed are
def get_folder_path():
    global folder_selected
    folder_selected = filedialog.askdirectory()
    ent2.insert(END, folder_selected)
    return folder_selected


# function to rename the photos
def rename():
    try:
        os.chdir(folder_selected)
        if len(names) == len(os.listdir(folder_selected)):
            for (i, filename) in enumerate(os.listdir(folder_selected)):
                if filename.endswith('.jpg'):
                    os.rename(filename, str(*names[i]) + '.jpg')
            messagebox.showinfo("Pronto", "Arquivos jpg renomeados com sucesso!")
            ent1.delete(0, END)
            ent2.delete(0, END)
        else:
            messagebox.showinfo("Erro", "Quantidade de fotos diferente da quantidade de nomes salvos no arquivo! Corrija e tente novamente!")
    except IndexError as error:
        messagebox.showinfo("Erro", "Selecione um arquivo csv válido e com a mesma quantidade!")
    except OSError as error:
        messagebox.showinfo("Erro", "Selecione um caminho válido!")
    except NameError as error:
        messagebox.showinfo("Erro", "Selecione um caminho válido!")


# create the labels of the interface
label1 = Label(window, text='Selecione o arquivo')
label1.grid(row=3, column=0)
label2 = Label(window, text='Selecione o local das fotos')
label2.grid(row=4, column=0)
label3 = Label(window, text='Renomeador de fotos dos ensaios de Salt Spray')
label3.grid(row=0, column=0, columnspan=3)
label4 = Label(window, text='Atualize o nome das fotos dos ensaios de Salt Spray '
                            'através do arquivo do tipo .csv contendo o código das peças do referente ensaio.')
label4.grid(row=1, column=0, columnspan=3)
label5 = Label(window, text='Instruções\n1.Inserir local do arquivo .csv que contém o nome das fotos\n'
                            '2. Inserir o local onde estão as fotos do ensaio\n'
                            '3. As fotos devem estar na pasta na mesma sequência de nomes no arquivo csv')
label5.grid(row=2, column=0, columnspan=3)

# create the text boxes of the labels
ent1 = Entry(window)
ent1.grid(row=3, column=1)
ent2 = Entry(window)
ent2.grid(row=4, column=1)

# create the buttons widgets
button1 = Button(window, text="Pesquisar", width=12, command=get_names)
button1.grid(row=3, column=2)
button2 = Button(window, text="Pesquisar", width=12, command=get_folder_path)
button2.grid(row=4, column=2)
button3 = Button(window, text="Renomear", width=12, command=rename)
button3.grid(row=5, column=1)

# keep the window open
window.mainloop()
