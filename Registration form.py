# GUI- Graphical User Interface
from tkinter import *
root = Tk()
root.geometry("500x300")
root.config(background="#5902EC")
def submit_value():
    print("Your information has been saved sucessfully")


Label(root, text="School Registration Form",font="times 18 bold").grid(row=0,column=3)

name_user = Label(root,text="Student's Name")
name_user.grid(row=1, column=2)
class_user = Label(root, text="Class")
class_user.grid(row=2, column=2)
gender_user = Label(root, text="Gender_")
gender_user.grid(row=3, column=2)
phone_user = Label(root, text="Contact no")
phone_user.grid(row=4, column=2)
country_user = Label(root, text="State of Origin")
country_user.grid(row=5, column=2)
address_user = Label(root, text="Place of Residence")
address_user.grid(row=6, column=2)


name_value = StringVar
class_value = StringVar
gender_value = StringVar
phone_value = StringVar
country_value = StringVar
address_value = StringVar
check_value = IntVar

name_box = Entry(root, textvariable = name_value) 
name_box.grid(row=1, column=3)
class_box = Entry(root, textvariable = class_value) 
class_box.grid(row=2, column=3) 
gender_box = Entry(root, textvariable = gender_value) 
gender_box.grid(row=3, column=3)
phone_box = Entry(root, textvariable = phone_value) 
phone_box.grid(row=4, column=3)
country_box = Entry(root, textvariable = country_value) 
country_box.grid(row=5, column=3)
address_box = Entry(root, textvariable = address_value) 
address_box.grid(row=6, column=3)


check_box = Checkbutton(text = "Remember me?", variable=check_value)
check_box.grid(row=7, column=3)

Button(text="Submit", command=submit_value).grid(row=8, column=3)

root.mainloop()

