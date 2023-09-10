from Doctor import Doctor
from Patient import Patient
from Consultation import Consultation

class Clinic:
    def __init__(self):
        self.allDoctors = []
        self.allPatients = []
        self.allConsultations = []

    # add new objects into lists
    def newPatient(self, myDoctor, fName, lName):
        onePatient = Patient(myDoctor, fName, lName)
        self.allPatients.append(onePatient)

    def newDoctor(self, fName, lName, spec):
        oneDoctor = Patient(fName, lName, spec)
        self.allDoctors.append(oneDoctor)

    def newConsultation(self, date, doctor, patient, reason, fee):
        oneConsultation = Consultation(date, doctor, patient, reason, fee)
        self.allConsultations.append(oneConsultation)