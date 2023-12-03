import tkinter as tk
from tkinter import filedialog

def save_file():
    file_path = filedialog.asksaveasfilename(title='Save File', filetypes=(('Text Files', '*.txt'), ('All Files', '*.*')))
    if file_path:
        with open(file_path+'.txt', 'w') as file:
            file.write('hello')

root = tk.Tk()
root.title('Save File')
button = tk.Button(root, text='Save File', command=save_file)
button.pack()
root.mainloop()
