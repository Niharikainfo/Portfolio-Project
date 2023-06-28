import os

s=[]                # List which stores objects, these objects are created by teacher claass and represent details of each student 

class OptionNotAvailable(Exception):                    # Exception class if selected option isn't available
    def display(self):
        print("Error: Option Not Available!")
        print("Please enter correct option number from list!")

class RecordAlreadyExists(Exception):                 # Exception class that stops from re-entering details for the same PRN again
    def display(self):
        print("Error: Record for this PRN already exists!")
        print("Enter other PRN!")
        
class college():                   # Parent class which contain all data members (student detail variables)
    
    def __init__(self):          
        self.name=""
        self.prn=0
        self.marks=0
        self.attendance=""
    def read(self):                            # Parent class method (depicting polymorphism)
        os.system('cls')
        if len(s)==0:
            print("\t\t\t\t\tNo records exist!!!")
        else:
            print("Here is the list:")
            for i in s:
                print("Name- ", i.name)
                print("PRN- ", i.prn)
                print("Marks- ", i.marks)
                print("Attendance Percentage- ", i.attendance,"%")
        o=input("PRESS ENTER TO CONTINUE")

class teacher(college):               # Child class which have access to data members of parent class, can add new records and can edit them
    
    def __init__(self):
        os.system('cls')
        self.option()
    
    def option(self):
        os.system('cls')
        print("\t\t\t\t\t Welcome ")
        print("Enter 1: For entering new record")
        print("Enter 2: For updating existing records")
        print("Enter 3: To see all the records")
        try:                                            # nested exception handling
            z=int(input())
            if z== 1 or z==2 or z==3:
                pass
            else:
                raise OptionNotAvailable
        except OptionNotAvailable as e:
            e.display()
            try:
                z=int(input())
                if z== 1 or z==2 or z==3:
                    pass
                else:
                    raise OptionNotAvailable
            except OptionNotAvailable as e:
                e.display()
                z=int(input())
            except ValueError:
                print("Value Error!")
                print("Enter correct option from list!")
                z=int(input())
        except ValueError:
            print("Value Error!")
            print("Enter correct option from list!")
            try:
                z=int(input())
                if z== 1 or z==2 or z==3:
                    pass
                else:
                    raise OptionNotAvailable
            except OptionNotAvailable as e:
                e.display()
                z=int(input())
            except ValueError:
                print("Value Error!")
                print("Enter correct option from list!")
                z=int(input())
        if z==1:
            self.enterprn()
            self.entername()
            self.entermarks()
            self.enterattendance()
        elif z==2:
            self.update()
        elif z==3:
            self.read()
    
    def enterprn(self):
        try:                             # nested exception handling   
            try:
                self.prn=int(input("Enter PRN of student: "))
            except ValueError:
                print("Value Error!")
                print("PRN must be an integer!")
                try:
                    self.prn=int(input("Enter PRN of student: "))
                except ValueError:
                    print("Value Error!")
                    print("PRN must be an integer!")
                    self.prn=int(input("Enter PRN of student: "))
            for i in s:
                if i.prn==self.prn:
                    raise RecordAlreadyExists
        except RecordAlreadyExists as e:
            e.display()
            try:
                self.prn=int(input("Enter PRN of student: "))
            except ValueError:
                print("Value Error!")
                print("PRN must be an integer!")
                self.prn=int(input("Enter PRN of student: "))
            for i in s:
                if i.prn==self.prn:
                    raise RecordAlreadyExists
        except RecordAlreadyExists as e:
            e.display()
            self.prn=int(input("Enter PRN of student: "))
    
    def entername(self):
        os.system('cls')
        self.name=str(input("Enter name of student: "))
        
    def entermarks(self):
        try:                                    # nested exception handling
            self.marks=float(input("Enter internal marks of student: "))
        except ValueError:
            print("Value Error!")
            print("Marks must be in numbers!")
            try:
                self.marks=float(input("Enter internal marks of student: "))
            except ValueError:
                print("Value Error!")
                print("Marks must be in numbers!")
                self.marks=float(input("Enter internal marks of student: "))
        
    def enterattendance(self):
        try:                                        # nested exception handling
            self.attendance=float(input("Enter attendance percentage of student: "))
        except ValueError:
            print("Value Error!")
            print("Attendance should be in numbers!")
            try:
                self.attendance=float(input("Enter attendance percentage of student: "))
            except ValueError:
                print("Value Error!")
                print("Attendance should be in numbers!")
                self.attendance=float(input("Enter attendance percentage of student: "))
        s.append(self)
        print("\t\t\t\t\tRECORD ENTERED SUCCESSFULLY!!!")
    
    def update(self):
        os.system('cls')
        count=0
        if len(s) == 0:                          # if no records exists as of now
            print("\t\t\t\t\tNO RECORDS EXIST FOR UPDATION")
        else:
            try:                                 # nested exception handling
                p=int(input("Enter PRN of student whose details are to be updated: "))
            except ValueError:
                print("Value Error!")
                print("PRN must be an integer!")
                try:
                    p=int(input("Enter PRN of student whose details are to be updated: "))
                except ValueError:
                    print("Value Error!")
                    print("PRN must be an integer!")
                    p=int(input("Enter PRN of student whose details are to be updated: "))
            for i in s:
                if i.prn==p:
                    print("Enter new details: ")
                    try:                                    # nested exception handling
                        m=float(input("Enter updated internal marks: "))
                    except ValueError:
                        print("Value Error!")
                        print("Marks must be in numbers!")
                        try:
                            m=float(input("Enter updated internal marks: "))
                        except ValueError:
                            print("Value Error!")
                            print("Marks must be in numbers!")
                            m=float(input("Enter updated internal marks: "))        
                    try:                                        # nested exception handling
                        c=float(input("Enter updated attendance percentage: "))
                    except ValueError:
                        print("Value Error!")
                        print("Attendance should be in numbers!")
                        try:
                            c=float(input("Enter updated attendance percentage: "))
                        except ValueError:
                            print("Value Error!")
                            print("Attendance should be in numbers!")
                            c=float(input("Enter updated attendance percentage: "))
                    i.marks=m
                    i.attendance=c
                    print("\t\t\t\t\tRECORD UPDATED SUCCESSFULLY")
                    count=1
            if count==0:
                print("Details for PRN- ",p," haven't been entered yet!")  # if no record exists for that PRN
        
    
class student(college):         # Child class that can only access data members but only to read them and can't edit them
    
    def __init__(self,p):
        os.system('cls')
        self.p=p
        self.read()
    
    def read(self):
        os.system('cls')
        if len(s)==0:               # if no record exists so far
            print("\t\t\t\t\tNo records exist!!!")
        else:
            count=0
            for i in s:
                if(i.prn==self.p):
                    print("Here are your details: ")
                    print("Name- ", i.name)
                    print("PRN- ", i.prn)
                    print("Marks- ", i.marks)
                    print("Attendance Percentage- ", i.attendance,"%")
                    count=1
            if count==0:            # if your details haven't been updated yet
                print("Your details haven't been updated yet") 
        o=input("PRESS ENTER TO CONTINUE")
        
def pcheck():                  # File handling (teacher login password matched from .txt file) 
    os.system('cls')
    print("\t\t\t\t\tTEACHER LOGIN")
    f = open(r"C:\Users\Lenovo\Desktop\StudentManagementSystem.txt","r")
    b=f.read()
    f.close()
    p=(input("Enter Teacher LogIn Key: "))
    if p==b:
        newr()
    else:
        print("WRONG PASSWORD!!!")
        pcheck()            # recursive function

def newr():
    obj=teacher()
            
def control_flow():          # Base function that handles the control flow of whole program
    print("\t\t\t\t\tWelcome to Student Management System")
    print("Enter 1 for Teacher login")
    print("Enter 2 for Student login")
    print("Enter 3 to Exit program")
    try:                      # nested exception handling
        x=int(input())
        if x== 1 or x==2 or x==3:
            pass
        else:
            raise OptionNotAvailable
    except OptionNotAvailable as e:
        e.display()
        try:
            x=int(input())
            if x== 1 or x==2 or x==3:
                pass
            else:
                raise OptionNotAvailable
        except OptionNotAvailable as e:
            e.display()
            x=int(input())
        except ValueError:
            print("Value Error!")
            print("Enter correct option from list!")
            x=int(input())
    except ValueError:
        print("Value Error!")
        print("Enter correct option from list!")
        try:
            x=int(input())
            if x== 1 or x==2 or x==3:
                pass
            else:
                raise OptionNotAvailable
        except OptionNotAvailable as e:
            e.display()
            x=int(input())
        except ValueError:
            print("Value Error!")
            print("Enter correct option from list!")
            x=int(input())

    if x==1:
        pcheck()
        print("Press y to continue and n to logout")
        try:                         # nested exception handling
            op=str(input())
            if op=="y" or op=="n":
                pass
            else:
                raise OptionNotAvailable
        except OptionNotAvailable as e:
            e.display()
            print("Press y to continue and n to logout")
            try:
                op=str(input())
                if op=="y" or op=="n":
                    pass
                else:
                    raise OptionNotAvailable
            except OptionNotAvailable as e:
                e.display()
                print("Press y to continue and n to logout")
                op=str(input())
            
        while(op=='y'):          # loop (so that teacher can log out on wish and don't have to relogin again and again)
            os.system('cls')
            newr()
            print("Press y to continue and n to logout")
            try:                # nested exception handling
                op=str(input())
                if op=="y" or op=="n":
                    pass
                else:
                    raise OptionNotAvailable
            except OptionNotAvailable as e:
                e.display()
                print("Press y to continue and n to logout")
                try:
                    op=str(input())
                    if op=="y" or op=="n":
                        pass
                    else:
                        raise OptionNotAvailable
                except OptionNotAvailable as e:
                    e.display()
                    print("Press y to continue and n to logout")
                    op=str(input())

    elif x==2:
        os.system('cls')
        print("\t\t\t\t\tSTUDENT LOGIN ")
        try:                        # nested exception handling
            p=int(input("Enter your PRN: "))
        except ValueError:
            print("Value Error!")
            print("PRN must be an inteeger!")
            try:
                p=int(input("Enter your PRN: "))
            except ValueError:
                print("Value Error!")
                print("PRN must be an inteeger!")
                p=int(input("Enter your PRN: "))
            
        obj=student(p)
    
    elif x==3:              # to exit the program otherwise it will keep running
        exit()
    
    if 1:
        control_flow()
        
control_flow()                   # here the program starts and calls the base function which handles all the control flow of program
