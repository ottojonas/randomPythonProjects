# * Basic - not working
import tkinter as tk

import customtkinter as ctk

ctk.set_appearance_mode("system")
ctk.set_default_color_theme("green")

root = ctk.CTk()
root.title("ToDo List")
root.geometry("1200 x 900")

frame = ctk.CTkFrame(master=root)
frame.pack(pady=50, padx=140, fill="both", expand=True)

todoItem = ctk.CTkEntry(master=frame, placeholder_text="New Task")
todoItem.pack(pady=29, padx=23)


def saveItem(event=None):
    itemList.insert(ctk.END, todoItem.get())
    todoItem.delete(0, ctk.END)


saveItem = ctk.CTkButton(master=frame, text="Save Item", command=saveItem)
saveItem.pack(pady=29, padx=23)

root.bind("<Return>", saveItem)

itemList = ctk.CTkListbox(master=root)
itemList.pack()

root.mainloop()
