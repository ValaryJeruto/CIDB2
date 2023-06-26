from tkinter import*
root = Tk()
root.geometry("800x800")

Label(root, text="Case Investigation Form for covid-19", font="ar 18 bold").grid(row=0, column=2)

#selection01;personal information

lb0 = Label(root, text="NAME")
lb1 = Label(root, text="ID/BIRTH CERT No.")
lb2 = Label(root, text="PHONE No.")
lb3 = Label(root, text="COUNTRY")
lb4 = Label(root, text="SUB-COUNTRY")
lb5 = Label(root, text="WARD")
lb6 = Label(root, text="RESIDENCE")
lb7 = Label(root, text="AGE")
lb8 = Label(root, text="DATE OF BIRTH(DD/MM/YY)")
lb9 = Label(root, text="EMAIL")


lb0.grid(row=2, column=1)
lb1.grid(row=3, column=1)
lb2.grid(row=4, column=1)
lb3.grid(row=5, column=1)
lb4.grid(row=6, column=1)
lb5.grid(row=7, column=1)
lb6.grid(row=8, column=1)
lb7.grid(row=9, column=1)
lb8.grid(row=10, column=1)
lb9.grid(row=11, column=1)

lb0value = StringVar
lb1value = StringVar
lb2value = StringVar
lb3value = StringVar
lb4value = StringVar
lb5value = StringVar
lb6value = StringVar
lb7value = StringVar
lb8value = StringVar
lb9value = StringVar
checkvalue = IntVar

lb0entry = Entry(root, textvariable =lb0value)
lb1entry = Entry(root, textvariable =lb1value)
lb2entry = Entry(root, textvariable =lb2value)
lb3entry = Entry(root, textvariable =lb3value)
lb4entry = Entry(root, textvariable =lb4value)
lb5entry = Entry(root, textvariable =lb5value)
lb6entry = Entry(root, textvariable =lb6value)
lb7entry = Entry(root, textvariable =lb7value)
lb8entry = Entry(root, textvariable =lb8value)
lb9entry = Entry(root, textvariable =lb9value)

lb0entry.grid(row=2, column=2)
lb1entry.grid(row=3, column=2)
lb2entry.grid(row=4, column=2)
lb3entry.grid(row=5, column=2)
lb4entry.grid(row=6, column=2)
lb5entry.grid(row=7, column=2)
lb6entry.grid(row=8, column=2)
lb7entry.grid(row=9, column=2)
lb8entry.grid(row=10, column=2)
lb9entry.grid(row=11, column=2)



root.mainloop()