from tkinter import *
from tkinter import filedialog, Text, simpledialog, messagebox, Frame, Entry, INSERT
import tkinter.scrolledtext as ScrolledText
from tkinter.filedialog import asksaveasfilename
from tkinter.font import Font, families
import tkinter.colorchooser
import tkinter as tk


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
    try:
        textArea.edit_undo()
    except TclError:
        pass

def redo():
    try:
        textArea.edit_redo()
    except TclError:
        pass

def about():
    label = messagebox.showinfo("About", "A Python alternative to Notepad")

def help():
    label = messagebox.showinfo("Help", "How can I help you?:)")

def color():
    try:
        (rgb, hx) = tkinter.colorchooser.askcolor()
        textArea.tag_add('color', 'sel.first', 'sel.last')
        textArea.tag_configure('color', foreground=hx)
    except TclError:
        pass

def bold():
    try:
        current_tags = textArea.tag_names("sel.first")
        if "bold" in current_tags:
            textArea.tag_remove("bold", "sel.first", "sel.last")
        else:
            textArea.tag_add("bold", "sel.first", "sel.last")
            bold_font = Font(textArea, textArea.cget("font"))
            bold_font.configure(weight="bold")
            textArea.tag_configure("bold", font=bold_font)
    except TclError:
        pass

def underline():
    try:
        current_tags = textArea.tag_names("sel.first")
        if "underline" in current_tags:
            textArea.tag_remove("underline", "sel.first", "sel.last")
        else:
            textArea.tag_add("underline", "sel.first", "sel.last")
            underline_font = Font(textArea, textArea.cget("font"))
            underline_font.configure(underline=1)
            textArea.tag_configure("underline", font=underline_font)
    except TclError:
        pass

def italic():
    try:
        current_tags = textArea.tag_names("sel.first")
        if "italic" in current_tags:
            textArea.tag_remove("italic", "sel.first", "sel.last")
        else:
            textArea.tag_add("italic", "sel.first", "sel.last")
            italic_font = Font(textArea, textArea.cget("font"))
            italic_font.configure(slant="italic")
            textArea.tag_configure("italic", font=italic_font)
    except TclError:
        pass

def choose_size():
    def size():
        try:
            enter_size.get() == int(enter_size.get())
            textArea.config(font=("Arial", enter_size.get()))
        except ValueError:
            messagebox.showinfo("Error", "Wrong values!!! Use numbers.")

    t = tk.Toplevel(app)
    font_size = tk.Label(t, text='Font Size: ')
    font_size.grid(row=0, column=0, sticky='nsew')
    enter_size = tk.Entry(t)
    enter_size.grid(row=0, column=1, sticky='nsew')
    quit_btn = tk.Button(t, text='Quit',
                         command=t.destroy)
    ok_btn = tk.Button(t, text='Apply Changes',
                      command= size)
    ok_btn.grid(row=1, column=1, sticky='nsew')
    quit_btn.grid(row=1, column=0, sticky='nsew')

#====================

app = tk.Tk()

app.title("Text Editor")
app.geometry("400x380")
textArea = ScrolledText.ScrolledText(app, width = 100,
                                     height = 80,
                                     font=("Andale Mono", 12),
                                     highlightthickness=0,
                                     bd=2)
textArea.pack()

# text = tk.Text(app)
# text.pack(expand=1, fill='both')


#===================

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
edit_menu.add_command(label="Color", command=color)
edit_menu.add_command(label="Bold", command=bold)
edit_menu.add_command(label="Underline", command=underline)
edit_menu.add_command(label="Italic", command=italic)
edit_menu.add_command(label="Size", command=choose_size)
edit_menu.add_separator()
edit_menu.add_command(label="Select All", command=select_all)

help_menu = Menu(menu)
menu.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="Help", command=help)
help_menu.add_command(label="About", command=about)

app.mainloop()