import tkinter
from tkinter import*
from tkinter import ttk
window = tkinter.Tk()
window.geometry("1300x10000")
window.title("Case Investigation Form for covid-19")
frame = tkinter.Frame(window)
frame.pack()

from datetime import date
#selection01;personal information
user_info_frame = tkinter.LabelFrame(frame, text="personal information", font="ar 10 bold")
user_info_frame.grid(row=0, column=1)


lb0 = tkinter.Label(user_info_frame, text="NAME")
lb0.grid(row=1, column=1)
lb0 = tkinter.Entry(user_info_frame)
lb0.grid(row=1, column=2, padx=10, pady=10)

lb1 = tkinter.Label(user_info_frame, text="ID/BIRTH CERT No.")
lb1.grid(row=2, column=1)
lb1 = tkinter.Entry(user_info_frame)
lb1.grid(row=2, column=2, padx=10, pady=10, )

lb2 = tkinter.Label(user_info_frame, text="PHONE No.")
lb2.grid(row=3, column=1)
lb2 = tkinter.Entry(user_info_frame)
lb2.grid(row=3, column=2)

lb3 = tkinter.Label(user_info_frame, text="COUNTRY")
lb3.grid(row=1, column=4)
lb3 = tkinter.Entry(user_info_frame)
lb3.grid(row=1, column=5)

lb4 = tkinter.Label(user_info_frame, text="SUB-COUNTRY")
lb4.grid(row=2, column=4)
lb4 = tkinter.Entry(user_info_frame)
lb4.grid(row=2, column=5)

lb5 = tkinter.Label(user_info_frame, text="WARD")
lb5.grid(row=3, column=4)
lb5 = tkinter.Entry(user_info_frame)
lb5.grid(row=3, column=5)

lb6 = tkinter.Label(user_info_frame, text="RESIDENCE")
lb6.grid(row=4, column=1)
lb6 = tkinter.Entry(user_info_frame)
lb6.grid(row=4, column=2)

lb7 = tkinter.Label(user_info_frame, text="AGE")
lbl7_spinbox = tkinter.Spinbox(user_info_frame, from_=0, to=150)
lb7.grid(row=5, column=1)
lbl7_spinbox.grid(row=5, column=2)

lb8 = tkinter.Label(user_info_frame, text="DATE OF BIRTH")
lb8.grid(row=6, column=1)
lb8 = tkinter.Entry(user_info_frame)
lb8.grid(row=6, column=2)

lb9 = tkinter.Label(user_info_frame, text="EMAIL")
lb9.grid(row=7, column=1)
lb9 = tkinter.Entry(user_info_frame)
lb9.grid(row=7, column=2,)

lbl0 = tkinter.Label(user_info_frame, text="TEST")
lbl0_combobox = ttk.Combobox(user_info_frame, values=["initial", "repeat"])
lbl0.grid(row=4, column=4)
lbl0_combobox.grid(row=4, column=5,)

lbl1 = tkinter.Label(user_info_frame, text="REASON")
lbl1_combobox = ttk.Combobox(user_info_frame, values=["Air travel", "Surveillance", "Truck drive", "Other"])
lbl1.grid(row=5, column=4)
lbl1_combobox.grid(row=5, column=5,)

lbl2 = tkinter.Label(user_info_frame, text="VACCINATED")
lbl2_combobox = ttk.Combobox(user_info_frame, values=["Yes", "No"])
lbl2.grid(row=6, column=4)
lbl2_combobox.grid(row=6, column=5,)

lbl3 = tkinter.Label(user_info_frame, text="SEX AT BIRTH")
lbl3_combobox = ttk.Combobox(user_info_frame, values=["Male", "Female"])
lbl3.grid(row=7, column=4)
lbl3_combobox.grid(row=7, column=5,)

for widget in user_info_frame.winfo_children():
    widget.grid_configure(padx=10, pady=10)

#selection02; clinical information
clinic_info_frame = tkinter.LabelFrame(frame, text="clinical information", font="ar 10 bold")
clinic_info_frame.grid(row=0, column=2, sticky="news", padx=10, pady=10)

lbl4 = tkinter.Label(clinic_info_frame, text="Patient clinical course")
lbl4.grid(row=1, column=1)
lbl4_combobox = ttk.Combobox(clinic_info_frame, values=["Asymptomatic", "Symptomatic", "Unknown"])
lbl4_combobox.grid(row=1, column=3)

lbl5 = tkinter.Label(clinic_info_frame, text="Ventilated")
lbl5_combobox = ttk.Combobox(clinic_info_frame, values=["Yes", "No"])
lbl5.grid(row=2, column=1)
lbl5_combobox.grid(row=2, column=3)

lbl6 = tkinter.Label(clinic_info_frame, text="Health Status")
lbl6_combobox = ttk.Combobox(clinic_info_frame, values=["Stable", "Severely ill", "Dead"])
lbl6.grid(row=3, column=1)
lbl6_combobox.grid(row=3, column=3)

lbl6 = tkinter.Label(clinic_info_frame, text="Patient symptoms (Number all selected symptoms)")
lbl6.grid(row=4, column=1)

lbl7 = tkinter.Label(clinic_info_frame, text="Patient signs (Number all reported signs)")
lbl7.grid(row=5, column=1)

lbl8 = tkinter.Label(clinic_info_frame, text="Temperature\n( in degrees celsius)")
lbl8.grid(row=6, column=1)
lbl8 = tkinter.Entry(clinic_info_frame)
lbl8.grid(row=6, column=3,)

lbl9 = tkinter.Label(clinic_info_frame, text="Underlying conditions \n(Number all that apply)")
lbl9.grid(row=7, column=1)

for widget in clinic_info_frame.winfo_children():
    widget.grid_configure(padx=10, pady=8)

#selection03; Exposure and travel information in 14 days prior to sympoms.

exp_trav_info = tkinter.LabelFrame(frame, text="Exposure and travel information", font="ar 10 bold")
exp_trav_info.grid(row=1, column=1, sticky="news", padx=10, pady=8)

llb1 = tkinter.Label(exp_trav_info, text="Occupation\n (Number any that apply)")
llb1.grid(row=2, column=1)

llb2 = tkinter.Label(exp_trav_info, text="Travelled\n 1. yes(specify) \n 2. No")
llb2.grid(row=3, column=1)
llb2 = tkinter.Entry(exp_trav_info)
llb2.grid(row=3, column=2)

llb3 = tkinter.Label(exp_trav_info, text="Visited any health facility(ies)")
llb3.grid(row=4, column=1)
llb3_combobox = ttk.Combobox(exp_trav_info, values=["Yes", "No"])
llb3_combobox.grid(row=4, column=2)

llb4 = tkinter.Label(exp_trav_info, text="Had close contact with an cute respiratory infected person")
llb4.grid(row=5, column=1)
llb4_combobox = ttk.Combobox(exp_trav_info, values=["Unknown", "No", "Yes"])
llb4_combobox.grid(row=5, column=2)

llb5 = tkinter.Label(exp_trav_info, text="Had contact with a probable confirmed case")
llb5.grid(row=6, column=1)
llb5_combobox = ttk.Combobox(exp_trav_info, values=["Unknown", "No", "Yes"])
llb5_combobox.grid(row=6, column=2)

llb6 = tkinter.Label(exp_trav_info, text="Visited any live animal markets")
llb6.grid(row=7, column=1)
llb6_combobox = ttk.Combobox(exp_trav_info, values=["Unknown", "No", "Yes"])
llb6_combobox.grid(row=7, column=2)

for widget in exp_trav_info.winfo_children():
    widget.grid_configure(padx=10, pady=8)

#section 04; Laboratory information

lab_info = tkinter.LabelFrame(frame, text="Laboratory information", font="ar 10 bold")
lab_info.grid(row=1, column=2, sticky="news", padx=10, pady=8)

lb51 = tkinter.Label(lab_info, text="Specimen collection\n (To be completed by the health facility)")
lb51.grid(row=0, column=0)
lb51 = tkinter.Label(lab_info, text="was the specimen collected")
lb51.grid(row=0, column=1)
lb51_combobox = ttk.Combobox(lab_info, values=["No", "Yes"])
lb51_combobox.grid(row=0, column=2)

lb52 = tkinter.Label(lab_info, text="Date of specimen collection\n (DD/MM/YY)")
lb52.grid(row=1, column=1)
lb52 = tkinter.Entry(lab_info)
lb52.grid(row=1, column=2)

lb53 = tkinter.Label(lab_info, text="specimen type")
lb53.grid(row=2, column=1)
lb53_combobox = ttk.Combobox(lab_info, values=["NP Swap", "OP Swap", "Serum Tracheal aspirate", "other specify", "Serum","Sputum"])
lb53_combobox.grid(row=2, column=2)

lb54 = tkinter.Label(lab_info, text="Date specimen sent to the lab\n (DD/MM/YY)")
lb54.grid(row=3, column=1)
lb54 = tkinter.Entry(lab_info)
lb54.grid(row=3, column=2)

lb55 = tkinter.Label(lab_info, text="To be completed by the confirming lab\n (Number any that apply)")
lb55.grid(row=7, column=0)

lb56 = tkinter.Label(lab_info, text="Name of confirming lab")
lb56.grid(row=7, column=1)
lb56 = tkinter.Entry(lab_info)
lb56.grid(row=7, column=2)

lb57 = tkinter.Label(lab_info, text="Assay used")
lb57.grid(row=8, column=1)
lb57 = tkinter.Entry(lab_info)
lb57.grid(row=8, column=2)

lb58 = tkinter.Label(lab_info, text="sequencing done")
lb58.grid(row=9, column=1)
lb58_combobox = ttk.Combobox(lab_info, values=["Yea", "No", "Unknown"])
lb58_combobox.grid(row=9, column=2)

lb59 = tkinter.Label(lab_info, text="Preliminary lab results")
lb59.grid(row=10, column=1)
lb59 = tkinter.Entry(lab_info)
lb59.grid(row=10, column=2)

lb60 = tkinter.Label(lab_info, text="Date of laboratory confirmation\n(DD/MM/YY)")
lb60.grid(row=10, column=1)
lb60 = tkinter.Entry(lab_info)
lb60.grid(row=10, column=2)
checkvalue = IntVar

for widget in lab_info.winfo_children():
    widget.grid_configure(padx=10, pady=6)


window.mainloop()