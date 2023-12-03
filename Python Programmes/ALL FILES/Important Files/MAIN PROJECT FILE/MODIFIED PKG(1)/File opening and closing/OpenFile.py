from tkinter import*
from tkinter import filedialog

def choose_file():
    file_name=filedialog.askopenfilename()
    #Function returns the file's name
    return file_name

root=Tk()
root.title("Choose a file")

button=Button(root,text="Choose a file",command=choose_file)
button.pack(pady=20)

root.mainloop()
