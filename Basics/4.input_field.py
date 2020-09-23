from tkinter import *

root = Tk()

input1 = Entry(root)
input1.pack()

#Adding width, fg, bg as parameters
input2 = Entry(root, width=50, bg="blue", fg="white")
input2.pack()

#Changing Border Width
input3 = Entry(root, width=50, borderwidth=5)
input3.pack()

def myClick():
	myLabel1 = Label(root, text="Look! I clicked a Button!")
	myLabel1.pack()

myButton1 = Button(root, text="Click here!", command=myClick)
myButton1.pack()

#Adding get() method
input4 = Entry(root)
input4.pack()

def myClick1():
	myLabel2 = Label(root, text="Hello " + input4.get())
	myLabel2.pack()

myButton2 = Button(root, text="Enter Your Name", command=myClick1)
myButton2.pack()


#insert() method [placeholder]
input5 = Entry(root)
input5.pack()
input5.insert(0, "Enter Your Name")

def myClick2():
	myLabel3 = Label(root, text="Hello " + input5.get())
	myLabel3.pack()

myButton3 = Button(root, text="Enter Your Name", command=myClick2)
myButton3.pack()


root.mainloop() 