import ListSplit
import date
def borrowBook():
    
    firstName=input("Enter first name: ")
    lastName=input("Enter last name: ")
    t="Borrower "+firstName+".txt"
    f=open(t,"w+") #opens file in read and write mode
    f.write("\t\t\t\tLibrary Management System  \n")
    f.write("\t\t\t\tBorrowed By: "+ firstName+" "+lastName+"\n")
    f.write("\t\t\t\tDate: " + date.getDate()+"\n\n")
    f.write("S.N. \t Bookname \t \tAuthorname\t\tCost \n" )
    
    list=[] #creating empty list
    success=False
    cost=0.0
    while success==False:
        print("Choose an option below:")
        for i in range(3):
            print("The code for borrowing",ListSplit.bookname[i],"is",i)
        print("\nEnter the book code to borrow book")


        try:
            booknumber1=int(input()) #enter a book code
            if (booknumber1<0):
                print("Invalid code")
            else:
                list.append(booknumber1) #adds entered bookcode to list
                try:
                    if(int(ListSplit.quantity[booknumber1])>0): #checks stock
                        print("\nYes, this book is availabe \n")
                        f=open(t,"a") #open in append mode
                        f.write("1. \t"+ ListSplit.bookname[booknumber1]+"\t\t"+ListSplit.authorname[booknumber1]+ "\t \t"+"$"+ListSplit.cost[booknumber1]+"\n")
                        cost=cost + float(ListSplit.cost[booknumber1])
                        f.close()
                        #deduct quantity of book
                        ListSplit.quantity[booknumber1]=  int(ListSplit.quantity[booknumber1])-1
                        f=open("Stock.txt","w+")
                        for i in range(3):
                            f.write(ListSplit.bookname[i]+","+ListSplit.authorname[i]+","+str(ListSplit.quantity[i])+","+"$"+ListSplit.cost[i]+"\n")
                        f.close()
                        
                        loop =True
                        count=1
                 
                        while loop ==True:
                            choice = str(input("Do you want to borrow more books?Press Y for yes and N for no."))
                            if(choice.upper()=="Y"):
                                count=count+1
                                print("Please select an option below:")
                                for i in range(3):
                                    print("Enter", i, "to borrow book", ListSplit.bookname[i])
                    
                                booknumber2=int(input())
                                if booknumber2 in list: #checks if the code already exists
                                    list.append(booknumber2) #add booknumber to list
                                    print("This book is already selected")
                                    list.pop() #removes last item
                                    count=count-1
                                # if book is not borrowed earlier then it runs code
                                else:
                                    list.append(booknumber2)
                                    if(int(ListSplit.quantity[booknumber2])>0): #checks for stock
                                        print("\nYes, this book is availabe \n")
                                        file= open(t,"a")
                                        file.write(str(count) +". \t"+ ListSplit.bookname[booknumber2]+"\t\t"+ListSplit.authorname[booknumber2]+"\t \t"+"$"+ListSplit.cost[booknumber2]+"\n")
                                        file.close()
                                        cost=cost+float(ListSplit.cost[booknumber2])
                                
                                        ListSplit.quantity[booknumber2]=int(ListSplit.quantity[booknumber2])-1
                                        f=open("Stock.txt","w+")
                                        for i in range(3):
                                            f.write(ListSplit.bookname[i]+","+ListSplit.authorname[i]+","+str(ListSplit.quantity[i])+","+"$"+ListSplit.cost[i]+"\n")
                                        f.close()
                                        success=False
                                        
                                    else:
                                        loop=False
                                        break
            
                            elif(choice.upper()=="N"):
                                print ("\nThank you for borrowing books from us. \n")
                                print("")
                                loop=False
                                success=True
                            else:
                                print("please choose as instructed")
                            
                        file=open(t,"a")
                        file.write("\n"+"\t\t\t\t\t\t------------------")
                        file.write("\n"+"\t\t\t\t\t\t------------------")
                        file.write("\n"+"\t\t\t\t\t\t"+"Total cost: $"+str(cost)) #adds total cost at the end to file
                        file.close()
                        print("\nHere is the detail of your borrowing\n")
                        f=open(t,"r")
                        l=f.read()
                        print(l)

                    else:
                        print("Sorry,this book is currently out of stock. Please contact us in few days.")
                    
                    
                  
        
                except:
                    print("Sorry, book code not found.Please check.")
        except ValueError:
             print("Please,Enter correct book code.")

    
