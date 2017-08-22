Info = []


def Gatherinfo():
    id = len(Info)
    #if Info.Count > 0 Get the max Id from the list  
    while True:
        option = input("Give info: enter 'y' to begin 'n' to stop.")
        if(option == "n" or option == "N"):
            #write to file and save input
            break
        elif(option == "y" or option == "Y"):
            name = input("Enter info: name.")
            if Len(name)>0:
                id = id+1
                AddInfo(id,name,True)
            continue


def AddInfo(Id,description,addToFile = False):
    dictItem = {}
    dictItem[Id]= description
    Info.append(dictItem)
    print(Info)
    if(addToFile):
        WriteDataToFile(dictItem)



def ReadDatafromFile():
    try:
        filehandle = open("Storage.txt","r")
        for item in filehandle.readlines():
            print(item)
            keyValuepair = item.split(",")
            AddInfo(keyValuepair[0],keyValuepair[1])
        filehandle.close()
    except Exception:
        print(Exception.with_traceback)
        print("Could not open file")

def WriteDataToFile(dictItem):
    try:
        filehandle = open("Storage.txt","a")
        #filehandle.write(dictItem[Id]+","+dictItem.keys +"\n")
        for k,v in dictItem.items():
           filehandle.write(str(k) + ","+ v +"\n")
        filehandle.close()
    except Exception:
        print(Exception.with_traceback)
        print("Could not open file")
    

ReadDatafromFile()
Gatherinfo()

