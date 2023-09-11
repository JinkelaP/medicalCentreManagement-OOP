class Consultation:
    nextID = 1000
    def __init__(self, date, doctor, patient, reason, fee):
        self.__myCDate = date
        self.__myCDoctor = doctor
        self.__myCPatient = patient
        self.__myCReason = reason
        self.__myFee = fee

    def __str__(self):
        return f'{self.__myCDate} {self.__myCDoctor} {self.__myCPatient} // {self.__myCReason} // {self.__myFee} NZD'
    
    # getter and setter needed
    @property
    def myCDate(self):
        return self.__myCDate

    @property
    def myCDoctor(self):
        return self.__myCDoctor
    
    @property
    def myCPatient(self):
        return self.__myCPatient
    
    @property
    def myCReason(self):
        return self.__myCReason
    
    @property
    def myFee(self):
        return self.__myFee