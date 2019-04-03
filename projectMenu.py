from project import *
from numpy import *

count = 0

class menu:
   employees = []
   def display(self):
       while(True):
          try:
             print("1. Create")
             print("2. Display")
             print("3. Raise Salary")
             print("4. Exit")
             ch = int(input())
             if(ch==1):
                while(True):  
                   print("1. Clerk")
                   print("2. Programmer")
                   print("3. Manager")
                   print("4. Exit")
                   try:
                      ch2 = int(input())
                      if(ch2 == 1):  
                         cl = Clerk()
                         cl.add()
                         self.employees.append(cl)
                      elif(ch2 == 2):
                         pr = Programmer()
                         pr.add()
                         self.employees.append(pr)
                      elif(ch2 == 3):        
                         mg = Manager()
                         mg.add()
                         self.employees.append(mg)
                      elif(ch2 == 4):
                         break
                      global count;
                      count += 1
                   except ValueError as v:
                      print("Wrong input ! Please Enter numerical value only: ",v)
                      continue
             elif(ch == 2):
                 for em in self.employees:
                    em.displayEmployees()
             elif(ch == 3):
                 for e in self.employees:
                    temp = Emp()
                    temp.raiseEmp(e)
             elif(ch == 4):
                 print("Number of employees created: ",count)
                 break
             else:
                 print("Wrong choice")
          except ValueError as v:
             print("Wrong input ! Please Enter numerical value only: ", v)
             continue
