from tkinter import *
from random import randint
import random
import pyperclip

root = Tk()
root.title("Password Generator Tool")
root.configure(background="black")
root.geometry("600x300+660+390")
root.resizable(False, False) #Making program un-resizable. 

def generatePassword():

    specialCharacters = '~`!@#$%^&*()-_+={}[]|\;:"<>,./?' #Defining special character string
    
    textField.config(state=NORMAL) #Changing text field state.

    global password #Declaring global password variable
    password = ""
    
    for i in range(5):
        i = chr(randint(65, 90))
        for x in range(5):
            x = chr(randint(65,90)).lower()

        password = str(password) + i + x 

    password = password + str(randint(65,90)) + specialCharacters[random.randint(0,30)]

    textField.delete(1.0, END)
    textField.config(state=NORMAL) #Changing text field state.
    textField.insert(END, password) # Inserting generated password value.
    textField.config(state=DISABLED) # Changing text field state.


def copyPassword():
    try:
        pyperclip.copy(password) #Copies value of password var to windows clipboard.
    except:
        print("Variable not yet defined")

    
programLbl = Label(text = "Password Generator Tool", font = ("Arial", 20), bg="black", fg="white")
programLbl.pack(pady=5)

generatePassButton = Button(root, text="CLICK TO GENERATE SECURE PASSWORD", background = "white", command = generatePassword)
generatePassButton.pack(pady=20)

textField = Text(root, width=60, height=2.5)
textField.pack(pady=25)
textField.config(state=DISABLED)

copyPassBtn = Button(root, text="Copy password to Clipboard", bg ="white", command= copyPassword)
copyPassBtn.pack(pady=20)

root.mainloop()
