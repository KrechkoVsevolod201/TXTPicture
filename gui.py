import tkinter
import customtkinter
import os

import main

root_tk = tkinter.Tk()  # create the Tk window like you normally do
root_tk.geometry("400x240")
root_tk.title("CustomTkinter Test")



def button_function():
    main.bw_convert()
    main.text_generator()
    print("button pressed")

# Use CTkButton instead of tkinter Button
label = customtkinter.CTkLabel(master=root_tk, text='Filename', text_color='black')
text = customtkinter.CTkEntry(master=root_tk, corner_radius=10)
button = customtkinter.CTkButton(master=root_tk, corner_radius=10, command=button_function)
button.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
text.place(relx=0.5, rely=0.3, anchor=tkinter.CENTER)
label.place(relx=0.5, rely=0.1, anchor=tkinter.CENTER)

root_tk.mainloop()