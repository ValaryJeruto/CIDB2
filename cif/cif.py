import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pymysql

# window size
window = tkinter.Tk()
window.geometry("1400x2400")
window.title("Case Investigation Form for covid-19")
window.resizable(0, 0)

# frame
frame = Frame(window, width=2500, height=2500, bg='black', bd=1)
frame.grid(row=0, column=0)
frame.pack()

import sqlite3


def submit():
    if FirstName_entry.get() == '':
        messagebox.showerror('Alert', 'please enter your First Name')
    elif SecondName_entry.get() == '':
        messagebox.showerror('Alert', 'please enter your second name')
    elif IdBirtCertNo_entry.get() == '':
        messagebox.showerror('Alert', 'please enter your ID Number')
    elif PhoneNumber_entry.get() == '':
        messagebox.showerror('Alert', 'please enter your Phone Number')
    elif CountyOfResidence_entry.get() == '':
        messagebox.showerror('Alert', 'please enter your Country')
    elif SubCounty_entry.get() == '':
        messagebox.showerror('Alert', 'please enter your sub_county')
    elif Ward_entry.get() == '':
        messagebox.showerror('Alert', 'please enter your ward')
    elif Village_entry.get() == '':
        messagebox.showerror('Alert', 'please enter your Residential')

    elif YearOfBirth_entry.get() == '':
        messagebox.showerror('Alert', 'please enter your Date of Birth')
    elif EmailAddress_entry.get() == '':
        messagebox.showerror('Alert', 'please enter your Email')
    elif TestStatus_combobox_entry.get() == '':
        messagebox.showerror('Alert', 'please select your test')
    elif ReasonForTesting_combobox_entry.get() == '':
        messagebox.showerror('Alert', 'please give your reason ')
    elif Vaccination_combobox_entry.get() == '':
        messagebox.showerror('Alert', 'This is required')
    elif SexAtBirth_combobox_entry.get() == '':
        messagebox.showerror('Alert', 'please select your sex at birth ')
    else:
        db = pymysql.connect(host='127.0.0.1', user='root', password='Jakakiimba9#', database='case_ivestication_db')
        cur = db.cursor()
        try:
            query = 'create database case_ivestication_db if not exist '
            cur.execute(query)
            query = 'use case_ivestication_db'
            cur.execute(query)

            query = 'create table personal_information ( FirstName VARCHAR(10) NOT NULL,SecondName VARCHAR(10) NOT ' \
                    'NULL,' \
                    ' IdBirtCertNo INT NOT NULL,PhoneNumber INT NULL DEFAULT NULL,' \
                    'CountyOfResidence VARCHAR(15) NULL DEFAULT NULL,SubCounty VARCHAR(15) NULL DEFAULT NULL,' \
                    ' Ward VARCHAR(15) NULL DEFAULT NULL, Village VARCHAR(20) NULL DEFAULT NULL,' \
                    'YearOfBirth INT NULL DEFAULT NULL, EmailAddress VARCHAR(30) NULL DEFAULT NULL,' \
                    'TestStatus` VARCHAR(6) NULL DEFAULT NULL,ReasonForTesting VARCHAR(15) NULL DEFAULT NULL,' \
                    ' Vaccination VARCHAR(3) NULL DEFAULT NULL,SexAtBirth VARCHAR(6) NULL DEFAULT NULL,' \
                    'PRIMARY KEY (`IdBirtCertNo`))'
            cur.execute(query)
            messagebox.showinfo('success', 'fields created successfully')
        except:
            cur.execute('use case_ivestication_db')
            query = 'insert into personal_information(FirstName,SecondName,IdBirtCertNo, PhoneNumber, ' \
                    'CountyOfResidence,' \
                    'SubCounty, Ward ,Village,YearOfBirth, EmailAddress , TestStatus, ReasonForTesting, Vaccination , ' \
                    'SexAtBirth) ' \
                    'VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
            cur.execute(query, (
                FirstName_entry.get(), SecondName_entry.get(), IdBirtCertNo_entry.get(), PhoneNumber_entry.get(),
                CountyOfResidence_entry.get(), SubCounty_entry.get(),
                Ward_entry.get(), Village_entry.get(), YearOfBirth_entry.get(), EmailAddress_entry.get(),
                TestStatus_combobox_entry.get(), ReasonForTesting_combobox_entry.get(),
                Vaccination_combobox_entry.get(), SexAtBirth_combobox_entry.get()))
            db.commit()
            db.cursor()
            messagebox.showinfo('success', 'successfully submitted')

    # FName = FirstName_entry.get()
    # SName = SecondName_entry.get()
    # ID_No = IdBirtCertNo_entry.get()
    # Phone_no = PhoneNumber_entry.get()
    # County = CountyOfResidence_entry.get()
    # Sub_County = SubCounty_entry.get()
    # Ward = Ward_entry.get()


# Residence = Village_entry.get()
# Dob = YearOfBirth_entry.get()
# Email = EmailAddress_entry.get()
# Test = TestStatus_combobox_entry.get()
# Reason = ReasonForTesting_combobox_entry.get()
# Vaccinated = Vaccination_combobox_entry.get()
# Sex = SexAtBirth_combobox_entry.get()

# print("FName:", FirstName, "SName:", SecondName, "ID_No:", IdBirtCertNo, "Phone_no:", PhoneNumber, "County :",
#     CountyOfResidence, "SubCounty:", SubCounty, "Ward :", Ward, "Residence :", Village, "Dob:",
#     YearOfBirth, "Email:", EmailAddress, "Test:", TestStatus, "Reason:",
#   ReasonForTesting, "Vaccinated:", Vaccination, "Sex:", SexAtBirth)


# selection01;personal information

user_info_frame = tkinter.LabelFrame(frame, text="personal information", fg='#97ffff', bg='black',
                                     font="calibre 15 bold")
user_info_frame.grid(row=0, column=0)

FirstName = tkinter.Label(user_info_frame, text="FIRST NAME:", fg='#97ffff', bg='black', font=('calibre', 8, 'bold'))
FirstName.grid(row=1, column=1)
FirstName_entry = tkinter.Entry(user_info_frame)
FirstName_entry.grid(row=1, column=2)

SecondName = tkinter.Label(user_info_frame, text="SECOND NAME:", fg='#97ffff', bg='black', font=('calibre', 8, 'bold'))
SecondName.grid(row=2, column=1)
SecondName_entry = tkinter.Entry(user_info_frame)
SecondName_entry.grid(row=2, column=2)

IdBirtCertNo = tkinter.Label(user_info_frame, text="ID/BIRTH CERT No.:", fg='#97ffff', bg='black',
                             font=('calibre', 10, 'bold'))
IdBirtCertNo.grid(row=3, column=1)
IdBirtCertNo_entry = tkinter.Entry(user_info_frame)
IdBirtCertNo_entry.grid(row=3, column=2)

PhoneNumber = tkinter.Label(user_info_frame, text="PHONE No.:", fg='#97ffff', bg='black', font=('calibre', 8, 'bold'))
PhoneNumber.grid(row=4, column=1)
PhoneNumber_entry = tkinter.Entry(user_info_frame)
PhoneNumber_entry.grid(row=4, column=2)

CountyOfResidence = tkinter.Label(user_info_frame, text="COUNTY:", fg='#97ffff', bg='black',
                                  font=('calibre', 8, 'bold'))
CountyOfResidence.grid(row=1, column=3)
CountyOfResidence_entry = tkinter.Entry(user_info_frame)
CountyOfResidence_entry.grid(row=1, column=4)

SubCounty = tkinter.Label(user_info_frame, text="SUB-COUNTY:", fg='#97ffff', bg='black',
                          font=('calibre', 10, 'bold'))
SubCounty.grid(row=2, column=3)
SubCounty_entry = tkinter.Entry(user_info_frame)
SubCounty_entry.grid(row=2, column=4)

Ward = tkinter.Label(user_info_frame, text="WARD:", fg='#97ffff', bg='black', font=('calibre', 10, 'bold'))
Ward.grid(row=3, column=3)
Ward_entry = tkinter.Entry(user_info_frame)
Ward_entry.grid(row=3, column=4)

Village = tkinter.Label(user_info_frame, text="Village:", fg='#97ffff', bg='black', font=('calibre', 10, 'bold'))
Village.grid(row=5, column=1)
Village_entry = tkinter.Entry(user_info_frame)
Village_entry.grid(row=5, column=2)


YearOfBirth = tkinter.Label(user_info_frame, text="Year of Birth:", fg='#97ffff', bg='black',
                            font=('calibre', 10, 'bold'))
YearOfBirth.grid(row=6, column=1)
YearOfBirth_entry = tkinter.Entry(user_info_frame)
YearOfBirth_entry.grid(row=6, column=2)

EmailAddress = tkinter.Label(user_info_frame, text="EMAIL:", fg='#97ffff', bg='black', font=('calibre', 10, 'bold'))
EmailAddress.grid(row=7, column=1)
EmailAddress_entry = tkinter.Entry(user_info_frame)
EmailAddress_entry.grid(row=7, column=2)

TestStatus = tkinter.Label(user_info_frame, text="TEST:", fg='#97ffff', bg='black', font=('calibre', 10, 'bold'))
TestStatus_combobox_entry = ttk.Combobox(user_info_frame, values=["intial", "repeat"])
TestStatus.grid(row=4, column=3)
TestStatus_combobox_entry.grid(row=4, column=4)

ReasonForTesting = tkinter.Label(user_info_frame, text="REASON:", fg='#97ffff', bg='black',
                                 font=('calibre', 10, 'bold'))
ReasonForTesting_combobox_entry = ttk.Combobox(user_info_frame,
                                               values=["Air travel", "Surveillance", "Truck drive", "Other"])
ReasonForTesting.grid(row=5, column=3)
ReasonForTesting_combobox_entry.grid(row=5, column=4)

Vaccination = tkinter.Label(user_info_frame, text="VACCINATED:", fg='#97ffff', bg='black', font=('calibre', 10, 'bold'))
Vaccination_combobox_entry = ttk.Combobox(user_info_frame, values=["Yes", "No"])
Vaccination.grid(row=6, column=3)
Vaccination_combobox_entry.grid(row=6, column=4)

SexAtBirth = tkinter.Label(user_info_frame, text="SEX AT BIRTH:", fg='#97ffff', bg='black',
                           font=('calibre', 10, 'bold'))
SexAtBirth_combobox_entry = ttk.Combobox(user_info_frame, values=["Male", "Female"])
SexAtBirth.grid(row=7, column=3)
SexAtBirth_combobox_entry.grid(row=7, column=4)

lbl4 = Button(user_info_frame, text="Submit", command=submit, width=10, borderwidth=3, height=1, fg='white',
              bg='#7f7fff',
              cursor='hand2', border=2, font=('#57a1f8', 10, 'bold'))
lbl4.grid(row=8, column=0)

for widget in user_info_frame.winfo_children():
    widget.grid_configure(padx=10, pady=10)

# selection02; clinical information
clinic_info_frame = tkinter.LabelFrame(frame, text="clinical information", fg='#97ffff', bg='black',
                                       font="calibre 20 bold")
clinic_info_frame.grid(row=1, column=1, sticky="news", padx=5, pady=5)

lbl4 = tkinter.Label(clinic_info_frame, text="Patient clinical course", fg='#97ffff', bg='black',
                     font=('calibre', 10, 'bold'))
lbl4.grid(row=1, column=1)
lbl4_combobox = ttk.Combobox(clinic_info_frame, values=["Asymptomatic", "Symptomatic", "Unknown"])
lbl4_combobox.grid(row=1, column=3)

lbl5 = tkinter.Label(clinic_info_frame, text="Ventilated", fg='#97ffff', bg='black', font=('calibre', 10, 'bold'))
lbl5_combobox = ttk.Combobox(clinic_info_frame, values=["Yes", "No"])
lbl5.grid(row=2, column=1)
lbl5_combobox.grid(row=2, column=3)

lbl6 = tkinter.Label(clinic_info_frame, text="Health Status", fg='#97ffff', bg='black', font=('calibre', 10, 'bold'))
lbl6_combobox = ttk.Combobox(clinic_info_frame, values=["Stable", "Severely ill", "Dead"])
lbl6.grid(row=3, column=1)
lbl6_combobox.grid(row=3, column=3)

lbl6 = tkinter.Label(clinic_info_frame, text="Patient symptoms (Number all selected symptoms)", fg='#97ffff',
                     bg='black', font=('calibre', 10, 'bold'))
lbl6.grid(row=4, column=1)

lbl7 = tkinter.Label(clinic_info_frame, text="Patient signs (Number all reported signs)", fg='#97ffff', bg='black',
                     font=('calibre', 10, 'bold'))
lbl7.grid(row=5, column=1)

lbl8 = tkinter.Label(clinic_info_frame, text="Temperature\n( in degrees celsius)", fg='#97ffff', bg='black',
                     font=('calibre', 10, 'bold'))
lbl8.grid(row=6, column=1)
lbl8 = tkinter.Entry(clinic_info_frame)
lbl8.grid(row=6, column=3, )

lbl9 = Button(clinic_info_frame, text="Enter", command=submit, width=10, borderwidth=3, height=1, fg='white',
              bg='#7f7fff',
              cursor='hand2', border=2, font=('#57a1f8', 10, 'bold'))
lbl9.grid(row=7, column=0)

for widget in clinic_info_frame.winfo_children():
    widget.grid_configure(padx=5, pady=5)

# selection03; Exposure and travel information in 14 days prior to symptoms.

exp_trav_info = tkinter.LabelFrame(frame, text="Exposure and travel information", fg='#97ffff', bg='black',
                                   font="calibre 20 bold")
exp_trav_info.grid(row=1, column=0, sticky="news", padx=5, pady=5)

llb1 = tkinter.Label(exp_trav_info, text="Occupation\n (Number any that apply)", fg='#97ffff', bg='black',
                     font=('calibre', 10, 'bold'))
llb1.grid(row=2, column=1)

llb2 = tkinter.Label(exp_trav_info, text="Travelled\n 1. yes(specify) \n 2. No", fg='#97ffff', bg='black',
                     font=('calibre', 10, 'bold'))
llb2.grid(row=3, column=1)
llb2 = tkinter.Entry(exp_trav_info)
llb2.grid(row=3, column=2)

llb3 = tkinter.Label(exp_trav_info, text="Visited any health facility(ies)", fg='#97ffff', bg='black',
                     font=('calibre', 10, 'bold'))
llb3.grid(row=4, column=1)
llb3_combobox = ttk.Combobox(exp_trav_info, values=["Yes", "No"])
llb3_combobox.grid(row=4, column=2)

llb4 = tkinter.Label(exp_trav_info, text="Had close contact with an cute respiratory infected person", fg='#97ffff',
                     bg='black', font=('calibre', 10, 'bold'))
llb4.grid(row=5, column=1)
llb4_combobox = ttk.Combobox(exp_trav_info, values=["Unknown", "No", "Yes"])
llb4_combobox.grid(row=5, column=2)

llb5 = tkinter.Label(exp_trav_info, text="Had contact with a probable confirmed case", fg='#97ffff', bg='black',
                     font=('calibre', 10, 'bold'))
llb5.grid(row=6, column=1)
llb5_combobox = ttk.Combobox(exp_trav_info, values=["Unknown", "No", "Yes"])
llb5_combobox.grid(row=6, column=2)

llb6 = tkinter.Label(exp_trav_info, text="Visited any live animal markets", fg='#97ffff', bg='black',
                     font=('calibre', 10, 'bold'))
llb6.grid(row=7, column=1)
llb6_combobox = ttk.Combobox(exp_trav_info, values=["Unknown", "No", "Yes"])
llb6_combobox.grid(row=7, column=2)

lbl9 = Button(exp_trav_info, text="Submit", command=submit, width=10, borderwidth=3, height=1, fg='white', bg='#7f7fff',
              cursor='hand2', border=2, font=('#57a1f8', 10, 'bold'))
lbl9.grid(row=7, column=0)

for widget in exp_trav_info.winfo_children():
    widget.grid_configure(padx=5, pady=5)

# section 04; Laboratory information

lab_info = tkinter.LabelFrame(frame, text="Laboratory information", fg='#97ffff', bg='black', font="calibre 10 bold")
lab_info.grid(row=0, column=1, sticky="news", padx=5, pady=5)

lb51 = tkinter.Label(lab_info, text="Specimen collection\n (To be completed by the health facility)", fg='#97ffff',
                     bg='black', font=('calibre', 10, 'bold'))
lb51.grid(row=0, column=0)
lb51 = tkinter.Label(lab_info, text="was the specimen collected", fg='white', bg='black', font=('#57a1f8', 10, 'bold'))
lb51.grid(row=0, column=1)
lb51_combobox = ttk.Combobox(lab_info, values=["No", "Yes"])
lb51_combobox.grid(row=0, column=2)

lb52 = tkinter.Label(lab_info, text="Date of specimen collection\n (DD/MM/YY)", fg='white', bg='black',
                     font=('#57a1f8', 10, 'bold'))
lb52.grid(row=1, column=1)
lb52 = tkinter.Entry(lab_info)
lb52.grid(row=1, column=2)

lb53 = tkinter.Label(lab_info, text="specimen type", fg='white', bg='black', font=('#57a1f8', 10, 'bold'))
lb53.grid(row=2, column=1)
lb53_combobox = ttk.Combobox(lab_info,
                             values=["NP Swap", "OP Swap", "Serum Tracheal aspirate", "other specify", "Serum",
                                     "Sputum"])
lb53_combobox.grid(row=2, column=2)

lb54 = tkinter.Label(lab_info, text="Date specimen sent to the lab\n (DD/MM/YY)", fg='white', bg='black',
                     font=('#57a1f8', 10, 'bold'))
lb54.grid(row=3, column=1)
lb54 = tkinter.Entry(lab_info)
lb54.grid(row=3, column=2)

lb55 = tkinter.Label(lab_info, text="To be completed by the confirming lab\n (Number any that apply)", fg='#97ffff',
                     bg='black', font=('calibre', 10, 'bold'))
lb55.grid(row=7, column=0)

lb56 = tkinter.Label(lab_info, text="Name of confirming lab", fg='white', bg='black', font=('#57a1f8', 10, 'bold'))
lb56.grid(row=7, column=1)
lb56 = tkinter.Entry(lab_info)
lb56.grid(row=7, column=2)

lb57 = tkinter.Label(lab_info, text="Assay used", fg='white', bg='black', font=('#57a1f8', 10, 'bold'))
lb57.grid(row=8, column=1)
lb57 = tkinter.Entry(lab_info)
lb57.grid(row=8, column=2)

lb58 = tkinter.Label(lab_info, text="sequencing done", fg='white', bg='black', font=('#57a1f8', 10, 'bold'))
lb58.grid(row=9, column=1)
lb58_combobox = ttk.Combobox(lab_info, values=["Yea", "No", "Unknown"])
lb58_combobox.grid(row=9, column=2)

lb59 = tkinter.Label(lab_info, text="Preliminary lab results", fg='white', bg='black', font=('#57a1f8', 10, 'bold'))
lb59.grid(row=10, column=1)
lb59 = tkinter.Entry(lab_info)
lb59.grid(row=10, column=2)

lb60 = tkinter.Label(lab_info, text="Date of laboratory confirmation\n(DD/MM/YY)", fg='white', bg='black',
                     font=('#57a1f8', 10, 'bold'))
lb60.grid(row=11, column=1)
lb60 = tkinter.Entry(lab_info)
lb60.grid(row=11, column=2)

lbl9 = Button(lab_info, text="Submit", command=submit, width=10, borderwidth=3, height=1, fg='white', bg='#7f7fff',
              cursor='hand2', border=2, font=('#57a1f8', 10, 'bold'))
lbl9.grid(row=11, column=0)

for widget in lab_info.winfo_children():
    widget.grid_configure(padx=5, pady=5)

window.mainloop()
