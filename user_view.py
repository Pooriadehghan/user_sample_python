from user_controller import UserController

from tkinter import *
from tkinter import messagebox
from tkinter import ttk

controller = UserController()


def save_click():
    success, message = controller.save(user_id.get(), name.get(), family.get(),
                                       national_id.get(), birth_date.get(),
                                       phone_number.get(), username.get(),
                                       password.get(), locked.get(), role.get())
    if success:
        messagebox.showinfo("User Save", message)
    else:
        messagebox.showerror("User Save Error", message)


def edit_click():
    success, message = controller.edit(user_id.get(), name.get(), family.get(),
                                       national_id.get(), birth_date.get(),
                                       phone_number.get(), username.get(),
                                       password.get(), locked.get(), role.get())
    if success:
        messagebox.showinfo("User Edit", message)
    else:
        messagebox.showerror("User Edit Error", message)


def delete_click():
    success, massege = controller.delete(user_id.get())
    if success:
        messagebox.showinfo("User Delete", massege)
    else:
        messagebox.showerror("User Delete Error", massege)


win = Tk()
win.geometry("1100x410")
win.title("User View")

# User Id
user_id = IntVar()
Label(win, text="User Id", ).place(x=20, y=20)
Entry(win, textvariable=user_id).place(x=90, y=20)

# Name
name = StringVar()
Label(win, text="Name", ).place(x=20, y=60)
Entry(win, textvariable=name).place(x=90, y=60)
# Family
family = StringVar()
Label(win, text="Family", ).place(x=20, y=100)
Entry(win, textvariable=family).place(x=90, y=100)
# National Id
national_id = StringVar()
Label(win, text="National Id", ).place(x=20, y=140)
Entry(win, textvariable=national_id).place(x=90, y=140)
# Birth Date
birth_date = StringVar()
Label(win, text="Birth Date", ).place(x=20, y=180)
Entry(win, textvariable=birth_date).place(x=90, y=180)
# Phone Number
phone_number = StringVar()
Label(win, text="Phone Num", ).place(x=20, y=220)
Entry(win, textvariable=phone_number).place(x=90, y=220)
# Username
username = StringVar()
Label(win, text="Username", ).place(x=20, y=260)
Entry(win, textvariable=username).place(x=90, y=260)
# Password
password = StringVar()
Label(win, text="Password", ).place(x=20, y=300)
Entry(win, textvariable=password).place(x=90, y=300)
# Locked
locked = BooleanVar()
Label(win, text="Locked", ).place(x=20, y=340)
Radiobutton(win, text="False", variable=locked, value=False).place(x=85, y=340)
Radiobutton(win, text="True", variable=locked, value=True).place(x=160, y=340)

# Role
role = StringVar()
Label(win, text="Role", ).place(x=20, y=380)
Entry(win, textvariable=role).place(x=90, y=380)

Button(win, text="Save", width=7, command=save_click).place(x=250, y=260)
Button(win, text="Edit", width=7, command=edit_click).place(x=330, y=260)
Button(win, text="Delete", width=7, command=delete_click).place(x=410, y=260)

table = ttk.Treeview(
    win,
    columns=(1, 2, 3, 4, 5, 6, 7, 8, 9, 10),
    show="headings",
)

table.heading(1, text="User Id")
table.heading(2, text="Name")
table.heading(3, text="Family")
table.heading(4, text="National Id")
table.heading(5, text="Birth Date")
table.heading(6, text="Phone Number")
table.heading(7, text="Username")
table.heading(8, text="Password")
table.heading(9, text="Locked")
table.heading(10, text="Role")

table.column(1, width=60)
table.column(2, width=100)
table.column(3, width=100)
table.column(4, width=100)
table.column(5, width=100)
table.column(6, width=100)
table.column(7, width=70)
table.column(8, width=80)
table.column(9, width=60)
table.column(10, width=60)
table.place(x=250, y=20)

win.mainloop()
