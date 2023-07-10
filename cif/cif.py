import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pymysql

# window size
window = tkinter.Tk()
window.geometry("1450x750")
window.title("Case Investigation Form for covid-19")
window.resizable(0, 0)

# frame
frame = Frame(window, width=2500, height=2500, bg='black', bd=1)
frame.grid(row=0, column=0)
frame.pack()


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

    elif PatientId.get() == '':
        messagebox.showerror('Alert', 'please The Patients ID')
    elif PatientClinicalCoursecombobox.get() == '':
        messagebox.showerror('Alert', 'please select the patients clinical course')
    elif Ventilationcombobox.get() == '':
        messagebox.showerror('Alert', 'please enter the ventilation filed')
    elif HealthStatuscombobox.get() == '':
        messagebox.showerror('Alert', 'please enter The patients health status')
    elif PatientSymptoms.get() == '':
        messagebox.showerror('Alert', 'please enter the patients symptoms')
    elif PatientSigns.get() == '':
        messagebox.showerror('Alert', 'please enter the patients signs')
    elif Temperature.get() == '':
        messagebox.showerror('Alert', 'please enter the patients temperature')
    elif UnderlingCondtions.get() == '':
        messagebox.showerror('Alert', 'please enter the patients underling conditions')
    elif personalInformationIdBirtCertNo.get() == '':
        messagebox.showerror('Alert', 'please enter your ID/ birth cert no')

    elif Occupation.get() == '':
        messagebox.showerror('Alert', 'Enter your occupation')
    elif Travelled.get() == '':
        messagebox.showerror('Alert', 'have u travelled')
    elif VisitedAnyHealthFacility_combobox.get() == '':
        messagebox.showerror('Alert', 'THIS INFO IS REQUIRED')
    elif ExposureToARIP_combobox.get() == '':
        messagebox.showerror('Alert', 'please enter your Exposure to ARIP')
    elif ExposureToPCC_combobox.get() == '':
        messagebox.showerror('Alert', 'please enter your Exposure to PCC')
    elif VisitedAnyAnimalMarket_combobox.get() == '':
        messagebox.showerror('Alert', 'THIS FILLED IS REQUIRED')
    elif OccupationID.get() == '':
        messagebox.showerror('Alert', 'please enter your Occupation id')
    elif personal_Information_IdBirtCertNo.get() == '':
        messagebox.showerror('Alert', 'please enter your ID/ birth cert no')

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

            query = 'create table clinical_information (PatientId INT NOT NULL,' \
                    'PatientClinicalCourse VARCHAR(15) NOT NULL,Ventilation CHAR(3) NULL DEFAULT NULL,' \
                    'HealthStatus VARCHAR(11) NULL, PatientSymptoms VARCHAR(7) NULL DEFAULT NULL,' \
                    'PatientSigns VARCHAR(6) NULL DEFAULT NULL, Temparature FLOAT NULL DEFAULT NULL,' \
                    'UnderlyingConditions VARCHAR(4) NULL DEFAULT NULL,personalInformationIdBirtCertNo INT NOT NULL'

            query = 'create table exposureandtravelinformatio(Occupation VARCHAR(30) CHARACTER SET utf8mb3 NULL ' \
                    'DEFAULT NULL,'\
                    ' Travelled? VARCHAR(20) NULL DEFAULT NULL, VisitedAnyHealthFacility VARCHAR(3) NULL DEFAULT NULL,'\
                    ' ExposureToARIP` VARCHAR(30) NULL DEFAULT NULL,ExposureToPCC` VARCHAR(20) NULL DEFAULT NULL,'\
                    'VisitedAnyAnimalMarket VARCHAR(20) NULL DEFAULT NULL,OccupationID INT NOT NULL,'\
                    'Personal_Information_IdBirtCertNo` INT NOT NULL,PRIMARY KEY (`Personal_Information_IdBirtCertNo`),'\
                    'CONSTRAINT fk_ExposureandTravelInformation_Personal_Information1FOREIGN KEY (' \
                    'Personal_Information_IdBirtCertNo)REFERENCES case_ivestication_db.personal_information (' \
                    'IdBirtCertNo)))'

            cur.execute(query)
            messagebox.showinfo('success', 'fields created successfully')
        except:
            query = 'insert into personal_information(FirstName,SecondName,IdBirtCertNo, PhoneNumber, ' \
                    'CountyOfResidence,' \
                    'SubCounty, Ward ,Village,YearOfBirth, EmailAddress , TestStatus, ReasonForTesting, Vaccination , ' \
                    'SexAtBirth) ' \
                    'VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'

            #query = "INSERT INTO 'clinical_information' (PatientId,PatientClinicalCourse,Ventilation, HealthStatus, ' \
                 #   'PatientSymptoms, PatientSigns, Temparature, UnderlyingCondition,personalInformationIdBirthCertNo) ' \
                 #   'VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"

        cur.execute(query, (
            FirstName_entry.get(), SecondName_entry.get(), IdBirtCertNo_entry.get(), PhoneNumber_entry.get(),
            CountyOfResidence_entry.get(), SubCounty_entry.get(),
            Ward_entry.get(), Village_entry.get(), YearOfBirth_entry.get(), EmailAddress_entry.get(),
            TestStatus_combobox_entry.get(), ReasonForTesting_combobox_entry.get(),
            Vaccination_combobox_entry.get(), SexAtBirth_combobox_entry.get()))

        #cur.execute(query, (PatientId.get(), PatientClinicalCoursecombobox.get(), Ventilationcombobox.get(),
                            #HealthStatuscombobox.get(), PatientSymptoms.get(), PatientSigns.get(),
                            #Temperature.get(), UnderlingCondtions.get(), personalInformationIdBirtCertNo.get()))
        db.commit()
        db.cursor()
        messagebox.showinfo('success', 'successfully submitted')


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
lbl4.grid(row=7, column=0)

for widget in user_info_frame.winfo_children():
    widget.grid_configure(padx=10, pady=15)

# selection02; clinical information
clinic_info_frame = tkinter.LabelFrame(frame, text="clinical information", fg='#97ffff', bg='black',
                                       font="calibre 20 bold")
clinic_info_frame.grid(row=1, column=1, sticky="news", padx=5, pady=5)

PatientId = tkinter.Label(clinic_info_frame, text="Patient ID :", fg='#97ffff', bg='black',
                          font=('calibre', 10, 'bold'))
PatientId.grid(row=2, column=0, )
PatientId = tkinter.Entry(clinic_info_frame)
PatientId.grid(row=2, column=1, )

PatientClinicalCourse = tkinter.Label(clinic_info_frame, text="Patient Clinical Course :", fg='#97ffff', bg='black',
                                      font=('calibre', 10, 'bold'))
PatientClinicalCourse.grid(row=3, column=0, )
PatientClinicalCoursecombobox = ttk.Combobox(clinic_info_frame, values=["Asymptomatic", "Symptomatic", "Unknown"])
PatientClinicalCoursecombobox.grid(row=3, column=1, )

Ventilation = tkinter.Label(clinic_info_frame, text="Ventilated", fg='#97ffff', bg='black',
                            font=('calibre', 10, 'bold'))
Ventilationcombobox = ttk.Combobox(clinic_info_frame, values=["Yes", "No"])
Ventilation.grid(row=4, column=0)
Ventilationcombobox.grid(row=4, column=1)

HealthStatus = tkinter.Label(clinic_info_frame, text="Health Status", fg='#97ffff',
                             bg='black', font=('calibre', 10, 'bold'))
HealthStatuscombobox = ttk.Combobox(clinic_info_frame, values=["Stable", "Severely ill", "Dead"])
HealthStatus.grid(row=5, column=0)
HealthStatuscombobox.grid(row=5, column=1)

PatientSymptoms = tkinter.Label(clinic_info_frame, text="Patient symptoms)",
                                fg='#97ffff', bg='black', font=('calibre', 10, 'bold'))
PatientSymptoms.grid(row=2, column=2)
PatientSymptoms = tkinter.Entry(clinic_info_frame)
PatientSymptoms.grid(row=2, column=3, )

PatientSigns = tkinter.Label(clinic_info_frame, text="Patient signs \n (Number all reported signs)",
                             fg='#97ffff', bg='black', font=('calibre', 10, 'bold'))
PatientSigns.grid(row=3, column=2)
PatientSigns = tkinter.Entry(clinic_info_frame)
PatientSigns.grid(row=3, column=3)

Temperature = tkinter.Label(clinic_info_frame, text="Temparature\n( in degrees celsius)", fg='#97ffff', bg='black',
                            font=('calibre', 10, 'bold'))
Temperature.grid(row=4, column=2)
Temperature = tkinter.Entry(clinic_info_frame)
Temperature.grid(row=4, column=3, )

UnderlingCondtions = tkinter.Label(clinic_info_frame, text="Patient underling conditions :", fg='#97ffff', bg='black',
                                   font=('calibre', 10, 'bold'))
UnderlingCondtions.grid(row=5, column=2)
UnderlingCondtions = tkinter.Entry(clinic_info_frame)
UnderlingCondtions.grid(row=5, column=3)

personalInformationIdBirtCertNo = tkinter.Label(clinic_info_frame, text="Personal info Id/ :\n(Birth cert No) ",
                                                  fg='#97ffff', bg='black', font=('calibre', 10, 'bold'))
personalInformationIdBirtCertNo.grid(row=6, column=2)
personalInformationIdBirtCertNo = tkinter.Entry(clinic_info_frame)
personalInformationIdBirtCertNo.grid(row=6, column=3)

Submitbtn = Button(clinic_info_frame, text="Submit", command=submit, width=10, borderwidth=3, height=1, fg='white',
                   bg='#7f7fff', cursor='hand2', border=2, font=('#57a1f8', 10, 'bold'))
Submitbtn.grid(row=6, column=0)

for widget in clinic_info_frame.winfo_children():
    widget.grid_configure(padx=10, pady=10)

# selection03; Exposure and travel information in 14 days prior to symptoms.

exp_trav_info = tkinter.LabelFrame(frame, text="Exposure and travel information", fg='#97ffff', bg='black',
                                   font="calibre 20 bold")
exp_trav_info.grid(row=1, column=0, sticky="news", padx=5, pady=5)
Occupation = tkinter.Label(exp_trav_info, text="Occupation\n (Number any that apply)", fg='#97ffff', bg='black',
                           font=('calibre', 10, 'bold'))
Occupation.grid(row=2, column=0)
Occupation = tkinter.Entry(exp_trav_info)
Occupation.grid(row=2, column=1)

Travelled = tkinter.Label(exp_trav_info, text="Travelled\n 1. yes(specify) \n 2. No", fg='#97ffff', bg='black',
                          font=('calibre', 10, 'bold'))
Travelled.grid(row=3, column=0)
Travelled = tkinter.Entry(exp_trav_info)
Travelled.grid(row=3, column=1)

VisitedAnyHealthFacility = tkinter.Label(exp_trav_info, text="Visited any health facility(ies)", fg='#97ffff',
                                         bg='black',
                                         font=('calibre', 10, 'bold'))
VisitedAnyHealthFacility.grid(row=4, column=0)
VisitedAnyHealthFacility_combobox = ttk.Combobox(exp_trav_info, values=["Yes", "No"])
VisitedAnyHealthFacility_combobox.grid(row=4, column=1)

ExposureToARIP = tkinter.Label(exp_trav_info, text="Had close contact with an \n cute respiratory "
                                                   "infected person", fg='#97ffff', bg='black',
                               font=('calibre', 10, 'bold'))
ExposureToARIP.grid(row=5, column=0)
ExposureToARIP_combobox = ttk.Combobox(exp_trav_info, values=["Unknown", "No", "Yes"])
ExposureToARIP_combobox.grid(row=5, column=1)

ExposureToPCC = tkinter.Label(exp_trav_info, text="Had contact with \n a probable confirmed case", fg='#97ffff',
                              bg='black', font=('calibre', 10, 'bold'))
ExposureToPCC.grid(row=2, column=2)
ExposureToPCC_combobox = ttk.Combobox(exp_trav_info, values=["Unknown", "No", "Yes"])
ExposureToPCC_combobox.grid(row=2, column=3)

VisitedAnyAnimalMarket = tkinter.Label(exp_trav_info, text="Visited any live animal markets", fg='#97ffff', bg='black',
                                       font=('calibre', 10, 'bold'))
VisitedAnyAnimalMarket.grid(row=3, column=2)
VisitedAnyAnimalMarket_combobox = ttk.Combobox(exp_trav_info, values=["Unknown", "No", "Yes"])
VisitedAnyAnimalMarket_combobox.grid(row=3, column=3)

OccupationID = tkinter.Label(exp_trav_info, text="Travelled\n 1. yes(specify) \n 2. No", fg='#97ffff', bg='black',
                             font=('calibre', 10, 'bold'))
OccupationID.grid(row=4, column=2)
OccupationID = tkinter.Entry(exp_trav_info)
OccupationID.grid(row=4, column=3)

personal_Information_IdBirtCertNo = tkinter.Label(exp_trav_info, text="Personal information\n ID/ birth cert No",
                                                  fg='#97ffff', bg='black', font=('calibre', 10, 'bold'))
personal_Information_IdBirtCertNo.grid(row=5, column=2)
personal_Information_IdBirtCertNo = tkinter.Entry(exp_trav_info)
personal_Information_IdBirtCertNo.grid(row=5, column=3)

lbl9 = Button(exp_trav_info, text="Submit", command=submit, width=10, borderwidth=3, height=1, fg='white', bg='#7f7fff',
              cursor='hand2', border=2, font=('#57a1f8', 10, 'bold'))
lbl9.grid(row=6, column=0)

for widget in exp_trav_info.winfo_children():
    widget.grid_configure(padx=1, pady=5)

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
