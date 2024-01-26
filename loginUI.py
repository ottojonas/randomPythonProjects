import customtkinter as ctk 
import tkinter.messagebox as tkmb

ctk.set_appearance_mode("system")
ctk.set_default_color_theme("green")

root = ctk.CTk()
root.title("Login Page") 
root.geometry("1200 x 900")

frame = ctk.CTkFrame(master = root)
frame.pack(pady = 50 , padx = 140 , fill = "both" , expand = True) 

def login(event = None):
    username = "orange"
    password = "orangejuice"
    if userName.get() == username and passWord.get() == password: 
        tkmb.showinfo(title = "Login successful" , message = "You have logged in successfully")
    elif userName.get() == username and passWord.get() != password: 
        tkmb.showwarning(title = "Wrong password" , message = "Please try again") 
    elif userName.get() != username and passWord.get() == password: 
        tkmb.showwarning(title = "Wrong username" , message = "Please try again") 
    else: 
        tkmb.showerror(title = "Login failed" , message = "Please try again")

label = ctk.CTkLabel(master = root , text = "Welcome, Please Login") 
label.pack(pady = 29 , padx = 23) 

userName = ctk.CTkEntry(master = frame , placeholder_text = "Username or Email") 
userName.pack(pady = 29 , padx = 23)

passWord = ctk.CTkEntry(master = frame , placeholder_text= "Password", show = "*") 
passWord.pack(pady = 29 , padx = 23)

loginButton = ctk.CTkButton( master = frame , text = "Login" , command = login) 
loginButton.pack(pady = 29 , padx = 23)

root.bind("<Return>" , login) 

saveLogin = ctk.CTkCheckBox(master = frame , text = "Save Login Information?") 
saveLogin.pack(pady = 29 , padx = 23)

root.mainloop()