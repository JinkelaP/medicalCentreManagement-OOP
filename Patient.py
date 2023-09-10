class Patient:
    nextID = 10000
    def __init__(self, myDoctor, fName, lName):
        self.__myDoctor = myDoctor
        self.__myPatientFName = fName
        self.__myPatientLName = lName
        self.__myPatientID = Patient.nextID
        Patient.nextID += 1

    def __str__(self):
        return str(self.__myPatientID) + " " + self.__myPatientFName + " " + self.__myPatientLName

    # getter and setter needed
    @property
    def myDoctor(self):
        return self.__myDoctor
    
    @property
    def myPatientFName(self):
        return self.__myPatientFName

    @property
    def myPatientLName(self):
        return self.__myPatientLName
    
    @property
    def myPatientID(self):
        return self.__myPatientID