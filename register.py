from tkinter import *
import os

def register_user():
  username_info = username.get()
  password_info = password.get()

  file = open(username_info, "w")
  file.write(username_info+"\n")
  file.write(password_info)
  file.close()

  # Clears inputs after registration
  username_entry.delete(0, END)
  password_entry.delete(0, END)

  Label(screen1, text = "Registration Successful!", fg = "green", font = ("calibri", 11)).pack()

def register():
  global screen1
  global username
  global password
  global username_entry
  global password_entry
  screen1 = Toplevel(screen)
  screen1.title("Register")
  screen1.geometry("400x300")

  username = StringVar()
  password = StringVar()

  Label(screen1, text = "Please enter details below").pack()
  Label(screen1, text = "").pack()
  
  Label(screen1, text = "Username *").pack()
  
  username_entry = Entry(screen1, textvariable = username)
  username_entry.pack()  
  
  Label(screen1, text = "Password *").pack()  
  password_entry = Entry(screen1, textvariable = password)
  password_entry.pack()
  Label(screen1, text = "").pack()  
  Button(screen1, text = "Register", width = 10, height = 1, command = register_user).pack()

def delete2():
  screen3.destroy()

def delete3():
  screen4.destroy()
  
def delete4():
  screen5.destroy()

def saved():
  screen8 = Toplevel(screen) 
  screen8.title("Saved")
  screen8.geometry("200x200")
  Label(screen8, text = "Note saved successfully!").pack()

def save():
  filename = raw_filename.get()
  notes = raw_notes.get()

  # intentionally no extension set so you wont be able to easily open notes outside of the program
  data = open(filename, "w")
  data.write(notes)
  data.close()

  saved()

def delete_note1():
  filename3 = raw_filename2.get()
  # deletes note file
  os.remove(filename3)
  screen12 = Toplevel(screen) 
  screen12.title("Notes")
  screen12.geometry("400x400")
  
  Label(screen12, text = filename3 + " removed").pack()



def delete_note():
  global raw_filename2
  raw_filename2 = StringVar()

  screen11 = Toplevel(screen) 
  screen11.title("View Notes")
  screen11.geometry("400x400")

  Label(screen11, text = "Use one of the files below to view notes:").pack()  
  all_files = os.listdir()
  Label(screen11, text = all_files).pack()
  Entry(screen11, textvariable = raw_filename2).pack()
  Label(screen7, text = "").pack()
  Button(screen11, command = delete_note1, text = "Ok").pack()

def view_notes1():
  filename1 = raw_filename1.get()
  data = open(filename1, "r")
  data1 = data.read()

  screen10 = Toplevel(screen) 
  screen10.title("Notes")
  screen10.geometry("400x400")
  
  Label(screen10, text = data1).pack()
  Label(screen10, text = all_files).pack()
  

def view_notes():
  global raw_filename1

  screen9 = Toplevel(screen) 
  screen9.title("View Notes")
  screen9.geometry("400x400")

  Label(screen9, text = "Use one of the files below to view notes:").pack()  
  all_files = os.listdir()
  Label(screen9, text = all_files).pack()
  raw_filename1 = StringVar()
  Entry(screen9, textvariable = raw_filename1).pack()
  Label(screen9, text = "").pack()
  Button(screen9, command = view_notes1, text = "Ok").pack()


def create_notes():
  global raw_filename
  raw_filename = StringVar()
  global raw_notes
  raw_notes = StringVar()

  screen7 = Toplevel(screen) 
  screen7.title("Info")
  screen7.geometry("400x400")
  Label(screen7, text = "Please enter a note file name below:").pack()
  Entry(screen7, textvariable = raw_filename).pack()
  Label(screen7, text = "").pack()
  Label(screen7, text = "Please enter your note below:").pack()
  Entry(screen7, textvariable = raw_notes).pack()
  Label(screen7, text = "").pack()
  Button(screen7, text = "Save", command = save).pack()
  

def session():
  screen6 = Toplevel(screen) 
  screen6.title("Dashboard")
  screen6.geometry("500x400")
  Label(screen6, text = "Welcome to the main dashboard!").pack()
  Label(screen6, text = "").pack()
  Button(screen6, text = "Create Notes", command = create_notes).pack()
  Label(screen6, text = "").pack()
  Button(screen6, text = "View Notes", command = view_notes).pack()
  Label(screen6, text = "").pack()
  Button(screen6, text = "Delete Note", command = delete_note).pack()

def login_success():
  session()
  
def incorrect_password():
  global screen4

  screen4 = Toplevel(screen)
  screen4.title("Denied!")
  screen4.geometry("400x300")

  Label(screen4, text = "Password not recognized!").pack()
  Button(screen4, text = "OK", command = delete3).pack()

def user_not_found():
  global screen5
  
  screen5 = Toplevel(screen)
  screen5.title("Not found!")
  screen5.geometry("400x300")
  
  Label(screen5, text = "User not found!").pack()
  Button(screen5, text = "OK", command = delete4).pack()


def login_verify():
  username1 = username_verify.get()
  password1 = password_verify.get()
  # Clears inputs after registration
  username_entry1.delete(0, END)
  password_entry1.delete(0, END)
  
  list_of_files = os.listdir()
  if username1 in list_of_files:
    file1 = open(username1, "r")
    # Ignores \n etc. 
    verify = file1.read().splitlines()
    if password1 in verify:
      login_success()
    else:
      incorrect_password()
  else:
    user_not_found()
  


def login():
  global screen2
  global username_verify
  global password_verify
  global username_entry1
  global password_entry1

  username_verify = StringVar()
  password_verify = StringVar()

  screen2 = Toplevel(screen)
  screen2.title("Login")
  screen2.geometry("400x300")
  
  Label(screen2, text = "Please enter login details below").pack()
  Label(screen2, text = "").pack()
  

  
  Label(screen2, text = "Username * ").pack()
  username_entry1 = Entry(screen2, textvariable = username_verify)
  username_entry1.pack()  
  
  Label(screen2, text = "").pack()
  
  Label(screen2, text = "Password * ").pack()  
  password_entry1 = Entry(screen2, textvariable = password_verify)
  password_entry1.pack()
  Label(screen2, text = "").pack()

  Button(screen2, text = "Login", width = 12, height = 1, command = login_verify).pack()

def main_screen():
  global screen

  screen = Tk()
  screen.geometry("400x300")
  screen.title("Notes 1.0")

  Label(text = "Notes 1.0", bg = "grey", width = "400", height = "2", font = ("Calibri", 14)).pack()
  Label(text = "").pack()
  Button(text = "Login", height = "2", width = "30", command = login).pack()
  Label(text = "").pack()
  Button(text = "Register", height = "2", width = "30", command = register).pack()

  screen.mainloop()

main_screen() 