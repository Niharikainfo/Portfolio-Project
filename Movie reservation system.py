email_s=[]
name_s=[]
city_s=[]
theatre_s=[]
date_s=[]
movie_s=[]
time_s=[]
ticket_s=[]

def menu():
    print("\nWelcome To Movie Ticket Reservation System")
    print("1 - Reserve tickets")
    print("2 - Check reservation details")
    print("3 - Exit")
    option = str(input("\nEnter your option: "))
    if option == '1':
        booking()
    elif option =='2':
        details()
    elif option =='3':
        exit()
    else:
        print("\nWrong Option!\n")
    input("\n\nPress Enter for further option\n\n")
    menu()
    return

def booking():
    email=str(input("\nEnter your Email address:"))
    n=check(email)
    if n==1:
        print("\nSorry! Ticket have been already reserved using this Email ID!\n")
        print("\nAnd you can only reserve ticket once\n")
        return
    else:
        email_s.append(email) 
        name=str(input("\nEnter your name:"))
        name_s.append(name)
        city_p= city()
        theatre_p= theatre()
        date_p= date()
        movie_p= movie()
        time_p= time()
        ticket_p= ticket()
        print("\n\n Congratulation! Reservation Complete\n\n")
        print("Email ID:", email)
        print("Name:", name)
        print("No. of Tickets:", ticket_p)
        print("City Name:", city_p)
        print("Theatre Name:", theatre_p)
        print("Date of reservation:", date_p)
        print("Show Time:", time_p)
        print("Movie Name:", movie_p)
    return

def details():
    if len(email_s)==0:
        print("\n\nNo reservations have been made so far!\n\n")
        return
    check=str(input("\nEnter the email you used for reserving tickets: "))
    n=0
    for i in email_s:
        if check == i:
            break
        n=n+1
    if n==len(email_s):
        print("\nNo ticket is reserved using this Email ID!\n")
        return
    else:
        print("\n\nEmail ID:", email_s[n])
        print("Name:", name_s[n])
        print("No. of Tickets:", ticket_s[n])
        print("City Name:", city_s[n])
        print("Theatre Name:", theatre_s[n])
        print("Show Date:", date_s[n])
        print("Show Time:", time_s[n])
        print("Movie Name:", movie_s[n])
    return

def check(x):
    n=0
    for i in email_s:
        if x == i:
            break
        n=n+1
    if n<len(email_s):
        w=1
    else:
        w=0
    return w

def city():
    print("\nAvailable Cities:")
    print("1 - Noida")
    print("2 - Delhi")
    print("3 - Gurugram")
    city_num= str(input("\nChoose your preferable city number: "))
    if city_num=='1':
        city_name="Noida"
        city_s.append(city_name)
    elif city_num=='2':
        city_name="Delhi"
        city_s.append(city_name)
    elif city_num=='3':
        city_name="Gurugram"
        city_s.append(city_name)
    else:
        print("\n\nWrong Option!\n\n")
        city_name=city()
    return city_name

def theatre():
    print("\nAvailable Theatres:")
    print("1 - PVR")
    print("2 - INOX")
    print("3 - Wave")
    theatre_num= str(input("\nChoose your preferable theatre number: "))
    if theatre_num=='1':
        theatre_name="PVR"
    elif theatre_num=='2':
        theatre_name="INOX"
    elif theatre_num=='3':
        theatre_name="Wave"
    else:
        print("\n\nWrong Option!\n\n")
        theatre_name=theatre()
    theatre_s.append(theatre_name)
    return theatre_name

def date():
    print("\nAvailable Dates:")
    print("1 - 28/11/2022")
    print("2 - 29/11/2022")
    print("3 - 30/11/2022")
    print("4 - 1/12/2022")
    print("5 - 2/12/2022")      
    date_num= str(input("\nChoose your preferable date number: "))
    if date_num=='1':
        date_name="28/11/2022"
    elif date_num=='2':
        date_name="29/11/2022"
    elif date_num=='3':
        date_name="30/11/2022"
    elif date_num=='4':
        date_name="1/12/2022"
    elif date_num=='5':
        date_name="2/12/2022"
    else:
        print("\n\nWrong Option!\n\n")
        date_name=date()
    date_s.append(date_name)
    return date_name

def movie():
    print("\nAvailable Movies:")
    print("1 - Bhediya")
    print("2 - Drishiyam 2")
    print("3 - Uunchai")
    movie_num= str(input("\nChoose your preferable movie number: "))
    if movie_num=='1':
        movie_name="Bhediya"
    elif movie_num=='2':
        movie_name="Drishiyam 2"
    elif movie_num=='3':
        movie_name="Uunchai"
    else:
        print("\n\nWrong Option!\n\n")
        movie_name=movie()
    movie_s.append(movie_name)
    return movie_name

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
    return time_name

def ticket():
    ticket_name= str(input("\nEnter the number of tickets you want: "))
    if ticket_name in ['1','2','3','4','5','6','7','8','9','10']:
        ticket_num=int(ticket_name)
        ticket_s.append(ticket_num)
    else:
        print("\nSorry! Wrong Input!\nYou can only reserve upto 10 tickets!\n")
        ticket_name=ticket()
    return ticket_name

menu()
