from tkinter import *
from tkinter import messagebox

import random
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
               'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    list_of_letters = [random.choice(letters) for _ in range(nr_letters)]
    list_of_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    list_of_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = list_of_letters + list_of_symbols + list_of_numbers
    random.shuffle(password_list)

    password = "".join(password_list)
    print(f"Your password is: {password}")

    entry_password.delete(0, END)
    entry_password.insert(0, password)

    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = entry_website.get()
    email = entry_email.get()
    password = entry_password.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(
            title="Oops", message="Please make sure you haven't left any fields empty.")
        return

    is_ok = messagebox.askokcancel(
        title=website, message=f"These are the details entered:\nEmail: {email}\nPassword: {password}\nIs it ok to save?")

    if not is_ok:
        return

    with open("data.txt", "a") as data_file:
        data_file.write(f"{website} | {email} | {password}\n")

    entry_website.delete(0, END)
    entry_password.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
WHITE = "#FFFFFF"


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg=WHITE)

canvas = Canvas(width=200, height=200, bg=WHITE, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)

label_website = Label(text="Website:", fg="black", bg="white")
label_email = Label(text="Email/Username:", fg="black", bg="white")
label_password = Label(text="Password:", fg="black", bg="white")

entry_website = Entry(width=35, fg="black", bg="white")
entry_email = Entry(width=35, fg="black", bg="white")
entry_password = Entry(width=21, fg="black", bg="white")

button_generate = Button(text="Generate Password", command=generate_password)
button_add = Button(text="Add", width=36, command=save)


# layout
canvas.grid(row=0, column=1)

label_website.grid(row=1, column=0)
entry_website.grid(row=1, column=1, columnspan=2)
label_email.grid(row=2, column=0)
entry_email.grid(row=2, column=1, columnspan=2)
label_password.grid(row=3, column=0)
entry_password.grid(row=3, column=1)
button_generate.grid(row=3, column=2)
button_add.grid(row=4, column=1, columnspan=2)

# default value
entry_website.focus()
entry_email.insert(0, "saibi@saibi.com")

window.mainloop()
