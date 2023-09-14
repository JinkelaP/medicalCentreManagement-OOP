import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from Clinic import Clinic
from datetime import datetime

cc = Clinic()

currentDate = datetime.now().strftime('%Y-%m-%d')
currentTime = datetime.now().strftime('%H:%M:%S')

# many functions

# read files and import from files
readFileStatus = None
def readFile():
    try:
        global readFileStatus
        if readFileStatus != True:

            doctorFile = open("Doctor.txt", "r")
            for line in doctorFile:
                data = line.strip()
                data = data.split(",")
                cc.newDoctor(data[0], data[1], data[2])
            
            for i in cc.allDoctors:
                boxDocs.insert(tk.END, f'{str(i)}')
            

            patFile = open("Patient.txt", "r")
            for line in patFile:
                data = line.strip()
                data = data.split(",")
                cc.newPatient(data[0], data[1])

            for i in cc.allPatients:
                boxPatients.insert(tk.END, f'{str(i)}')

            msg = f'Read file successful. Doctors and Patients have been imported.'
            showinfo(title = 'Success', message = msg)

            readFileStatus = True
        else:
            msg = f'You have read the file already.'
            showinfo(title = 'Caution', message = msg)


    except Exception as e:
        msg = f'Read file FAILED.'
        showinfo(title = 'ERROR', message = msg)

# msg box for displaying full patient information
def displayPatientInfo(event):
    selected = boxPatients.curselection()

    if selected:
        patientStr = boxPatients.get(selected[0])
        patID = int(patientStr[0:6])
        showinfo(title = 'Patient info', message = cc.displayPatient(patID))

# msg box for displaying full doctor information
def displayDocInfo(event):
    selected = boxDocs.curselection()

    if selected:
        docStr = boxDocs.get(selected[0])
        docID = int(docStr[0:5])
        showinfo(title = 'Doctor info', message = cc.displayDoctor(docID))

# get ID number and assign the doctor
def assignDoctor():
    patIndex = boxPatients.curselection()
    docIndex = boxDocs.curselection()

    if patIndex and docIndex:
        patientStr = boxPatients.get(patIndex[0])
        patID = int(patientStr[0:6])

        docStr = boxDocs.get(docIndex[0])
        docID = int(docStr[0:5])
        showinfo(title = 'Assign Doctor', message = cc.assignDoctorPatient(docID, patID))

    else:
        showinfo(title = 'Assign Doctor', message = 'Either doctor or patient is not chosen.\nPlease single-click them and then assign.')

# show all consults
def allConsult():
    showinfo(title = 'All consultations', message = cc.displayAllConsult())

# create a consultation by getting info from variables
def createConsult():
    patIndex = boxPatients.curselection()
    docIndex = boxDocs.curselection()

    if patIndex and docIndex:
        patientStr = boxPatients.get(patIndex[0])
        patID = int(patientStr[0:6])

        docStr = boxDocs.get(docIndex[0])
        docID = int(docStr[0:5])

        datetimeConsult = f'{consultationDate.get()} {consultationTime.get()}'
        showinfo(title = 'Create consultation', message = cc.newConsultation(datetimeConsult, \
                                                                         docID, patID, consultationReason.get(), \
                                                                        consultationFee.get()))

    else:
        showinfo(title = 'Create consultation', message = 'Either doctor or patient is not chosen.\nPlease single-click them and then submit.')

# create date
def createDate():
    currentDateNew = datetime.now().strftime('%Y-%m-%d')
    currentTimeNew = datetime.now().strftime('%H:%M:%S')
    consultationDate.set(currentDateNew)
    consultationTime.set(currentTimeNew)

# search a user

def searchUser():
    searchStrGet = searchStr.get()
    showinfo(title = 'Result', message = cc.searchUser(searchStrGet))


    

# Initialise Sys

root = tk.Tk()
root.title("Medical Centre Management System - beta 0.1 made by Haochen")
root.geometry("600x900+100+100")
root.resizable(width=False, height=False)

# widgets

# header
header = ttk.Label(root,text="Welcome to medical centre!", font=("Arial bold", 30))
header.pack(ipadx=10, ipady=10)

# frame operation
frmOperation = ttk.LabelFrame(root, text='Operation')
frmOperation.pack(padx=5, pady=5, side=tk.TOP)

# read file and create
readButton = ttk.Button(frmOperation, text="Read file", command=readFile)
readButton.pack(fill=tk.X, expand=True, padx=5, pady=5, ipadx=5, ipady=3,side=tk.LEFT)

# Assign doctor
assignButton = ttk.Button(frmOperation, text="Assign Doctor", command=assignDoctor)
assignButton.pack(fill=tk.X, expand=True, padx=5, pady=5, ipadx=5, ipady=3,side=tk.LEFT)

# Consultation report
allConsultButton = ttk.Button(frmOperation, text="Consultation report", command=allConsult)
allConsultButton.pack(fill=tk.X, expand=True, padx=5, pady=5, ipadx=5, ipady=3,side=tk.LEFT)

# frame displayInfo
frmdisplayInfo = ttk.LabelFrame(root, text='Display')
frmdisplayInfo.pack(padx=5, pady=5, side=tk.TOP)


# search function
searchStr = tk.StringVar()

frmSearch = ttk.LabelFrame(frmdisplayInfo, text='Search an user by name')
frmSearch.pack(padx=5, pady=5, side=tk.TOP)

boxSearch = tk.Label(frmSearch,  text="")
boxSearch.pack(fill=tk.BOTH, side=tk.LEFT)

entrySearch = ttk.Entry(frmSearch, textvariable=searchStr)
entrySearch.pack(fill='x', expand=True)

searchButton = ttk.Button(frmSearch, text="Submit", command=searchUser)
searchButton.pack(fill=tk.X, expand=True, padx=5, pady=5, ipadx=5, ipady=3,side=tk.LEFT)

# all patients&doctors label
frmPatients = ttk.LabelFrame(frmdisplayInfo, text='Patients')
frmPatients.pack(padx=5, pady=5, side=tk.LEFT)

boxPatients = tk.Listbox(frmPatients, exportselection=0, selectmode=tk.BROWSE)
boxPatients.bind('<Double-Button-1>', displayPatientInfo)
boxPatients.pack(fill=tk.BOTH, padx=20, pady=7, side=tk.LEFT)

frmDocs = ttk.LabelFrame(frmdisplayInfo, text='Doctors')
frmDocs.pack(padx=5, pady=5, side=tk.LEFT)

boxDocs = tk.Listbox(frmDocs, exportselection=0, selectmode=tk.BROWSE)
boxDocs.bind('<Double-Button-1>', displayDocInfo)
boxDocs.pack(fill=tk.BOTH, padx=20, pady=7,side=tk.LEFT)




#Vars needed
consultationDate = tk.StringVar()
consultationReason = tk.StringVar()
consultationFee = tk.StringVar()
consultationTime = tk.StringVar()

consultationDate.set(currentDate)
consultationTime.set(currentTime)

# frame consult
frmCreateConsult = ttk.LabelFrame(root, text='Create Consultation', width=300, height=300)
frmCreateConsult.pack(ipadx=80, ipady=80, padx=10, pady=10,side=tk.TOP)

# date
dateLabel = ttk.Label(frmCreateConsult, text="Date")
dateLabel.pack(fill='x', expand=True, padx=20)

dateEntry = ttk.Entry(frmCreateConsult, textvariable=consultationDate)
dateEntry.pack(fill='x', expand=True, padx=20)
dateEntry.focus()

# time
timeLabel = ttk.Label(frmCreateConsult, text="Time")
timeLabel.pack(fill='x', expand=True, padx=20)

timeEntry = ttk.Entry(frmCreateConsult, textvariable=consultationTime)
timeEntry.pack(fill='x', expand=True, padx=20)
timeEntry.focus()

# Reason
reasonLabel = ttk.Label(frmCreateConsult, text="Reason")
reasonLabel.pack(fill='x', expand=True, padx=20)

reasonEntry = ttk.Entry(frmCreateConsult, textvariable=consultationReason)
reasonEntry.pack(fill='x', expand=True, ipadx=30, ipady=30, padx=20)
reasonEntry.focus()

# Fee
feeLabel = ttk.Label(frmCreateConsult, text="Fee (NZD)")
feeLabel.pack(fill='x', expand=True, padx=20)

feeEntry = ttk.Entry(frmCreateConsult, textvariable=consultationFee)
feeEntry.pack(fill='x', expand=True, padx=20)
feeEntry.focus()

# frame operation
frmOperation2 = ttk.LabelFrame(frmCreateConsult, text='')
frmOperation2.pack(padx=5, pady=5, side=tk.TOP)

# date
dateButton = ttk.Button(frmOperation2, text="Current Date&Time", command=createDate)
dateButton.pack(fill=tk.X, expand=True, padx=5, pady=5, ipadx=5, ipady=3,side=tk.LEFT)

# submit
submitButton = ttk.Button(frmOperation2, text="Submit", command=createConsult)
submitButton.pack(fill=tk.X, expand=True, padx=5, pady=5, ipadx=5, ipady=3,side=tk.LEFT)




# start
root.mainloop()