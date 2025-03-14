print("""
__________________________________________
    MuscleForge PowerPlay Fitness Hub

          <Gym Management System>
__________________________________________
""")

import mysql.connector
mydb = mysql.connector.connect(host='localhost',user='root',passwd='2N57j$~L')
mycursor = mydb.cursor()

# Creating database
mycursor.execute("create database if not exists GymDB")
mycursor.execute("use GymDB")
mycursor.execute("create table if not exists fees(Bronze int,Silver int,Gold int,Platinum int NOT NULL)")
mycursor.execute("create table if not exists login(username varchar(25),password varchar(25) NOT NULL)")
mycursor.execute("create table if not exists member(MID int,Name varchar(25),Gender char,Category varchar(25),Amount int)")
mycursor.execute("create table if not exists trainer(TID int,Name varchar(25),Age int,Gender char,Salary int)")
mycursor.execute("create table if not exists equipment(EID int,Name varchar(25),Type varchar(25),Quantity int)")
mycursor.execute("create table if not exists sno(trainer_id int, member_id int, equipment_id int)")
mydb.commit()

# Inserting data
# login
mycursor.execute("select * from login")
flag=0
for i in mycursor:
    flag=1
if flag==0:
    mycursor.execute("insert into login values('admin','1234')")
    mydb.commit()
# sno
flag=0
mycursor.execute("select * from sno")
for i in mycursor:
    flag=1
if flag==0:
    mycursor.execute("insert into sno values(0,0,0)")
    mydb.commit()
    
# Inserting fees structure
flag=0
mycursor.execute("select * from fees")
for i in mycursor:
    flag=1
if flag==0:
    mycursor.execute("insert into fees values(500,750,900,1500)")
    mydb.commit()

# Main Structure
while True:
    print('1.Login\n2.Exit')
    ch = int(input("\nEnter your choice:"))
    if ch==1:
        pwd = input("Enter your password:")
        mycursor.execute("select * from login")
        for i in mycursor:
            t_user,t_pass = i
        if t_pass==pwd:
            print("\n1.Add Trainer\n2.Add Member\n3.Remove Trainer\n4.Remove Member\n5.Modify\n6.Manage Equipment\n7.Change Password\n8.Go Back")
            choice = int(input("\nEnter your choice:"))
            # ADD TRAINER
            if choice==1:
                name=input("Enter name:")
                age=input("Enter Age:")
                gender=input("Enter Gender(M/F):")
                salary=int(input("Enter Salary:"))
                mycursor.execute("select * from sno")
                for i in mycursor:
                    t_id, m_id, e_id = i
                t_id = t_id + 1
                mycursor.execute("insert into trainer values('"+str(t_id)+"','"+name+"','"+age+"','"+gender+"','"+str(salary)+"')")
                mycursor.execute("update sno set trainer_id='"+str(t_id)+"'")
                mydb.commit()
                print(f"Trainer added successfully with TID: T00{t_id}\n")
            # ADD MEMBER
            elif choice==2:
                name=input("Enter name:")
                gender=input("Enter Gender(M/F):")
                print("\n1.Bronze---> amount-> 6000 [500 monthly]\n2.Silver---> amount-> 9000 [750 monthly]\n3.Gold---> amount->10800 [900 monthly]\n4.Platinum---> amount->18000 [1500 monthly]\n")
                mycursor.execute("select * from fees")
                for i in mycursor:
                    t_bronze,t_silver,t_gold,t_platinum = i
                ch=int(input("Enter Category:"))
                if ch==1:
                    category = 'Bronze'
                    amount = t_bronze
                elif ch==2:
                    category = 'Silver'
                    amount = t_silver
                elif ch==3:
                    category = 'Gold'
                    amount = t_gold
                elif ch==4:
                    category = 'Platinum'
                    amount = t_platinum              
                mycursor.execute("select * from sno")
                for i in mycursor:
                    t_id, m_id, e_id = i
                m_id = m_id + 1
                mycursor.execute("insert into member values('"+str(m_id)+"','"+name+"','"+gender+"','"+category+"','"+str(amount)+"')")
                mycursor.execute("update sno set member_id='"+str(m_id)+"'")
                mydb.commit()
                print(f"Member added successfully with MID: M00{m_id}\n")
            # REMOVE TRAINER
            elif choice==3:
                Id=int(input("Enter TID to remove:"))
                mycursor.execute("select * from trainer")
                flag=0    
                for i in mycursor:
                    t_id = i[0]
                    if t_id==Id:
                        flag=1
                if flag==1:
                    mycursor.execute("delete from trainer where TId='"+str(Id)+"'")
                    mydb.commit()
                    print("Trainer Removed Successfully.\n")
                else:
                    print("ID Not Found!\n")
            # REMOVE MEMBER
            elif choice==4:
                Id=int(input("Enter MID to remove:"))
                mycursor.execute("select * from member")
                flag=0
                for i in mycursor:
                    m_id = i[0]
                    if m_id==Id:
                        flag=1
                if flag==1:
                    mycursor.execute("delete from member where MID='"+str(Id)+"'")
                    mydb.commit()
                    print("Member Removed Successfully.\n")
                else:
                    print("ID Not Found!\n")
            # MODIFY DATA
            elif choice==5:
                while True:
                    print("\n1.Plans\n2.Trainer Data\n3.Member Data\n4.Go Back\n")
                    ch=int(input("Enter your choice:"))
                    if ch==1:
                        print("1.Bronze\n2.Silver\n3.Gold\nPlatinum\n")
                        plan=int(input("Enter plan to update:"))
                        if plan==1:
                            amt=int(input("Enter new monthly amount:"))
                            mycursor.execute("update fees set Bronze='"+str(amt)+"'")
                            mydb.commit()
                            print("Plan Updated Successfully.\n")
                        elif plan==2:
                            amt=int(input("Enter new monthly amount:"))
                            mycursor.execute("update fees set Silver='"+str(amt)+"'")
                            mydb.commit()
                            print("Plan Updated Successfully.\n")
                        elif plan==3:
                            amt=int(input("Enter new monthly amount:"))
                            mycursor.execute("update fees set Gold='"+str(amt)+"'")
                            mydb.commit()
                            print("Plan Updated Successfully.\n")
                        elif plan==4:
                            amt=int(input("Enter new monthly amount:"))
                            mycursor.execute("update fees set Platinum='"+str(amt)+"'")
                            mydb.commit()
                            print("Plan Updated Successfully.\n")
                     
                    elif ch==2:
                        Id=int(input("Enter TID to edit:"))
                        mycursor.execute("select * from trainer")
                        flag=0
                        for i in mycursor:
                            t_id = i[0]
                            if t_id==Id:
                                flag=1
                        if flag==1:
                            print("1.Name\n2.Age\n3.Salary\n")
                            ch=int(input("Enter your choice:"))
                            if ch==1:
                                name=input("Enter new name:")
                                mycursor.execute("update trainer set Name='"+name+"' where TId='"+str(Id)+"'")
                                mydb.commit()
                                print("Changes made successfully.\n")
                            elif ch==2:
                                age=int(input("Enter new age:"))
                                mycursor.execute("update trainer set Age='"+str(age)+"' where TId='"+str(Id)+"'")
                                mydb.commit()
                                print("Changes made successfully.\n")
                            elif ch==3:
                                salary=int(input("Enter new salary:"))
                                mycursor.execute("update trainer set Salary='"+str(salary)+"' where TId='"+str(Id)+"'")
                                mydb.commit()
                                print("Changes made successfully.\n")
                        else:
                            print("ID Not Found!\n")
                            
                    elif ch==3:
                        Id=int(input("Enter MID to edit:"))
                        mycursor.execute("select * from member")
                        flag=0
                        for i in mycursor:
                            m_id = i[0]
                            if m_id==Id:
                                flag=1
                        if flag==1:
                            print("1.Name\n2.Category\n")
                            ch=int(input("Enter your choice:"))
                            if ch==1:
                                name=input("Enter new name:")
                                mycursor.execute("update member set Name='"+name+"' where MId='"+str(Id)+"'")
                                mydb.commit()
                                print("Changes made successfully...\n")
                            elif ch==2:
                                print("1.Bronze\n2.Silver\n3.Gold\n4.Platinum\n")
                                mycursor.execute("select * from fees")
                                for i in mycursor:
                                    t_bronze,t_silver,t_gold,t_platinum = i
                                ch1=int(input("Enter new category:"))
                                if ch1==1:
                                    category = 'Bronze'
                                    amount = t_bronze
                                elif ch1==2:
                                    category = 'Silver'
                                    amount = t_silver
                                elif ch1==3:
                                    category = 'Gold'
                                    amount = t_gold
                                elif ch1==4:
                                    category = 'Platinum'
                                    amount = t_platinum 
                                mycursor.execute("update member set Category='"+category+"', Amount='"+str(amount)+"' where MId='"+str(Id)+"'")
                                mydb.commit()
                                print("Changes made successfully...\n")
                        else:
                            print("ID Not Found!\n")
                            
                    elif ch==4:
                        break
            # MANAGING EQUIPMENT
            elif choice==6:
                print("\n1.Add Equipment\n2.Remove Equipment\n3.Update Equipment\n4.View Equipment\n5.Go Back\n")
                ch=int(input("Enter your choice:"))
                if ch==1:
                    name=input("Enter Equipment Name:")
                    type=input("Enter Equipment Type:")
                    qty=int(input("Enter Quantity:"))
                    mycursor.execute("select * from sno")
                    for i in mycursor:
                        t_id, m_id, e_id = i
                    e_id = e_id + 1
                    mycursor.execute("insert into equipment values('"+str(e_id)+"','"+name+"','"+type+"','"+str(qty)+"')")
                    mycursor.execute("update sno set equipment_id='"+str(e_id)+"'")
                    mydb.commit()
                    print(f"Equipment Added Successfully with EID: E00{e_id}\n")
                elif ch==2:
                    eid = int(input("Enter EID to remove:"))
                    mycursor.execute("select * from equipment")
                    flag = 0
                    for i in mycursor:
                        e_id = i[0]
                        if e_id == eid:
                            flag = 1
                    if flag == 1:
                        mycursor.execute("delete from equipment where EID='" + str(e_id) + "'")
                        mydb.commit()
                        print("Equipment Removed Successfully.\n")
                    else:
                        print("ID Not Found!\n")
                elif ch==3:
                    eid = int(input("Enter EID to update:"))
                    mycursor.execute("select * from equipment")
                    flag = 0
                    for i in mycursor:
                        e_id = i[0]
                        if e_id == eid:
                            flag = 1
                    if flag == 1:
                        print("1.Name\n2.Type\n3.Quantity\n")
                        ch1 = int(input("Enter your choice to modify:"))
                        if ch1 == 1:
                            new_name = input("Enter new equipment name:")
                            mycursor.execute("update equipment set Name='" + new_name + "' where EID='" + str(eid) + "'")
                            mydb.commit()
                            print("Equipment name updated successfully.\n")
                        elif ch1 == 2:
                            new_type = input("Enter new equipment type:")
                            mycursor.execute("update equipment set Type='" + new_type + "' where EID='" + str(eid) + "'")
                            mydb.commit()
                            print("Equipment type updated successfully.\n")
                        elif ch1 == 3:
                            new_qty = int(input("Enter new quantity:"))
                            mycursor.execute("update equipment set Quantity='" + str(new_qty) + "' where EID='" + str(eid) + "'")
                            mydb.commit()
                            print("Equipment quantity updated successfully.\n")
                    else:
                        print("ID Not Found!\n")
                elif ch==4:
                    print("\nDisplaying All Equipment\n-------------------------")
                    mycursor.execute("select * from equipment")
                    for row in mycursor:
                        print(f"{row[1]} x {row[3]}")
                    print()
                elif ch==5:
                    break                    
            # CHANGE PASSWORD
            elif choice==7:
                old_pwd=input("enter old password:")
                mycursor.execute("select * from login")
                for i in mycursor:
                    t_user,t_pass = i
                if t_pass==old_pwd:
                    new_pwd=input("Enter new password:")
                    mycursor.execute("update login set password='"+new_pwd+"'")
                    mydb.commit()
                    print("Password Updated Successfully.\n")
                else:
                    print("Wrong password!\n")

            elif choice==8:
                break          
       
        else:
            print("Wrong password...\n")
      
    elif ch==2:
        break
    
