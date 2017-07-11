__Author__ = Olaitan 
from tkinter import *
import backend

root = Tk()
gp = backend.GP()

def add_button():
    gp.add(course_text.get(),grade_text.get(),int(unit_text.get()))
    list1.insert(END,("Course-- {}   Grade-- {}  unit-- {}".format(course_text.get(),grade_text.get(),unit_text.get())))
    course_entry.delete(0,END)
    grade_entry.delete(0, END)
    unit_entry.delete(0, END)

def calculate_button():
    cgpa = gp.calculate()
    #list1.delete(0,END)
    # list1.insert(END,("YOUR CGPA IS {}".format(cgpa)))
    print(cgpa)
    
    lab= Label(root, text ="YOUR CGPA IS %.2f"%(cgpa))
    lab.grid(row=5, column=0)

def new_button():
    gp.new()
    list1.delete(0,END)



#labels
course_label = Label(root, text="course code")
course_label.grid(row=0, column=0)

grade_label = Label(root, text= "Grade")
grade_label.grid(row=2, column=0)

unit_label = Label(root, text="unit")
unit_label.grid(row=4, column=0)

#entries
course_text = StringVar()
course_entry = Entry(root,textvariable=course_text)
course_entry.grid(row=0, column=1)

grade_text = StringVar()
grade_entry = Entry(root, textvariable=grade_text)
grade_entry.grid(row=2, column=1)

unit_text =StringVar()
unit_entry = Entry(root, textvariable=unit_text)
unit_entry.grid(row=4, column=1)

#listbox
list1 = Listbox(root, height= 8, width=40)
list1.grid(row = 6, column = 0, columnspan=2)

scroll = Scrollbar(root)
scroll.grid(row=6, column=3, rowspan=8)

list1.configure(yscrollcommand=scroll.set)
scroll.configure(command=list1.yview,)

#buttons
b1 = Button(root, text="add entry", command=add_button)
b1.grid(row=0, column=7)

b2 = Button(root, text="calculate GP", command=calculate_button)
b2.grid(row=2, column=7)

b3 = Button(root, text="start new", command=new_button)
b3.grid(row=4, column=7)

root.mainloop()
