class Doctor:
    nextID = 1000
    def __init__(self, fName, lName, spec):
        self.__myDoctorFName = fName
        self.__myDoctorLName = lName
        self.__myDoctorSpec = spec
        self.__myDoctorID = Doctor.nextID
        Doctor.nextID += 1

    def __str__(self):
        return str(self.__myDoctorID) + " " + self.__myDoctorFName + " " + self.__myDoctorLName
    
    # getter and setter needed
    @property
    def myDoctorFName(self):
        return self.__myDoctorFName

    @property
    def myDoctorLName(self):
        return self.__myDoctorLName
    
    @property
    def myDoctorSpec(self):
        return self.__myDoctorSpec
    
    @property
    def myDoctorID(self):
        return self.__myDoctorID