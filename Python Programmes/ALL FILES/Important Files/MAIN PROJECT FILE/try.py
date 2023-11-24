import tkinter as tk

def toggle_password():
    if passwd_entry.cget('show') == '':
        passwd_entry.config(show='*')
        toggle_btn.config(text='Show Password')
    else:
        passwd_entry.config(show='')
        toggle_btn.config(text='Hide Password')

root = tk.Tk()

passwd_entry = tk.Entry(root, show='*', width=20)
passwd_entry.pack(side=tk.LEFT)

toggle_btn = tk.Button(root, text='Show Password', width=15, command=toggle_password)
toggle_btn.pack(side=tk.LEFT)

root.mainloop()