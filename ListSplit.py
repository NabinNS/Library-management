def read_data(filename): #passing parameter
    file=open("Stock.txt","r")
    lines=file.readlines() #read lines 
    file.close()
    return lines
raw_data=read_data("Stock.txt")


def process_data(raw_data):
    data=[]
    for line in raw_data:
        data.append(line.replace('\n','').split(','))      
    return data
data=process_data(raw_data)


bookname=[]
authorname=[]
quantity=[]
cost=[]

def listSplit():
    for i in range (len(data)):
        index=0
        for j in data[i]:
            if(index==0): #adds books to list bookname
                bookname.append(j)
            elif(index==1): #adds author to list author name
                authorname.append(j)
            elif(index==2): #adds quantity to list quantity
                quantity.append(j)
            elif(index==3): #add cost to list cost
                cost.append(j.strip("$")) #strip removes "$" for further calculation
            index=1+index








            
