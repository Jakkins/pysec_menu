# main.py

import tkinter as tk
from tkinter import END, LEFT, ttk
import os

root = tk.Tk()
root.tk.call('lappend', 'auto_path', './awthemes-10.4.0')
root.tk.call('package', 'require', 'awdark')
style = ttk.Style()  # create a style
style.theme_use('awdark')  # set the theme

container = ttk.Frame(root)
container.pack(side="top", fill="both", expand=True)
container.columnconfigure(tuple(range(60)), weight=1)
container.rowconfigure(tuple(range(30)), weight=1)

frame_button = ttk.Frame(container)
frame_button.grid(column=0, row=0, sticky="news")
frame_listbox = ttk.Frame(container)
frame_listbox.grid(column=1, row=0, sticky="news")

listbox = tk.Listbox(frame_listbox)
listbox.grid(column=1, row=0, sticky="news")

btn1 = ttk.Button(frame_button, text="default gateway", takefocus=0)
btn1.configure(command=lambda: {os.system(
    "python ./scripts/lan_radar/find_default_gateway.py")})
btn2 = ttk.Button(frame_button, text="B2", takefocus=0)
btn2.configure(command=lambda: {print('wooo')})

btn3 = ttk.Button(frame_button, text="B3", takefocus=0)
btn3.configure(command=lambda: {print('wooo')})

objs = [btn1, btn2, btn3]

counter = 0
for obj in objs:
    obj.grid(column=0, row=counter, sticky="news")
    counter += 1


root.mainloop()
