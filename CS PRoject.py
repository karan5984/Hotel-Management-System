#                    Creating Database and Table                            
#                  ******************************* 

import mysql.connector  
db=mysql.connector.connect(host='localhost',user='root',password='root') 
mycursor=db.cursor() 
mycursor.execute('create database if not exists HOTEL_MANAGEMENT') 

db=mysql.connector.connect(host='localhost',user='root',password='root',database='HOTEL_MANAGEMENT') 
mycursor=db.cursor() 

mycursor.execute("create table if not exists hoteldata(Ccode int(5) primary key , Cname varchar(20) , Cadd varchar(20) , Cindate varchar(5) , Coutdate varchar(5) , Room_no varchar(5) , Room_rent varchar(10))")
mycursor.execute("insert into hoteldata values(25,'Deepak','Morar,Gwalior',25,26, 1000, 6000)")
mycursor.execute("insert into hoteldata  values(26,'Amit','Morar,Gwalior',5,8,1017, 10000)") 
mycursor.execute("insert into hoteldata values(27,'Anuj','New  Delhi',12,20,1407, 000)") 
mycursor.execute("insert into hoteldata values(28,'Kunal','Morar,Gwalior',5,8,1405, 9000)") 
mycursor.execute("insert into hoteldata values(29,'Smith','Canada',23,30,1008, 3000)") 
mycursor.execute("insert into hoteldata values(30,'Alex','America',25,30,1012, 3000)") 
mycursor.execute("create table if not exists Room(Room_no int(1),Rooms varchar(10),Type varchar(45), Charges int(7),Features varchar(90),Occupancy int(45))")
mycursor.execute("insert into Room values(1,'1-500','Duplex',6000,'Two rooms on same  floor connected by common stairs',5)") 
mycursor.execute("insert into Room values(2,'501-1000','Cabana',5000,'Faces water body,beach or a swimming pool',3)") 
mycursor.execute("insert into Room values(3,'1001-1500','Lanai',4000,'This room faces a landscape, a waterfall, or a garden',4)") 
mycursor.execute("insert into Room values(4,'1501-2000','Suit',3000, 'It is composed of one or more bedrooms, a living room, and a dining area',12)")
mycursor.execute("insert into Room values(5,'2001-2500','Mini',2000, 'It is composed of one bedroom, a living room',12)") 
mycursor.execute("create table if not exists Customer(Ccode int(5),Cid_type varchar (20),Cid_no varchar(15) primary key , Cname varchar(15), Ccontact_no varchar(15),Cadd varchar(20),Cindate varchar(5), Coutdate varchar(5), CNationality varchar(10))")
mycursor.execute("insert into Customer values(25,'Aadhaar card',412563578952, 'Deepak',8269513294,'Morar,Gwalior',25,26,'Indian' )") 
mycursor.execute("insert into Customer values(26,'Pan card', 5874695325,'Amit', 9063560847,'Morar,Gwalior',5,8,'Indian')") 
mycursor.execute("insert into Customer values(27,'Pan card', 8456958236, 'Anuj', 9770563593,'New Delhi',12,20,'Indian')") 
mycursor.execute("insert into Customer values(28,'Service Id',8546952156,'Kunal', 4856985123,'Morar,Gwalior',5,8,'Indian')") 
mycursor.execute("insert into Customer values(29,'Voter Id Card',45896244,'Smith', 6598541256,'Canada',23,30,'Canadian')") 
mycursor.execute("insert into Customer values(30,'Aadhaar card',485962578545, 'Alex',6325489652,'America',25,30,'American')") 
db.commit() 
 
def speciality():
    db=mysql.connector.connect(host='localhost',user='root',password='root',database= 'HOTEL_MANAGEMENT') 
    mycursor=db.cursor() 
    qry=("select * from room") 
    mycursor.execute(qry) 
    for (Room_no,Rooms,Type,Charges,Features,Occupancy) in mycursor: 
        print("We have Rooms",Rooms,"of type",Type,",it has",Features,"and occupancy of",Occupancy,"persons.") 
    db.commit() 

# Function, hotel fare calculator 
# ********************************** 
 
def hotelfarecal(): 
      while True : 
             print("\n")
             print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~") 
             print("1.Booking for Room")         
             print("2.Show Customer Record") 
             print("3.Search Customer Record") 
             print("4.Delete Customer Record") 
             print("5.Update Customer Record") 
             print("6.Return to Main Menu") 
             print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
             b=(input("\nEnter your choice:"))
             
             if (b=='1'): 
                    z='y' 
                    while (z=='y'): 
                           inputdata() 
                           z=input("\nDo you want to continue..(y/n):") 
                    if (z=='n'): 
                           return hotelfarecal() 
                    else : 
                           print("Invalid Input!!") 
                           z=input("\nDo you want to continue..(y/n):")         

             elif (b=='2'): 
                    z='y' 
                    while z=='y': 
                          display() 
                          z=input("\nDo you want to continue..(y/n):")  
                    if  (z=='n'): 
                          return hotelfarecal() 
                    else : 
                          print("Invalid Input!!") 
                          z=input("\nDo you want to continue..(y/n):") 
 
             elif (b=='3'): 
                    z='y' 
                    while (z=='y'): 
                          search() 
                          z=input("\nDo you want to continue..(y/n):") 
                    if (z=='n'): 
                          return hotelfarecal() 
                    else : 
                          print("Invalid Input!!") 
                          z=input("\nDo you want to continue..(y/n):") 
 
             elif (b=='4'): 
                    z='y' 
                    while (z=='y'): 
                          delete() 
                          z=input("\nDo you want to continue..(y/n):") 
                    if (z=='n'): 
                          return hotelfarecal() 
                    else : 
                          print("Invalid Input!!") 
                          z=input("\nDo you want to continue..(y/n):") 
 
             elif (b=='5'): 
                    z='y' 
                    while (z=='y'): 
                          update() 
                          z=input("\nDo you want to continue..(y/n):") 
                    if (z=='n'): 
                          return hotelfarecal() 
                    else : 
                          print("Invalid Input!!") 
                          z=input("\nDo you want to continue..(y/n):") 
 
             elif (b=='6'): 
                    break 
             
             else: 
                    print("Invalid Input......") 
 
# Inserting data 
# ****************** 

import random 
def inputdata():
    Customer_code=random.randint(31,2501)
    print("------------------")
    print("\nCustomer Code:",Customer_code)
    print("------------------")
    s=0
    db=mysql.connector.connect(host='localhost',user='root',password='root',database= 'HOTEL_MANAGEMENT') 
    mycursor=db.cursor()
    print("\n")
    Ccode=input("Enter Customer Code:") 
    Cname=input("Enter Customer Name:") 
    Cadd=input("Enter Customer Address:") 
    Cindate=input("Enter Customer Check in Date:") 
    Coutdate=input("Enter Customer Check out Date:") 
    Cid_type=input("Enter your Identity card name:") 
    Cid_no=input("Enter your Identity number:") 
    Ccontact_no=input("Enter you Contact number:") 
    CNationality=input("Enter your nationality:")
    qry1=("insert into Customer(Ccode,Cid_type,Cid_no,Cname,Ccontact_no,Cadd,Cindate,Coutdate,CNationality) values({0},'{1}',{2},'{3}',{4},'{5}',{6},{7},'{8}')".format(Ccode,Cid_type,Cid_no,Cname,Ccontact_no,Cadd,Cindate,Coutdate,CNationality))
    mycursor.execute(qry1)
    print("\n")
   
    #      Booking room
    #    ****************
   
    print ("We have the following rooms for you:-")
    print("___________________________________")
    qry=("select * from room")
    mycursor.execute(qry)
    for (Room_no,Rooms,Type,Charges,Features,Occupancy) in mycursor:
        print("\n")
        print("Room No.-",Room_no)
        print("No. of rooms:",Rooms)
        print("Room type:",Type)
        print("Cost per room:",Charges)
        print("Features of the rrom:",Features)
        print("No. of person per room:",Occupancy)
        print("___________________________________")
    print ("\n6.  Next") 
     
    while (1): 
            x=int(input("\nEnter your choice:")) 
     
            if (x==1):
                    n=int(input("For How Many Nights Did You Stay:")) 
                    print ("You have opted room Duplex") 
                    s=s+6000*n 
                    Room_no= random.randint(1,501) 
                    print("Your Room Number is:",Room_no) 
     
            elif (x==2): 
                    n=int(input("For How Many Nights Did You Stay:")) 
                    print ("You have opted room Cabana") 
                    s=s+5000*n 
                    Room_no= random.randint(501,1001) 
                    print("Your Room Number is:",Room_no) 
    
            elif (x==3): 
                    n=int(input("For How Many Nights Did You Stay:")) 
                    print ("You have opted room Lanai") 
                    s=s+4000*n 
                    Room_no= random.randint(1001,1501) 
                    print("Your Room Number is:",Room_no) 
       
            elif (x==4): 
                    n=int(input("For How Many Nights Did You Stay:")) 
                    print ("You have opted room Suit") 
                    s=s+3000*n 
                    Room_no= random.randint(1501,2001) 
                    print("Your Room Number is:",Room_no) 
     
            elif (x==5): 
                    n=int(input("For How Many Nights Did You Stay:")) 
                    print ("You have opted room Mini") 
                    s=s+2000*n 
                    Room_no= random.randint(2001,2501) 
                    print("Your Room Number is:",Room_no) 
             
            elif (x==6) :
                    break 

            else: 
                    print ("Please choose a room") 
    print ("Your room rent is",s,'RS')
    qry2=("insert into hoteldata(Ccode,Cname,Cadd,Cindate,Coutdate,Room_no,Room_rent) values({0},'{1}','{2}',{3},{4},{5},{6})".format(Ccode,Cname,Cadd,Cindate,Coutdate,Room_no,s))
    mycursor.execute(qry2)
    if s==0:
        mycursor.execute("delete from hoteldata where Ccode=%s",(Ccode,))
        mycursor.execute("delete from customer where Ccode=%s",(Ccode,))
    db.commit() 
    mycursor.close() 
    db.close()

# Show Details of Customer 
# **************************** 

def display(): 
      print("\n") 
      print("1.Display all records") 
      print("2.Display through code number") 
      d=input("\nEnter your choice:") 
      
      if (d=='1'): 
              db=mysql.connector.connect(host='localhost',user='root',password='root',database= 'HOTEL_MANAGEMENT') 
              mycursor=db.cursor() 
              qry=("select h.Ccode,h.Cname,h.Cadd,h.Cindate,h.Coutdate,h.Room_no,c.CNationality, c.Ccontact_no,c.Cid_type,c.Cid_no from hoteldata h, customer c where  h.Ccode=c.Ccode") 
              mycursor.execute(qry)             
              for(Ccode,Cname,Cadd,Cindate,Coutdate,Room_no,CNationality, Ccontact_no,Cid_type,Cid_no) in mycursor:          
                     print ("\n") 
                     print ("Customer details.......") 
                     print ("Customer code:",Ccode) 
                     print ("Customer name:",Cname) 
                     print ("Customer Id type:",Cid_type) 
                     print ("Customer Id Number:",Cid_no) 
                     print ("Customer address:",Cadd)
                     print ("customer Nationality:",CNationality) 
                     print ("Check in date:",Cindate) 
                     print ("Check out date",Coutdate) 
                     print ("Room number:",Room_no) 
                     print ("Customer Contact number:",Ccontact_no) 
                     print ("___________________________________")
              mycursor.close() 
              print("\nIt's All record") 
              db.close() 

      elif (d=='2'): 
              db=mysql.connector.connect(host='localhost',user='root',password='root', 
              database='HOTEL_MANAGEMENT') 
              mycursor=db.cursor() 
              Ccode=input("\nEnter code of customer:") 
              qry=("select h.Ccode,h.Cname,h.Cadd,h.Cindate,h.Coutdate,h.Room_no,c.CNationality,c.Ccontact_no,c.Cid_type,c.Cid_no from hoteldata h, customer c where h.Ccode=c.Ccode and h.Ccode=%s") 
              rec_code=(Ccode,) 
              mycursor.execute(qry,rec_code) 
              rec_count=0 
              for(Ccode,Cname,Cadd,Cindate,Coutdate,Room_no,CNationality,Ccontact_no, 
              Cid_type,Cid_no) in mycursor: 
                              rec_count+=1 
                              print ('\nRecord Found......') 
                              print ("Customer details.......") 
                              print ("Customer code:",Ccode) 
                              print ("Customer name:",Cname) 
                              print ("Customer Id type:",Cid_type) 
                              print ("Customer Id Number:",Cid_no) 
                              print ("Customer address:",Cadd) 
                              print ("customer Nationality:",CNationality) 
                              print ("Check in date:",Cindate) 
                              print ("Check out date",Coutdate) 
                              print ("Room number:",Room_no) 
                              print ("Customer Contact number:",Ccontact_no) 

              if (rec_count==0): 
                              print("\nRecord not found!!") 
                              db.commit() 
                              mycursor.close() 
                              db.close() 
      else : 
            print("Invalid Input!!") 
 
# Search Customer 
# ******************* 
 
def search(): 
      db=mysql.connector.connect(host='localhost',user='root',password='root',database= 
      'HOTEL_MANAGEMENT') 
      mycursor=db.cursor() 
      Ccode=input("\nEnter Customer Code to be Searched in Hotel:") 
      qry=("select * from hoteldata where Ccode=%s") 
      rec_srch=(Ccode,) 
      mycursor.execute(qry,rec_srch) 
      rec_count=0 
      for(Ccode,Cname,Cadd,Cindate,Coutdate,Room_no,Room_rent) in mycursor: 
                          rec_count+=1 
                          print ('\nRecord Found') 
                          print ("Customer details......") 
                          print ("Customer code:",Ccode) 
                          print ("Customer name:",Cname) 
                          print ("Customer address:",Cadd) 
                          print ("Check in date:",Cindate) 
                          print ("Check out date",Coutdate) 
                          print ("Room number:",Room_no) 
                          print ("Room rent is:",Room_rent)  
      if (rec_count==0): 
                          print("\nRecord not found!!") 
                          db.commit() 
                          mycursor.close() 
                          db.close() 
 
# Delete Customer 
# ******************* 
 
def delete():
      db=mysql.connector.connect(host='localhost',user='root',password='root',database= 
      'HOTEL_MANAGEMENT') 
      mycursor=db.cursor()
      mycursor.execute("select Ccode from customer")
      rec_count=[]
      for Ccode in mycursor: 
              rec_count.append(Ccode)
      a=input("\nEnter Customer Code to be delete from Hotel:")
      for i in rec_count:
          if int(i[0])==int(a):
              qry=("delete from hoteldata where Ccode=%s") 
              qry1=("delete from customer where Ccode=%s") 
              del_rec=(a,)
              mycursor.execute(qry,del_rec) 
              mycursor.execute(qry1,del_rec)
              print("\nRecord Deleted......")
              db.commit()
              mycursor.close()
              db.close()
          elif ((int(a),)) not in rec_count:
              print("\nRecord not Found!!") 
              print("Enter valid data")
              break
 
# Update Customer 
# ******************* 
 
def update(): 
            print("\nWhich Data Should be Updated......") 
            print("1.Customer Name")
            print("2.Customer Address") 
            print("3.Customer in Date") 
            print("4.Customer out date") 
            print("5.Customer Contact number") 
            c=int(input("\nSelect your Choice:")) 
 
            if (c==1): 
                     db=mysql.connector.connect(host='localhost',user='root',password='root', 
                     database='HOTEL_MANAGEMENT') 
                     mycursor=db.cursor() 
                     Ccode=input('\nEnter Code of Customer to be Updated:')
                     Cname=input("Enter Customer Name:")     
                     q=('update hoteldata set Cname=%s where Ccode=%s') 
                     data=(Cname,Ccode) 
                     mycursor.execute(q,data) 
                     q=('update customer set Cname=%s where Ccode=%s') 
                     data=(Cname,Ccode) 
                     mycursor.execute(q,data) 
                     print('\nRecord Updated.....') 
                     db.commit() 
                     mycursor.close() 
                     db.close() 

            elif (c==2): 
                       db=mysql.connector.connect(host='localhost',user='root',password='root',database='HOTEL_MANAGEMENT')
                       mycursor=db.cursor()
                       Ccode=int(input('\nEnter Code of Customer to be Updated:'))
                       Cadd=input("Enter Customer Adrress:")     
                       q=('update hoteldata set Cadd=%s where Ccode=%s') 
                       data=(Cadd,Ccode) 
                       mycursor.execute(q,data) 
                       q=('update customer set Cadd=%s where Ccode=%s') 
                       data=(Cadd,Ccode) 
                       mycursor.execute(q,data) 
                       print('\nRecord Updated.....')           
                       db.commit() 
                       mycursor.close() 
                       db.close() 
 
            elif (c==3): 
                       db=mysql.connector.connect(host='localhost',user='root',password='root', 
                       database='HOTEL_MANAGEMENT') 
                       mycursor=db.cursor() 
                       Ccode=int(input('\nEnter Code of Customer to be Updated:'))
                       Cindate=input("Enter Customer in Date:")
                       q=('update hoteldata set Cindate=%s where Ccode=%s') 
                       data=(Cindate,Ccode) 
                       mycursor.execute(q,data) 
                       q=('update customer set Cindate=%s where Ccode=%s') 
                       data=(Cindate,Ccode) 
                       mycursor.execute(q,data)    
                       print('\nRecord Updated.....') 
                       db.commit() 
                       mycursor.close() 
                       db.close()
 
            elif (c==4): 
                       db=mysql.connector.connect(host='localhost',user='root',password='root', 
                       database='HOTEL_MANAGEMENT') 
                       mycursor=db.cursor() 
                       Ccode=int(input('\nEnter Code of Customer to be Updated:'))
                       Coutdate=input("Enter Customer out Date:")     
                       q=('update hoteldata set Coutdate=%s where Ccode=%s') 
                       data=(Coutdate,Ccode) 
                       mycursor.execute(q,data) 
                       q=('update customer set Coutdate=%s where Ccode=%s') 
                       data=(Coutdate,Ccode) 
                       mycursor.execute(q,data)           
                       print('\nRecord Updated.....')
                       db.commit() 
                       mycursor.close() 
                       db.close()
 
            elif (c==5): 
                       db=mysql.connector.connect(host='localhost',user='root',password='root', 
                       database='HOTEL_MANAGEMENT') 
                       mycursor=db.cursor() 
                       Ccode=int(input('Enter Code of Customer to be Updated:'))
                       Ccontact_no=input("Enter Customer Contact number:")     
                       q=('update customer set Ccontact_no=%s where Ccode=%s') 
                       data=(Ccontact_no,Ccode) 
                       mycursor.execute(q,data) 
                       print('\nRecord Updated.....') 
                       db.commit() 
                       mycursor.close() 
                       db.close() 

            else : 
                    print("Invalid Input!!") 

print("\n\t\t\t\t\t\t\t\t           ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░") 
print("֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎░░ WELCOME TO THE TAJ PALACE ░░֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎֎") 
print("\t\t\t\t\t\t\t\t           ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░")     
a=True
while a==True: 
       print("\n") 
       print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~") 
       print("1.About rooms of the Hotel") 
       print("2.Customer Management") 
       print("3.EXIT") 
       print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~") 
       b=input("\nEnter your choice:") 
       if (b=='1'):
             speciality() 
       elif (b=='2'):
             hotelfarecal() 
       elif (b=='3'):
             print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
             print("Thanks for visiting !!!")
             print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
             a=False
       else: 
            print("Wrong Choice")