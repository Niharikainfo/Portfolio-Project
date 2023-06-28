#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def gym():
    print("Gym membership management system")
    print("1.check your plan")
    print("2.want to take membership plan")
    option = int(input("Enter your option : "))
    if option == 1:
        print("No membership have been taken so far ")
        exit(0)
        gym()
 
    elif option == 2:
        people = int(input("Enter no. of members for you want to take membership : "))
        name_1 = []
        age_1= []
        sex_1= []
        email_1= []
        time_s=[]
        duration_s=[]
        city_s=[]
        package_s=[]
        for p in range(people):
            name = str(input("Name : "))
            name_1.append(name)
            age  = int(input("Age  : "))
            age_1.append(age)
            sex  = str(input("Male or Female : "))
            sex_1.append(sex)
            email = (input("Enter your email : "))
            email_1.append(email)
            time()
            
            
def time():
    print("\nAvailable Time Slots:")
    print("1 - 12.00 P.M")
    print("2 - 3.05 P.M")
    print("3 - 5.15 P.M")
    print("4 - 7.50 P.M")
    time_num= str(input("\nChoose your preferable time slot number: "))
    if time_num=='1':
        time_name="12.00 P.M"
    elif time_num=='2':
        time_name="3.05 P.M"
    elif time_num=='3':
        time_name="5.15 P.M"
    elif time_num=='4':
        time_name="7.50 P.M"
    else:
        print("\n\nWrong Option!\n\n")
        time_name=time()
        time_s.append(time_name)
    city()
    
def city():
    print("\nAvailable Cities:")
    print("1 - Noida")
    print("2 - Delhi")
    print("3 - Gurugram")
    city_num= str(input("\nChoose your preferable city number: "))
    if city_num=='1':
        city_name="Noida"
    elif city_num=='2':
        city_name="Delhi"
    elif city_num=='3':
        city_name="Gurugram"
    else:
        print("\n\nWrong Option!\n\n")
        city_name=city()
        city_s.append(city_name)
    duration()
        
def duration():
    print("\nmembership duration:")
    print("1 - 3 months")
    print("2 - 6 months")
    print("3 - 8 months")
    print("4 - 10 months")
    print("5 - 12 months")
    duration_num= str(input("\nChoose your preferable duration : "))
    if duration_num=='1':
        duration_name="3 months"
    elif duration_num=='2':
        duration_name="6 months"
    elif duration_num=='3':
        duration_name="8 months"
    elif duration_num=='4':
        duration_name="10 months"
    elif duration_num=='5':
        duration_num="12 months"
    else:
        print("\n\nWrong Option!\n\n")
        duration_name=duration()
        duration_s.append(duration_name)
    package()
        
def package():
    print("\ndifferent packages are available:")
    print("1 - gold")
    print("2 - silver")
    print("3 - platinum")
    package_num= str(input("\nChoose your package : "))
    if package_num=='1':
        package_name="gold"
    elif package_num=='2':
        package_name="silver"
    elif package_num=='3':
        package_name="platinum"
    else:
        print("\n\nWrong Option!\n\n")
        package_name=package()
        package_s.append(package_name)
    print("Congratulation! your Registration is Complete")


gym()
    
 

