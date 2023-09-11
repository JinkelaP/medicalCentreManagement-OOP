import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from Clinic import Clinic

cc = Clinic()

# many functions
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

def displayPatientInfo(event):
    selected = boxPatients.curselection()

    if selected:
        patientStr = boxPatients.get(selected[0])
        patID = int(patientStr[0:6])
        showinfo(title = 'Patient info', message = cc.displayPatient(patID))

def displayDocInfo(event):
    selected = boxDocs.curselection()

    if selected:
        docStr = boxDocs.get(selected[0])
        docID = int(docStr[0:5])
        showinfo(title = 'Doctor info', message = cc.displayDoctor(docID))

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


def allConsult():
    showinfo(title = 'All consultations', message = cc.displayAllConsult())

def createConsult():
    patIndex = boxPatients.curselection()
    docIndex = boxDocs.curselection()

    if patIndex and docIndex:
        patientStr = boxPatients.get(patIndex[0])
        patID = int(patientStr[0:6])

        docStr = boxDocs.get(docIndex[0])
        docID = int(docStr[0:5])
        showinfo(title = 'Create consultation', message = cc.newConsultation(consultationDate.get(), \
                                                                         docID, patID, consultationReason.get(), \
                                                                        consultationFee.get()))

    else:
        showinfo(title = 'Create consultation', message = 'Either doctor or patient is not chosen.\nPlease single-click them and then submit.')

    

# Initialise Sys

root = tk.Tk()
root.title("Medical Centre Management System - beta 0.1")
root.geometry("600x700+100+100")
root.resizable(width=False, height=False)

# widgets

# header
header = ttk.Label(root,text='Welcome to medical centre!', font=("Arial bold", 30))
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

# frame consult
frmCreateConsult = ttk.LabelFrame(root, text='Create Consultation', width=300, height=300)
frmCreateConsult.pack(ipadx=80, ipady=80, padx=10, pady=10,side=tk.TOP)

# date
dateLabel = ttk.Label(frmCreateConsult, text="Date")
dateLabel.pack(fill='x', expand=True, padx=20)

dateEntry = ttk.Entry(frmCreateConsult, textvariable=consultationDate)
dateEntry.pack(fill='x', expand=True, padx=20)
dateEntry.focus()

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

# submit
submitButton = ttk.Button(frmCreateConsult, text="Submit", command=createConsult)
submitButton.pack(fill='x', expand=True, padx=90, pady=10)



# start
root.mainloop()