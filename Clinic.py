from Doctor import Doctor
from Patient import Patient
from Consultation import Consultation
from decimal import Decimal

class Clinic:
    def __init__(self):
        self.allDoctors = []
        self.allPatients = []
        self.allConsultations = []

    # add new objects into lists
    def newPatient(self, fName, lName):
        onePatient = Patient('n/a', fName, lName)
        self.allPatients.append(onePatient)
        return 'Patient created'

    def newDoctor(self, fName, lName, spec):
        oneDoctor = Doctor(fName, lName, spec)
        self.allDoctors.append(oneDoctor)
        return 'Doctor created'

    # search for a doctor/patient
    def searchDoctor(self, id):
        for doctor in self.allDoctors:
            if doctor.myDoctorID == id:
                return doctor
        else:
            return 'Doctor not found.'
    
    def searchPatient(self, id):
        for patient in self.allPatients:
            if patient.myPatientID == id:
                return patient
        else:
            return 'Patient not found.'
    
    def searchConsultation(self, id):
        consultationList = []
        for c in self.allConsultations:
            if c.myCDoctor == id or c.myCPatient == id:
                consultationList.append(c)
        
        if consultationList == []:
            return 'No consultation found.'
        else:
            return consultationList
            
    
    # Assign doctor to a patient
    def assignDoctorPatient(self, docID, patID):
        doctor = self.searchDoctor(docID)
        patient = self.searchPatient(patID)
        patient.myDoctor = doctor.myDoctorID
        return 'Doctor assigned to the patient.'

    # Add a consultation
    def newConsultation(self, date, docID, patID, reason, fee):
        docAssigned = self.searchPatient(patID).myDoctor
        if docAssigned != docID:
            return 'Caution! Either:\n\n The doctor you chosed is not the one assigned to the patient! \n\nOr \n\nYou have not assigned a doctor to the patient.'
        else:
            try:
                feeDecimal = Decimal(fee)
            except:
                return 'Fee must be number, allowing two decimals.'
            oneConsultation = Consultation(date, docID, patID, reason, feeDecimal)
            self.allConsultations.append(oneConsultation)
            return 'Consultation created'

    #Display information
    # def displayDoctor(self, docID):
    #     doctor = self.searchDoctor(docID)
    #     if type(doctor) is str:
    #         return doctor
    #     else:
    #         return f'ID: {doctor.myDoctorID}\nName: {doctor.myDoctorFName} {doctor.myDoctorLName}\nSpecialisation: {doctor.myDoctorSpec}'

    def displayDoctor(self, docID):
        doctor = self.searchDoctor(docID)
        if type(doctor) is str:
            return doctor
        else:
            patientDocList = []
            for p in self.allPatients:
                if p.myDoctor == docID:
                    patientDocList.append(p)
            
            if patientDocList != []:
                patientDocAll = ''
                for i in patientDocList:
                    patientDocAll += f'{str(i)}\n'
            else:
                patientDocAll = 'No patient assigned yet.'
            
            
            doctorConsultation = self.searchConsultation(docID)
            if doctorConsultation != 'No consultation found.':
                doctorConsultAll = ''
                for i in doctorConsultation:
                    patName = f'{self.searchPatient(i.myCPatient).myPatientFName} {self.searchPatient(i.myCPatient).myPatientLName}'
                    doctorConsultAll += f'{i.myCDate} {patName} // {i.myCReason} // {i.myFee} NZD\n'
            else:
                doctorConsultAll = 'No consultation yet.'
                
            return f'ID: {doctor.myDoctorID}\nName: {doctor.myDoctorFName} {doctor.myDoctorLName}\nSpecialisation: {doctor.myDoctorSpec}\n\nPatients:\n{patientDocAll}\n\nConsultations:\n{doctorConsultAll}'
    
    def displayPatient(self, patID):
        patient = self.searchPatient(patID)
        if type(patient) is str:
            return patient
        else:
            if patient.myDoctor == 'n/a':
                doctorPrint = patient.myDoctor
            else:
                doctor = self.searchDoctor(int(patient.myDoctor))
                doctorPrint = f'{doctor.myDoctorFName} {doctor.myDoctorLName}'
            
            patConsultation = self.searchConsultation(patID)
            if patConsultation != 'No consultation found.':
                patConsultAll = ''
                patFeeAll = Decimal(0.00)
                for i in patConsultation:
                    doctorName = f'{self.searchDoctor(i.myCDoctor).myDoctorFName} {self.searchDoctor(i.myCDoctor).myDoctorLName}'
                    patConsultAll += f'{i.myCDate} {doctorName} // {i.myCReason} // {i.myFee} NZD\n'
                    patFeeAll += i.myFee
                patFeeAll = str(patFeeAll)
                patFeeAll += ' NZD due.'
                
            else:
                patConsultAll = 'No consultation yet.'
                patFeeAll = 'n/a'

            return f'ID: {patient.myPatientID}\nName: {patient.myPatientFName} {patient.myPatientLName}\nAssigned Doctor: {doctorPrint}\n\nConsultations:\n{patConsultAll}\n\nTotal fees:\n{patFeeAll}'
    
    def displayConsult(self, id):
        consultList = ''
        for i in self.allConsultations:
            if i.myCDoctor == id or i.myCPatient == id:
                consultList += f'{str(i)}'
        
        if consultList == '':
            return 'The doctor/patient does not have any previous consultation.'
        else:
            return consultList
    
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
    
    def displayAllConsult(self):
        consultList = ''
        totalFee = Decimal(0.00)
        for i in self.allConsultations:
            doctorName = f'{self.searchDoctor(i.myCDoctor).myDoctorFName} {self.searchDoctor(i.myCDoctor).myDoctorLName}'
            patName = f'{self.searchPatient(i.myCPatient).myPatientFName} {self.searchPatient(i.myCPatient).myPatientLName}'
            consultList += f'{i.myCDate} {doctorName} {patName} // {i.myCReason} // {i.myFee} NZD \n'
            totalFee += i.myFee
        
        if consultList == '':
            return 'The medical centre does not have any previous consultation.'
        else:
            return f'Consultation Report for medical center: \n\n{consultList}\nTotal fee: {str(totalFee)} NZD'
    

    
