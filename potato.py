# -*- coding: utf-8 -*-
"""
Created on Sat Jun 28 15:23:35 2025

@author: yoyo
"""

import tkinter as tk

import tkinter.messagebox
potato=0


def clickMe():
    global potato
    potato+=1
    tkinter.messagebox.showinfo(title="Become a Potato",message=str("You become a potato*"+str(potato)))

window = tk.Tk()

window.title("potato")

window.geometry('250x100')

label = tk.Label(window,text="Become a Potato Simulator")
label.pack()

entry = tk.Entry(window,width=30)
entry.pack()

button = tk.Button(window,text="Become a Potato",command = clickMe)
button.pack()


window.mainloop()
