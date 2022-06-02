from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    random_letter = [random.choice(letters) for _ in range(random.randint(8, 10))]
    random_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    random_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]

    password_list = random_letter + random_symbols + random_numbers

    random.shuffle(password_list)

    password = ''.join(password_list)
    password_text_box.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_function():
    website = website_text_box.get()
    username = username_text_box.get()
    password = password_text_box.get()
    new_data = {
        website: {
            'Email/Username': username,
            'password': password
        }
    }

    if len(website) * len(username) * len(password) == 0:
        messagebox.showinfo(title='Oops', message='Please don\'t leave any fields empty!')

    else:
        is_ok = messagebox.askokcancel(title=website,
                                       message=f'These are the details entered: \nEmail/Username: {username} \nPassword: {password}\nIs it ok to save?')

        if is_ok:
            try:
                with open('data.json', 'r') as file:
                    # Reading the old data
                    data = json.load(file)

            except FileNotFoundError:
                with open('data.json', 'w') as file:
                    json.dump(new_data, file, indent=4)

            else:
                # Updating old data with new data
                data.update(new_data)

                with open('data.json', 'w') as file:
                    json.dump(data, file, indent=4)

        website_text_box.delete(0, 'end')
        password_text_box.delete(0, 'end')
# ---------------------------- search password ------------------------------- #
def search():

    website = website_text_box.get()
    try:
        with open('data.json', 'r') as file:
            data = json.load(file)
        messagebox.askokcancel(title=website,
                               message=f'Email/Username: {data[website]["Email/Username"]}\n Password: {data[website]["password"]}')

    except FileNotFoundError:
        messagebox.showinfo(title='Error', message='No Data File Found')

    except KeyError:
        messagebox.showinfo(title='Error', message='No details for the website exits')
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Password manager')
window.config(width=500, height=500, padx=50, pady=50)

canvas = Canvas(width=200, height=200)
lock_image = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=lock_image)
canvas.grid(column=1, row=0, columnspan=2)

website_label = Label(text='Website:')
website_label.grid(column=0, row=1)

username_label = Label(text='Email/Username:')
username_label.grid(column=0, row=2)

password_label = Label(text='Password:')
password_label.grid(column=0, row=3)

website_text_box = Entry(width=21)
website_text_box.grid(column=1, row=1)

username_text_box = Entry(width=42)
username_text_box.grid(column=1, row=2, columnspan=2)
username_text_box.insert(0, 'alvinlocity76@gmail.com')

password_text_box = Entry(width=21)
password_text_box.grid(column=1, row=3)

generate_pw_button = Button(text='Generate Password', command=generate_password)
generate_pw_button.grid(column=2, row=3)

add_button = Button(text='Add', width=36, command=add_function)
add_button.grid(column=1, row=4, columnspan=2)

search_button = Button(text='Search', width=15, command=search)
search_button.grid(column=2, row=1)

window.mainloop()
