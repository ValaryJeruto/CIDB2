import tkinter
from tkinter import*

window = tkinter.Tk()
window.geometry("800x800")
window.title("Case Investigation Form for covid-19")
frame = tkinter.Frame(window)
frame.pack()

#selection01;personal information
user_info_frame = tkinter.LabelFrame(frame, text="personal information", font="ar 10 bold")
user_info_frame.grid(row=0, column=1)

lb0 = tkinter.Label(user_info_frame, text="NAME")
lb0.grid(row=1, column=1)
lb0 = tkinter.Entry(user_info_frame)
lb0.grid(row=1,column=2)

lb1 = tkinter.Label(user_info_frame, text="ID/BIRTH CERT No.")
lb1.grid(row=2, column=2)
lb1 = tkinter.Entry(user_info_frame)
lb1.grid(row=2,column=2)

lb2 = tkinter.Label(user_info_frame, text="PHONE No.")
lb2.grid(row=3, column=1)
lb2 = tkinter.Entry(user_info_frame)
lb2.grid(row=3,column=2)

lb3 = tkinter.Label(user_info_frame, text="COUNTRY")
lb3.grid(row=4, column=1)
lb3 = tkinter.Entry(user_info_frame)
lb3.grid(row=4,column=2)

lb4 = tkinter.Label(user_info_frame, text="SUB-COUNTRY")
lb4.grid(row=5, column=1)
lb4 = tkinter.Entry(user_info_frame)
lb4.grid(row=5,column=2)

lb5 = tkinter.Label(user_info_frame, text="WARD")
lb5.grid(row=6, column=1)
lb5 = tkinter.Entry(user_info_frame)
lb5.grid(row=6,column=2)

lb6 = tkinter.Label(user_info_frame, text="RESIDENCE")
lb6.grid(row=7, column=1)
lb6 = tkinter.Entry(user_info_frame)
lb6.grid(row=7,column=2)

lb7 = tkinter.Label(user_info_frame, text="AGE")
lb7.grid(row=8, column=1)
lb7 = tkinter.Entry(user_info_frame)
lb7.grid(row=8,column=2)

lb8 = tkinter.Label(user_info_frame, text="DATE OF BIRTH")
lb8.grid(row=9, column=1)
lb8 = tkinter.Entry(user_info_frame)
lb8.grid(row=9,column=2)

lb9 = tkinter.Label(user_info_frame, text="EMAIL")
lb9.grid(row=10, column=1)
lb9 = tkinter.Entry(user_info_frame)
lb9.grid(row=10,column=2)

lbl1 = tkinter.Label(user_info_frame, text="TEST")
lbl1.grid(row=1, column=3)






window.mainloop()