from tkinter import *
import random
from tkinter import messagebox
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

#Password Generator Project
def password_gen():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)



    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers

    random.shuffle(password_list)

    password = "".join(password_list)

    pass_entry.insert(0, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_button_func():

    if web_entry.get() == "" or pass_entry.get() == "" or user_entry.get() == "":
        messagebox.showerror(title="Empty Field", message="Ooops .. it seems you forgot a field.")

    else:        

        is_ok = messagebox.askokcancel(title="Save", message="Are you sure you want to save the credentials provided?")

        if is_ok == True:
            write_to_csv(web_entry.get(),user_entry.get(),pass_entry.get())
            web_entry.delete(0, END)
            pass_entry.delete(0, END)

def write_to_csv(website,name,password):


    data_dict = {website:
                 {
                     "email":name,
                     "password":password

                 }
    }
    try:
        file = open("./passwords.json", "r") # open the file in read mode
        data = json.load(file)
        data.update(data_dict)

    #writing to the file
        file = open("./passwords.json", "w") 
        json.dump(data,file,indent=4)
        file.close() 
    except FileNotFoundError:

        file = open("./passwords.json", "w") 
        json.dump(data_dict,file,indent=4)
        file.close() 

# ---------------------------- SEARCH PASSWORD ------------------------------- #
        




def load_passwords_file():
    try:
        file = open("./passwords.json", "r") # open the file in read mode
        data = json.load(file)
        search_data = data[web_entry.get()]
        messagebox.showinfo(title="website Info",message=f"website {web_entry.get()} \n username : {search_data['email']} \n password : {search_data['password']}")
    except KeyError:
        messagebox.showerror(title="website Info",message=f"Data does not exist!")






# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.minsize(width=350,height=325)


canvas = Canvas(height=200,width=200, highlightthickness=0)
pass_foto = PhotoImage(file="./logo.png")
pass_img = canvas.create_image(100,100, image= pass_foto)
canvas.place(x=90,y=0)

#Buttons

gen_pass = Button(text="Search", command=load_passwords_file)
gen_pass.place(x=240,y=175)

gen_pass = Button(text="Generate", command=password_gen)
gen_pass.place(x=240,y=225)

add_button = Button(text="Add", width=25,command=add_button_func)
add_button.place(x=110,y=260)





#TextInputs
web_entry = Entry(width=20)
web_entry.place(x=110,y=180)
web_entry.focus()

user_entry = Entry(width=30)
user_entry.place(x=110,y=205)
user_entry.insert(0,"youremail@domain.com")
pass_entry = Entry(width=20)
pass_entry.place(x=110,y=230)





#Labels

main_title = Label(text="Pasword Manager",font=("Arial", 14, "bold"))
main_title.place(x=105,y=0)

website_label = Label(text="Website:",font=("Arial", 8, "bold"))
website_label.place(x=35,y=180)

username_label = Label(text="Email/Username:",font=("Arial", 8, "bold"))
username_label.place(x=10,y=205)

pass_label = Label(text="Password:",font=("Arial", 8, "bold"))
pass_label.place(x=30,y=230)

window.mainloop()

