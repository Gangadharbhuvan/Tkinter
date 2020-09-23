from tkinter import *

root = Tk()

myButton1 = Button(root, text="Click here!")
myButton1.pack()



#To Disable the Button
myButton2 = Button(root, text="Click Me!", state=DISABLED)
myButton2.pack()


#To change Size

#for X and Y
myButton3 = Button(root,text="Click the link!", padx=50,pady=50)
myButton3.pack()


#Defining own Function 
def myClick():
	myLabel = Label(root, text="Look! I clicked a Button!")
	myLabel.pack()

myButton4 = Button(root, text="Click here!", command=myClick)
myButton4.pack()

#Adding Foreground and Background Color
myButton5 = Button(root, text="Click here!", command=myClick,fg="blue", bg="red")
myButton5.pack()

#We can also use Hex Color Code for fg and bg [like ffffff= white]
myButton6 = Button(root, text="Click here!", command=myClick,fg="blue", bg="#ffffff")
myButton6.pack()






root.mainloop()