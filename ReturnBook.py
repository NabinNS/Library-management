import date
import ListSplit
def returnbook():
    name=input("Enter name of borrower: ")
    a="Borrower "+name+".txt"
    """
    checks if there is borrower with the same name
    run try block if name is availabe else    
    """
    try:
        f=open(a,"r") #opens file in reading mode
        line=f.read()
        print(line)
        f.close()
    except:
        print("The name of the borrower is not listed")
        returnbook() #re-run function returnbook
        
    b="Returned By "+name+".txt"
    f=open(b,"w+")
    f.write("\t\t\t\tLibrary Management System  \n")
    f.write("\t\t\t\tReturned By: "+ name+"\n")
    f.write("\t\t\t\tDate: " + date.getDate()+"\n\n")
    f.write("S.N. \t Bookname \t\t\tCost\n" )
    f.close()

    total=0.0
    count=1
    for i in range(3):
        if ListSplit.bookname[i] in line:
            f=open(b,"a")
            f.write(str(count)+"\t"+ListSplit.bookname[i]+"\t\t\t$"+ListSplit.cost[i]+"\n")
            f.close()
            count=count+1
            ListSplit.quantity[i]=int(ListSplit.quantity[i])+1
            total+=float(ListSplit.cost[i])
            f=open("Stock.txt","w+")
            for i in range(3):
                f.write(ListSplit.bookname[i]+","+ListSplit.authorname[i]+","+str(ListSplit.quantity[i])+","+"$"+ListSplit.cost[i]+"\n")
            f.close()
    f=open(b,"a")
    f.write("\t\t\t\t---------------------")
    f.write("\n\t\t\t\t---------------------")
    f.write("\n\t\t\t\t  Total Price:\t"+"$"+str(total))
    f.close()
    """
    Checks if book is returned late or not
    """

    late=input("Is the book returned late? Press Y for yes and N for no ")
    if (late.upper()=="Y"):
        days=int(input("By how many days is book returned late?  "))
        print("Since book is returned late. You will be charged fine ")
        print("\nHere is your bill\n")
        fine=float(total*(20/100)+days) #calculate fine
        f=open(b,"a")
        f.write("\n\t\t\t\t  Total Fine:\t$"+str(fine))
        total=total+fine
        f.write("\n\t\t\t\t*-------------------*")
        f.write("\n\t\t\t\t  Grand Total:\t$"+str(total))
        f.close()
        f1=open(b,"r")
        l=f1.read()
        print(l)
        f1.close()
        
        print("\nThank you for borrowing book with us\n")
        
    elif (late.upper()=="N"):
        print("\nHere is your bill\n")
        f=open(b,"a")
        fine=0.0
        f.write("\n\t\t\t\t  Total Fine:\t$"+str(fine))
        total=total+fine
        f.write("\n\t\t\t\t*-------------------*")
        f.write("\n\t\t\t\t  Grand Total:\t$"+str(total))
        f.close()
        f2=open(b,"r")
        l=f2.read()
        print(l)
        f2.close()
    
        print("Thank you for borrowing book with us")

        
    
            
            
