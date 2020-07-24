import csv
StudentData=[]
#--------------------------------------- CLASS -----------------------------------------------
#create a class structure to store the information for each person.
#ensure that data type are explicit.
class StudentData:
    def __init__(self, in_studentname, in_Sub1, in_Sub2, in_Sub3, in_Sub4, in_Sub5):
        self.name=str(in_name)
        self.email=str(in_email)
        self.phone= str(in_phone)
        self.dob=datetime.datetime(int(in_dob[-4:]),int(in_dob[3:5]),int(in_dob[:2]))
        self.height= float(in_height)
        self.weight = int(in_weight)
        self.sex= str(in_sex)
        self.smoker=True if in_smoker=='Yes' else False

    def __str__(self):
        return self.name

    def BMI(self):
        return round(float(self.weight)/self.height**2,1)

    def age(self):
        calcAge=datetime.datetime.now() - self.dob
        return calcAge.days//365

#----------------------------------------- BMI ----------------------------------------------
#def BMI(height, weight):
#    return round(float(weight)/height**2,1)
#
#----------------------------------------- Load Data ---------------------------------------------
def loadData():
    data=csv.DictReader(open('Tasting Table.csv'))
    for datum in data:
        persons.append(person(datum['Name'],datum['Email'],datum['Phone'],datum['DoB'],
                              datum['Height'],datum['Weight'],datum['Gender'],datum['Smoker']))
    