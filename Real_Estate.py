print("Would you like to rent a property or buy it")
a=input("please enter your choice")
import mysql.connector as ms
con=ms.connect(host="localhost", user="root", passwd="root", database="vsh")
m=con.cursor();
m=con.cursor(buffered=True)
if a=='buy' or a=='Buy':
    choice=int(input("choose 1 to buy a property & choose 2 to exit"))
    if choice==1:
        m.execute("use vsh")
        m.execute("create table properties(s_no int,n_house varchar(20),h_no varchar(20),type varchar(20),location varchar(20),size varchar(20),amenities varchar(20),price_in_Cr varchar(20))")
        m.execute("insert into properties values(1,'the gables','h_no=358','independant house','ganganagar','2BHK','has a pool','1Cr')")
        m.execute("insert into properties values(2,'the woodland','h_no=451','independant house','ganganagar','3BHK','fully solar powered','1Cr')")
        m.execute("insert into properties values(3,'the orchard','h_no=301','Apartment','sanjaynagar','2BHK','gym&spa','3Cr')")
        m.execute("insert into properties values(4,'samruddi nilaya','h_no=101','independant house','sadashivnagar','4BHK','mini garden','5Cr')")
        m.execute("insert into properties values(5,'Sneha Kuteer','h_no=402','Apartment','jayanagar','3BHK','power backup','2Cr')")
        m.execute("insert into properties values(6,'the goldfinch','h_no=302','Apartment','sanjaynagar','4BHK','tennis court','4Cr')")
        con.commit()
        m.execute("create table filters(s_no int,filters varchar(20))")
        m.execute("insert into filters values(1,'location')")
        m.execute("insert into filters values(2,'size')")
        m.execute("insert into filters values(3,'price_in_Cr')")
        m.execute("insert into filters values(4,'type')")
        con.commit()
        print("properties:")
        m.execute("select s_no,n_house,location,type from properties")
        data=m.fetchall()
        for i in data:
            print(i)
        while True:
            f=input("would you like to use filters to find your dream home?(y/n)")
            if f=='y' or f=='Y':
                print("Available filters:")
                m.execute("select * from filters")
                data=m.fetchall()
                for i in data:
                    print(i)
                choice=input("enter filter of choice")
                if choice=="type":
                    print("types of houses available are:")
                    m.execute("select distinct type from properties")
                    data=m.fetchall()
                    for i in data:
                        print(i)
                    ch=input("enter type of property you want to buy:")
                    if ch=='apartment' or ch=="Apartment":
                        m.execute("select * from properties where type='Apartment'")
                        data=m.fetchall()
                        for i in data:
                            print(i)
                    elif ch=='independant house' or ch=="Independant house":
                        m.execute("select * from properties where type='independant house'")
                        data=m.fetchall()
                        for i in data:
                            print(i)
                elif choice=="location":
                    print("locations where properties are available:")
                    m.execute("select distinct location from properties")
                    data=m.fetchall()
                    for i in data:
                        print(i)
                    ch=input("enter location in which you want to buy a properties:")
                    if ch=='sanjaynagar':
                        m.execute("select * from properties where location='sanjaynagar'")
                        data=m.fetchall()
                        for i in data:
                            print(i)
                    elif ch=='ganganagar':
                        m.execute("select * from properties where location='ganganagar'")
                        data=m.fetchall()
                        for i in data:
                            print(i)
                    elif ch=='jayanagar':
                        m.execute("select * from properties where location='jayanagar'")
                        data=m.fetchall()
                        for i in data:
                            print(i)
                    elif ch=='sadashivnagar':
                        m.execute("select * from properties where location='sadashivnagar'")
                        data=m.fetchall()
                        for i in data:
                            print(i)
                    else:
                        print("invalid input")
                elif choice=="size":
                    print("available sizes of properties :")
                    m.execute("select distinct size from properties")
                    data=m.fetchall()
                    for i in data:
                        print(i)
                    ch=input("enter size of properties you want to buy:")
                    if ch=="2BHK" or ch=="2bhk":
                        m.execute("select * from properties where size='2BHK'")
                        data=m.fetchall()
                        for i in data:
                            print(i)
                    elif ch=="3BHK" or ch=="3bhk":
                        m.execute("select * from properties where size='3BHK'")
                        data=m.fetchall()
                        for i in data:
                            print(i)
                    elif ch=="4BHK" or ch=="4bhk":
                        m.execute("select * from properties where size='4BHK'")
                        data=m.fetchall()
                        for i in data:
                            print(i)
                elif choice=="price_in_Cr" or choice=="price" or choice=="Price":
                    print("price range of properties:")
                    m.execute("select distinct price_in_Cr from properties")
                    data=m.fetchall()
                    for i in data:
                        print(i)
                    ch=input("enter price of properties you want to buy:")
                    if ch=="1" or ch=="1cr" or ch=="1Cr":
                        m.execute("select * from properties where price_in_Cr='1Cr'")
                        data=m.fetchall()
                        for i in data:
                            print(i)
                    elif ch=="2Cr" or ch=="2cr" or ch=="2":
                        m.execute("select * from properties where price_in_Cr='2Cr'")
                        data=m.fetchall()
                        for i in data:
                            print(i)
                    elif ch=="3Cr" or ch=="3cr" or ch=="3":
                        m.execute("select * from properties where price_in_Cr='3Cr'")
                        data=m.fetchall()
                        for i in data:
                            print(i)
                    elif ch=="4Cr" or ch=="4cr" or ch=="4":
                        m.execute("select * from properties where price_in_Cr='4Cr'")
                        data=m.fetchall()
                        for i in data:
                            print(i)
                    elif ch=="5Cr" or ch=="5cr" or ch=="5":
                        m.execute("select * from properties where price_in_Cr='5Cr'")
                        data=m.fetchall()
                        for i in data:
                            print(i)
                    else:
                        print("invalid input")
            elif f=='n' or f=='N':
                while True:
                    h=int(input("Please enter property no. to get more details"))
                    if h>=1 and h<=6:
                        print("Wounderful choice, all the details of the property are given below!")
                        m.execute("select * from properties")
                        if h==1:
                            d=m.fetchone()
                            print(d)
                        elif h>1 and h<=6:
                            for i in range(1,h+1):
                                d=m.fetchone()
                            print(d)
                    ch=int(input("enter 1 to continue and 2 to go to next step"))
                    if ch==1:
                        continue
                    elif ch==2:
                        break
                    else:
                        print("invalid input")
                        break
            ch=int(input("enter 1 to proceed to billing, 2 to continue browsing,3 to exit"))
            if ch==1:
                b=int(input("enter property number you want to buy"))
                y=input("would you like to purchase the property?(y/n)")
                if y=='y' or y=='Y':
                    c=input("would you like to confirm your purchase?(y/n)")
                    if c=="y" or c=="Y":
                        print("Your purchase has been confirmed")
                        print("please submit the required details below")
                        name=input("enter name")
                        pn=int(input("enter phone number"))
                        email=input("enter email address")
                        print("""Please submit all important documents required for purchase
like adhar card in the email given below:""")
                        print("harmonioushousing@gmail.com")
                        print('''thank you for choosing harmonious housing to buy your home!
payment details will be sent to your email.''')
                        break
                    elif c=="n" or c=="N":
                        print("thank you for visiting harmoneous housing,hope to see you again")
                        break
                    else:
                        print("invalid input")
                        break
                elif y=="n" or y=="N":
                    print("thank you for visiting harmoneous housing,hope to see you again")
                    break
                else:
                    print("invalid input")
                    break
            elif ch==2:
                continue
            elif ch==3:
                print("thank you for visiting harmoneous housing,hope to see you again")
                break
            else:
                print("invalid input")
    elif choice==2:
        print("thank you for visiting harmoneous housing,hope to see you again")
    else:
        print("invalid input")
