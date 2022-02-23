from tkinter import *



# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

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

password_text = Label(text="Password:")
password_text.grid(column=0, row=3)

password_field = Entry(width=22)
password_field.grid(column=1, row=3)

password_button = Button(text="Password")
password_button.grid(column=2, row=3)

add_button = Button(text="Add", width=35)
add_button.grid(column=1, row=4, columnspan=2)










window.mainloop()