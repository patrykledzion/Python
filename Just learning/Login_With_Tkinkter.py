import customtkinter as ctk

global login_input
global pass_input


ctk.set_appearance_mode("system")
ctk.set_default_color_theme("green")

root = ctk.CTk()
root.geometry("500x300")


def getLoginDataFromFile(filename):
    f = open(filename, "r")
    return f.readline().strip(), f.readline().strip()


def login():
    login = login_input.get()
    password = pass_input.get()

    filelogin, filepassword = getLoginDataFromFile("login.txt")
    if login == filelogin and password == filepassword:
        print("Logged in")
    else:
        print("Not logged in")


def UI():
    global login_input
    global pass_input

    frame = ctk.CTkFrame(master=root)
    frame.pack(pady=20, padx=60, fill="both", expand="True")

    label = ctk.CTkLabel(master=frame, text="Login system", font=("poppins", 20))
    label.pack(pady=12, padx=10)

    login_input = ctk.CTkEntry(master=frame, placeholder_text="Username")
    login_input.pack(pady=12, padx=10)

    pass_input = ctk.CTkEntry(master=frame, placeholder_text="Password", show="*")
    pass_input.pack(pady=12, padx=10)

    button = ctk.CTkButton(master=frame, text="Login", command=login)
    button.pack(pady=12, padx=10)


    root.mainloop()


UI()
