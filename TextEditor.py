from tkinter import *
from tkinter import filedialog, Text, simpledialog, messagebox, Frame, Entry, INSERT
import tkinter.scrolledtext as ScrolledText
from tkinter.filedialog import asksaveasfilename

app = Tk()
app.title("Text Editor")
app.geometry("400x380")
textArea = ScrolledText.ScrolledText(app, width = 100,
                                     height = 80,
                                     font=("Andale Mono", 12),
                                     highlightthickness=0,
                                     bd=2)
textArea.pack()

def new():
    if len(textArea.get("1.0", END + '-1c')) > 0:
        answer = messagebox.askyesno(title="Save File", message="Would you like to save this file?")
        if answer is True:
            save()
    textArea.delete('1.0', END)

def open_file():
    new()
    file = filedialog.askopenfile(parent = app, title = "Select a text file", filetypes=(("Text file", "*.txt"), ("All files", "*.*")))

    if file != None:
        contents = file.read()
        textArea.insert('1.0', contents)
        file.close()

def save():
    path = filedialog.asksaveasfile(mode="w")

    if path != None:
        data = textArea.get("1.0", END + '-1c')
        path.write(data)
        path.close()

def close():
    if messagebox.askyesno("Close", "Are you sure you want to quit?"):
        save()
        app.quit()

def cut():
    app.clipboard_clear()
    textArea.clipboard_append(string=textArea.selection_get())
    textArea.delete(index1=SEL_FIRST, index2=SEL_LAST)

def copy():
    app.clipboard_clear()
    textArea.clipboard_append(string = textArea.selection_get())

def paste():
    textArea.insert(INSERT, app.clipboard_get())

def delete():
    textArea.delete(index1=SEL_FIRST, index2=SEL_LAST)

def select_all():
    textArea.tag_add(SEL, "1.0", END)

def findInFile():
    findString = simpledialog.askstring("Find", "Enter text")
    textData = textArea.get("1.0", END)

    amount = textData.upper().count(findString.upper())

    if amount > 0:
        Label = messagebox.showinfo("Results", " I find " + str(amount)+ " " + findString)
    else:
        Label = messagebox.showinfo("Results", " Nope, sorry mate. ")

def undo():
    textArea.edit_undo()

def redo():
    textArea.edit_redo()

menu = Menu(app)
app.config(menu=menu)
file_menu = Menu(menu)
menu.add_cascade(label="File", menu=file_menu)

file_menu.add_command(label="New", command=new)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_separator()
file_menu.add_command(label="Save", command=save)
file_menu.add_command(label="Close", command=close)




edit_menu = Menu(menu)
w = menu.widgetName
menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Find", command=findInFile)
edit_menu.add_command(label="Undo", command=undo)
edit_menu.add_command(label="Redo", command=redo)
edit_menu.add_separator()
edit_menu.add_command(label="Cut", command=cut)
edit_menu.add_command(label="Copy", command=copy)
edit_menu.add_command(label="Paste", command=paste)
edit_menu.add_command(label="Delete", command=delete)
edit_menu.add_separator()
edit_menu.add_command(label="Select All", command=select_all)

app.mainloop()