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
        return 'Patient created'

    def newDoctor(self, fName, lName, spec):
        oneDoctor = Patient(fName, lName, spec)
        self.allDoctors.append(oneDoctor)
        return 'Doctor created'

    # search for a doctor/patient
    def searchDoctor(self, id):
        for doctor in self.allDoctors:
            if doctor.myDoctorID == id:
                return str(doctor)
        else:
            return 'Doctor not found.'
    
    def searchPatient(self, id):
        for patient in self.allPatients:
            if patient.myPatientID == id:
                return str(patient)
        else:
            return 'Patient not found.'
    
    def searchConsultation(self, id):
        for c in self.allConsultations:
            if c.myCDoctor == id or c.myCPatient == id:
                return str(c)
        else:
            return 'Consultation not found.'
            
    
    # Assign doctor to a patient
    def assignDoctorPatient(self, docID, patID):
        doctor = self.searchDoctor(docID)
        patient = self.searchPatient(patID)
        patient.myDoctor = doctor.myDoctorID
        return 'Doctor assigned to the patient.'

    # Add a consultation
    def newConsultation(self, date, docID, patID, reason, fee):
        doctor = self.searchDoctor(docID)
        patient = self.searchPatient(patID)
        oneConsultation = Consultation(date, doctor, patient, reason, fee)
        self.allConsultations.append(oneConsultation)
        return 'Consultation created'

    #Display information
    def displayDoctor(self, docID):
        doctor = self.searchDoctor(docID)
        return doctor
    
    def displayPatient(self, patID):
        patient = self.searchPatient(patID)
        return patient
    
    def displayConsultation(self, id):
        c = self.searchConsultation(id)
        return c
    
    def displayAllPat(self):
        patList = ''

        for pat in self.allPatients:
            patList += f'{str(pat)}\n' 

        if patList == '':
            return 'No patient in the record.'
        else:
            return patList
    
    def displayAllDoc(self):
        docList = ''

        for doc in self.allDoctors:
            docList += f'{str(doc)}\n' 

        if  docList == '':
            return 'No doctor in the record.'
        else:
            return docList
    
    def displayDocsPat(self, docID):
        docsPatList = ''
        for pat in self.allPatients:
            if pat.myDoctor == docID:
                docsPatList += f'{str(pat)}'
        
        if docsPatList == '':
            return 'The doctor does not manage any patient.'
        else:
            return 'These patients are managed by the doctor:\n' + docsPatList
    
    def displayConsult(self, id):
        consultList = ''
        for i in self.allConsultations:
            if i.myCDoctor == id or i.myCPatient == id:
                consultList += f'{str(i)}'
        
        if consultList == '':
            return 'The doctor/patient do not have any previous consultation.'
        else:
            return consultList
    

    
