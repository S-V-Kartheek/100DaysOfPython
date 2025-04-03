from tkinter import *
from tkinter import messagebox# from tkinter.messagebox import askokcancel,showinfo
import random
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list=[]
    password_list += [random.choice(letters) for _ in range(random.randint(5,10))]
    password_list += [random.choice(numbers) for _ in range(random.randint(2,4))]
    password_list += [random.choice(symbols) for _ in range(random.randint(2,4))]

    random.shuffle(password_list)
    password="".join(password_list)
    entry3.insert(0,password)
    pyperclip.copy(password)

def toggle_password():
    """Toggle between show/hide password."""
    if entry3.cget('show') == '':
        entry3.config(show='*')
        toggle_btn.config(text="👁️")
    else:
        entry3.config(show='')
        toggle_btn.config(text="🙈")


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website=entry1.get()
    email=entry2.get()
    password=entry3.get()

    if len(website)==0 or len(password)==0:
        messagebox.showinfo(title="oops",message="PLease fill all the fields")
    else:
        is_ok=messagebox.askokcancel(title=website,message=f"These are the details entered.\n Email: {email}\n Password: {password}\n Is it ok to save?")
        if is_ok:
            with open("data.txt","a") as file:
                file.write(f"{website} | {email} | {password}\n")
                entry1.delete(0,END)
                entry3.delete(0,END)

# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("Password Manager")
window.config(padx=50,pady=50,bg="white")

canvas=Canvas(height=200,width=200,bg="white",highlightthickness=0)
img=PhotoImage(file="logo.png")
canvas.create_image(100,100,image=img)
canvas.grid(row=0,column=1)

label1=Label(text="Website:",bg="white")
label1.grid(row=1,column=0)
label2=Label(text="Email/Username:",bg="white")
label2.grid(row=2,column=0)
label3=Label(text="Password:",bg="white")
label3.grid(row=3,column=0)

entry1=Entry(width=35)
entry1.grid(row=1,column=1,columnspan=2)
entry1.focus()
entry2=Entry(width=35)
entry2.grid(row=2,column=1,columnspan=2)
entry2.insert(0,"venkatakartheeks2005@gmail.com")
entry3=Entry(width=21)
entry3.grid(row=3,column=1)

button1=Button(text="Generate Password",bg="white",command=generate_password)
button1.grid(row=3,column=2)
toggle_btn = Button(text="👁️", bg="white", command=toggle_password)
toggle_btn.grid(row=3, column=3)

button2=Button(text="Add",width=30,command=save)
button2.grid(row=4,column=1,columnspan=2)


window.mainloop()