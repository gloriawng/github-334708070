def quitcheck():
    quit=input('Enter QUIT if you wish to exit, otherwise hit Enter:')
    if quit.upper()=="QUIT":
        print("QUITTING\ngoodbye")
        return " "

def makecheck(make):
    checking=0
    for i in range(4):
        if make==makemenu[i]:
            checking+=1
    
    if make.upper()=="QUIT":
        print("QUITTING\ngoodbye")
        return " "
    elif checking==1:
        return make
    else: 
        make=input("Enter VALID make of your car (from menu) or QUIT if you wish to exit: ")
        return makecheck(make)

def sizeprompt(make):
    if make=="EDSEL":
        print("Size options: 6 or 8 cylinders")
    elif make=="AUSTIN":
        print("Size options: 4 or 6 cylinders")
    elif make=="CATEPILLAR":
        print("Size options: 15 or 20 cylinders")
    elif make=="JAGUAR":
        print("Size options: 6 or 12 cylinders")

def checksize(size):
    if size.upper()=="QUIT":
        print("QUITTING\ngoodbye")
        return " "
    elif make=="EDSEL" and (size=="6" or size=="8"):
        return size
    elif make=="AUSTIN" and (size=="4" or size=="6"):
        return size
    elif make=="CATEPILLAR" and (size=="15" or size=="20"):
        return size
    elif make=="JAGUAR" and (size=="6" or size=="12"):
        return size
    else: 
        size=input("Enter the VALID size from make (or QUIT if you wish to exit): ")
        return checksize(size)

def yearcheck(year):
    if(year>=1985 and year<=2005):
        return year
    else: 
        year=int(input("Enter VALID year manufactured: "))
        return yearcheck(year)

#Start of program
makemenu=["EDSEL","AUSTIN","CATEPILLAR","JAGUAR"]

start=input("Start? (Yes or No): ")

if(start=="Yes"):
    print("Make Menu",makemenu)
    make=input("Enter make of your car from menu (or QUIT if you wish to exit): ")
    make=make.upper()
    make=makecheck(make)
    if make==" ":
        quit()

    sizeprompt(make)
    size=input("Enter the size from menu (or QUIT if you wish to exit): ")
    size=checksize(size)
    if size==" ":
        quit()

    if quitcheck()==" ":
        quit()
    year=int(input("Enter year manufactured: "))
    year=yearcheck(year)

    #determine filter
    filtermake=make[0]
    filteryear=year%100
    if int(size)<10:
        airfiltertag=filtermake+str(filteryear)+"0"+str(size)
    else:
        airfiltertag=filtermake+str(filteryear)+str(size)
    
    #printing make, year, number of cylinders, and filter model number
    print("Make:",make)
    print("Size:",size)
    print("Year:",year)
    print("Air Filter Model:",airfiltertag)
    print("goodbye")