import pickle
class Employee:
    def __init__(self, salary, desig,):
        print("Enter details for %s: " %desig)
        self.name = input("Enter name: ")
        try:
            self.age = int(input("Enter age: "))
            if(self.age < 21 or self.age > 65):
                raise InvalidAgeError
            self.salary = salary
            self.desig = desig

        except InvalidAgeError as ie:
            self.age = ie.readAge()

      
    def add(self):  
        f1 = open("empdetails.txt","a")
        det = self.name + "|" + str(self.age) + "|" + str(self.salary) + "|" + self.desig + "\n"
        f1.write(det)
        f1.close()

    @staticmethod
    def display():
        f1 = open("empdetails.txt","r")
        for line in f1:
            tempList = (line.split('|'))
            print("Name: " + tempList[0])
            print("Age: " + tempList[1])
            print("Salary: " + tempList[2])
            print("Designation: " + tempList[3])
        f1.close()

    def __str__(self):
        print("Name: ", self.name)
        print("Age: ",self.age)
        print("Salary: ",self.salary)
        print("Designation: ", self.desig)
        return " ";
    
    def displayEmployees(self):
        print("Name: ", self.name)
        print("Age: ",self.age)
        print("Salary: ",self.salary)
        print("Designation: ", self.desig)

class Clerk(Employee):
    salary = 8000
    desig = "Clerk"
    def __init__(self):
        super().__init__(self.salary, self.desig)

    def raiseSal(self):
        self.salary += 5000
        


class Programmer(Employee):
    salary = 25000
    desig = "Programmer"
    def __init__(self):
        super().__init__(self.salary, self.desig)

    def raiseSal(self):
        self.salary += 8000



class Manager(Employee):
    salary = 80000
    desig = "Manager"
    def __init__(self):
        super().__init__(self.salary, self.desig)

    def raiseSal(self):
        self.salary += 10000


class InvalidAgeError(Exception):
    def readAge(self):
        while(True):
            print("Please enter age between 21 and 65")
            age = int(input("Enter Age: "))
            if(age >= 21 and age <= 65):
                return age

class Emp:
    def raiseEmp(self, obj):
        print("Salary Raised !")
        obj.raiseSal()
