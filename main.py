import mysql.connector

con=mysql.connector.connect(host="localhost",user="root",passwd="sid25136666",database="bsbakery")
print("__________________Welcome User___________________")
print("              B.S BAKERY PVT LTD")
cursor=con.cursor()
cursor.execute("use bsbakery")

#ITEMS IN STORE
def items():
    item="select * from product"
    cursor.execute(item)
    res=cursor.fetchall()
    t=(['serial_no','products','cost','totalUnits'])
    for Serial_no,Product,Cost,TotalUnits in res:
        print(Serial_no,':',"\t",Product,":","\t","Cost",Cost,':',"\t","Total Units",":",TotalUnits)


#ITEMS AVAILABLE IN KITCHEN
def kitchen():
    kit="select * from ration"
    cursor.execute(kit)
    fet=cursor.fetchall()
    x=(['Ration','Quantity in KG'])
    for Ration,Quantity_In_Kg in fet:
        print(">" ,Ration,":","\t","Quantity",Quantity_In_Kg,"Kg")

#GROCERY ITEMS
def grocery():
    groc="select * from ration"
    cursor.execute(groc)
    det=cursor.fetchall()
    x=(['Ration'])
    for Ration,Quantity_In_Kg in det:
        print(">" ,Ration,":")


#CROCKERY ITEMS
def crockery():
    croc="select sno,itemname from crockery order by sno"
    cursor.execute(croc)
    let=cursor.fetchall()
    q=(["sno","itemname"])
    for sno,itemname in let:
        print(sno,"\t",itemname)


#RETAILERS FOR ORDER PURCHASES#
def retailer():
    retail="select * from retailer"
    cursor.execute(retail)
    ret=cursor.fetchall()
    x=(['No','retailerID','retailer','phoneno'])
    for No,retailerID,retailer,phoneno in ret:
        print(No,":","\t","RetailerID",retailerID,"\t",retailer,"\t","Phone No:",phoneno)


#FUNCTION TO PLACE ORDER
def order():
    print("1 For Grocery:")
    print("2 For Crockery:")
    x=int(input("What do you want to order for your kitchen:"))
    if x==1:
        grocery()
        print()
        k=int(input("Select any one grocery from 1-12:"))
        retailer()
        j=int(input("Select any retailer from 1-3:"))
        if (0<j<4):
            o=int(input("How much quantity to be ordered(in Kgs)?"))
            conf=input("NOTE: Are you sure to place this order? (Y/N):")
            if conf=="Y" or conf=="y":
               print()
               print("Your Order has been placed!!!")
            else:
               print("Order is being cancelled.... No Order placed:") 
               order()          
        else:
            print("No retailer with such no.!!")

    elif x==2:
        crockery()
        print()
        k=int(input("Select any one crockery from 1-10:"))
        retailer()
        a=int(input("Select any retailer from 1-3:"))
        if (0<a<4):
            oe=int(input("How many units?"))
            confirm=input("NOTE: Are you sure to place this order? (Y/N):")
            if confirm=="Y" or confirm=="y":
               print()
               print("Your Order has been placed!!!")
            else:
               print("Order is being cancelled.... No Order placed:") 
               order()          
        else:
            print("No retailer with such no.!!")


    else:
        print("Wrong Input")


#FUNCTION TO UPDATE VALUES OF STORE#
def updatestore():
    items()
    print("NOTE THAT ONLY TOTALUNITS ARE CHANGABLE")
    p=int(input("Enter existing unitvalue:"))
    q=int(input("Enter new value:"))
    x="update product SET Totalunits={} where Totalunits={}".format(q,p)
    cursor.execute(x)
    con.commit()
    print("Value changed!")


#FUNCTION TO UPDATE VALUES OF KITCHEN# 
def updateration():
    kitchen()
    print("NOTE THAT ONLY QUANTITIES ARE CHANGABLE")
    p=int(input("Enter existing Quantity_In_Kg value:"))
    q=int(input("Enter new value:"))
    x="update ration SET Quantity_In_Kg={} where Quantity_In_Kg={}".format(q,p)
    cursor.execute(x)
    con.commit()
    print("Value changed!")


print()
print()
print("                           |                 FOOD PROCESSING AND ORDER MANAGEMENT            |")
print("                           |MADE BY- SHAURYA GAUR,SIDDHARTH SILORI,SNEHA BALODHI,SOURABH NEGI|")
print("                           |ROLL NO-    53           54               55            56       |")
print('  ')
name=input("Enter your name:")
phone=int(input("Enter your ID:"))

#MAINCODE
def Main():
    ch=''
    while ch!="N" or ch!="n":

        def funct():
            print("\n\nPLEASE CHOOSE\n1 TO ENTER \n2 TO EXIT")
            choice=int(input("Enter your choice:"))
            if choice==2:
                return
            elif choice==1:
                print('  ')
                print("Press 1 to Check Items In The Store")
                print("Press 2 to Check Ration")
                print("Press 3 to Order Ration")
                print("Press 4 to Update Records")
                print("Press 5 to EXIT")
                e=int(input("Enter your choice:"))
                if e==5:
                    return
                elif e==1:
                    print("Items Available In The Store:")
                    items()
                    funct()
                elif e==2:
                    print ("Ration available in the kitchen:")
                    kitchen()
                    funct()
                elif e==3:
                    order()
                    funct()
                elif e==4:
                    print("Press 1 To update Items in Store")
                    print('Press 2 To update items in Ration')
                    p=int(input("Enter your choice:"))
                    if p==1:
                        updatestore()
                    elif p==2:
                        updateration()
                    else:
                        print("Wrong entry!!!")
                else:
                    print("Wrong Input")
                    funct()
        funct()            

    ch=input("ARE YOU SURE TO EXIT FROM PROGRAM(Y/N)?")
    if ch=='y' or ch=='Y':
        exit()
Main()        

