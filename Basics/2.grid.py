from tkinter import *

root = Tk()

#creating a label Widget
mylabel1 = Label(root, text="Hello World")
mylabel2 = Label(root, text="My name is Gangadhar Bhuvan")



#Shoving it onto the screen
mylabel1.grid(row=0, column=1)
mylabel2.grid(row=1, column=2)


##################################################
# We can do this in 1 Line
'''

mylabel1 = Label(root, text="Hello World").grid(row=0, column=1)
mylabel2 = Label(root, text="My name is Gangadhar Bhuvan").grid(row=1, column=2)

'''

root.mainloop()