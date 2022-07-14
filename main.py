import ListSplit
import BorrowBook
import date
import ReturnBook

def start():
    while(True): #set while to true for continuous looping
        #prints following information as a menu
        print("--------->Welcome to the library management system<---------")
        print("------------------------------------------------------------")
        print("Enter 1: To Display available books")
        print("Enter 2: To Borrow a book")
        print("Enter 3: To return a book")
        print("Enter 4: To exit")
        try: #Try block to look errors
            #ask user to input a number in int format
            choice=int(input("Select a choice from 1-4: "))
            print()
            if(choice==1):
                ListSplit.listSplit() #calls function listSplit from ListSplit module
                # displaing information in form of table
                print ("The availabe books in our library are\n")
                print("S.N\tBook Name\t\tAuthor Name\t\tQuantity\tCost"+"\n")
                file=open("Stock.txt","r") #open file in read form
                for i in range(3):
                    #prints information stored in Stock.txt file
                    print(str(i+1)+"\t"+ListSplit.bookname[i]+"\t\t"+ListSplit.authorname[i]+"\t\t"+ListSplit.quantity[i]+" pcs"+"\t\t$"+ListSplit.cost[i]+"\n")
                print()
                file.close() 
                
            elif(choice==2):
                #calls function from ListSplit and BorrowBook
                ListSplit.listSplit()
                BorrowBook.borrowBook()
                

            elif(choice==3):
                #calls function from ListSplit and ReturnBook
                ListSplit.listSplit()
                ReturnBook.returnbook()
                
            elif(choice==4):
                print("Thank you for using our library")
                break #Ends program
                
            else:
                print("enter number from 1 to 4")
                
        except ValueError:
            #prints following information if wrong number is given
            print("please input number from 1 to 4\n")
#run function start
start()








