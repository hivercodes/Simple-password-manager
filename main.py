import json
from tkinter import *
from tkinter import messagebox
import random
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def pass_gen():
    password_field.delete(0, END)
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    for char in range(nr_letters):
        password_list.append(random.choice(letters))

    for char in range(nr_symbols):
        password_list += random.choice(symbols)

    for char in range(nr_numbers):
        password_list += random.choice(numbers)

    random.shuffle(password_list)

    password = ""
    for char in password_list:
        password += char
    password_field.insert(0, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def write_info():

    website = website_text_field.get()
    user_name = user_name_field.get()
    password = password_field.get()
    window.clipboard_append(password)
    new_data = {
        website: {
        "username": user_name,
        "password": password,
    }
    }

    if website == "" or user_name == "" or password == "":
        messagebox.showinfo(title="Missing information", message="One or more of the boxes of information is empty")
    else:
        try:
            with open("password.json", "r") as file:

                data = json.load(file)
                data.update(new_data)
            with open("password.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
                website_text_field.delete(0, END)
                password_field.delete(0, END)
        except json.decoder.JSONDecodeError:
            with open("password.json", "w") as file:
                json.dump(new_data, file, indent=4)
                website_text_field.delete(0, END)
                password_field.delete(0, END)
        except FileNotFoundError:
            with open("password.json", "w") as file:
                json.dump(new_data, file, indent=4)
                website_text_field.delete(0, END)
                password_field.delete(0, END)

# ---------------------------- Search ------------------------------- #


def search():
    website = website_text_field.get()
    try:
        with open("password.json", "r") as file:
            data = json.load(file)
            if website in data:
                for key in data:
                    if key.lower() == website.lower():
                        sub_dict = data[key]
                        user = sub_dict["username"]
                        pw = sub_dict["password"]
                        messagebox.showinfo(title="Search Result",
                                            message=f"{key} has the login information:\n"
                                                    f"username: {user}\n"
                                                    f"password: {pw}")
            else:
                messagebox.showinfo(title="Search Result",
                                    message=f"Unknown website")
    except json.decoder.JSONDecodeError:
        messagebox.showinfo(title="Search Result",
                            message=f"Empty database")
    except FileNotFoundError:
        messagebox.showinfo(title="Search Result",
                            message=f"Empty database")

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
lock = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200, highlightthickness=0)
canvas.create_image(100,100, image=lock)
canvas.grid(column=1, row=0)


website_text = Label(text="Website:")
website_text.grid(column=0, row=1)

website_text_field = Entry(width=35)
website_text_field.grid(column=1, row=1, columnspan=2)

user_name_text = Label(text="Username/Email:")
user_name_text.grid(column=0, row=2)

user_name_field = Entry(width=35)
user_name_field.grid(column=1, row=2, columnspan=2)
user_name_field.insert(0, "example@example.com")

password_text = Label(text="Password:")
password_text.grid(column=0, row=3)

password_field = Entry(width=22)
password_field.grid(column=1, row=3)

password_button = Button(text="Password", command=pass_gen)
password_button.grid(column=2, row=3)

add_button = Button(text="Add", width=35, command=write_info)
add_button.grid(column=1, row=4, columnspan=2)

search_button = Button(text="Search", command=search)
search_button.grid(column=2, row=1)










window.mainloop()