from tkinter import *
from tkinter import messagebox
def login():
    username=entry1.get()
    passward=entry2.get()
    if(username==""and passcode==""):
        messagebox.showinfo("","Blank not allowed")
        
    elif(username=="Yashika" and password=="Yashika@123")
        messagebox.showinfo("","Login success")
    else:
        messagebox.showinfo("","incorrect username and password")
root=Tk()
root.title("Login")
root.geometry("300*200")
global entry1
global entry2
Label(root,text="Username").place(x=20,y=20)
Label(root,text="passward").place(x=20,y=70)
entry1=Entry(root,bd=5)
entry1=place(x=140,y=20)
entry2=Entry(root,bd=5)
entry2=place(x=140,y=70)
Button(root,text="Login",command=login,height=3,width=13,bd=6).place(x=100,y=120)
root.mainloop()
