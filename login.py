from customtkinter import *
from PIL import Image
from tkinter import messagebox
# to open the window

def login():
    if usernameEntry.get() == '' or passwordEntry.get() == '':
        messagebox.showerror('Error','All fields are required')
    elif usernameEntry.get() == 'Garvit' and passwordEntry.get() == '1234':
        messagebox.showinfo('Success','Login is successful')
        root.destroy()
        import ems
    else:
        messagebox.showerror('Error','Wrong Credentials')



root = CTk()
root.geometry('930x478')
root.resizable(0,0)
root.title('login page')
image = CTkImage(Image.open('image123.jpg'),size=(930,478))
imageLable = CTkLabel(root,image=image,text='')
imageLable.place(x=0,y=0)
headinglabel = CTkLabel(root,text='Employee Management System',bg_color='#FFFFFF',font=('Goundy Old Style',20,'bold'),text_color='dark blue')
headinglabel.place(x=20,y=100)

usernameEntry = CTkEntry(root,placeholder_text='Enter Your Username',width=180,bg_color='#FFFFFF')
usernameEntry.place(x=50,y=150)

passwordEntry = CTkEntry(root,placeholder_text='Password',width=180,bg_color='#FFFFFF',show='*')
passwordEntry.place(x=50,y=200)

loginButton = CTkButton(root,text='Login',cursor='hand2',bg_color='#FFFFFF',command=login)
loginButton.place(x=70,y=250)

root.mainloop()




