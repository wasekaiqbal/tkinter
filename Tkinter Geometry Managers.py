from tkinter import *

#window creation
root = Tk()
root.title('LOGIN APPLICATION')
root.geometry('800x900')

frame = Frame(master=root, height= 400, width = 600, bg='#F4C2C2')

lbl1 = Label(frame, text = 'Full name' , bg="#8560A3" ,fg='white', width=22)
lbl2 = Label(frame, text = 'EMAIL ID' , bg="#8560A3" ,fg='white', width=22)  
lbl3 = Label(frame, text = 'ENTER PASSWORD' , bg="#8560A3" ,fg='white', width=22)         

name_entry = Entry(frame)
email_entry = Entry(frame)
pass_entry = Entry(frame, show='*')

def display():
    name = name_entry.get()
    greet = "hey" + name
    message = "\nCongratulations on your new account"
    textbox.insert(END, greet)
    textbox.insert(END, message)

textbox = Text(bg="#8560A3", fg='white')

btn = Button(text = 'create account',command= display, bg="#6084A3")

frame.place(x=40,y=10)
lbl1.place(x=40,y=40)
name_entry.place(x=280,y=40)
lbl2.place(x=40,y=80)
email_entry.place(x=280,y=80)
lbl3.place(x=40,y=120)
pass_entry.place(x=280,y=120)
btn.place(x=230,y=340)
textbox.place(y=500)

root.mainloop()
