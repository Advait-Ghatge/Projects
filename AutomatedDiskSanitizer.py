import sys
import os
import time
import schedule

def DirectoryScanner(DirName = "Marvellous"):
    
    Border = "-" * 51
    timestamp = time.ctime()

    LogFileName = "Marvellous%s.log" %(timestamp)
    LogFileName = LogFileName.replace(" ", "_")
    LogFileName = LogFileName.replace(":", "_")
    fobj = open(LogFileName, "w")

    fobj.write(Border+"\n")
    fobj.write("This is a log file created by Marvellous Automation\n")
    fobj.write("This is a Directory Cleaner Script\n")
    fobj.write(Border+"\n")

    Ret = False

    Ret = os.path.exists(DirName)

    if (Ret == False):

        print()
        print("There is no such directory")
        return
    
    Ret = os.path.isdir(DirName)

    if (Ret == False):

        print()
        print("It is not a directory")
        return
    
    FileCount = 0
    EmptyFileCount = 0
    
    for FolderName, SubFolder, FileName in os.walk(DirName):

        for fname in FileName:

            fname = os.path.join(FolderName, fname)

            FileCount = FileCount + 1


            if (os.path.getsize(fname) == 0):   # Empty file

                EmptyFileCount = EmptyFileCount + 1
                os.remove(fname)


    fobj.write("\n")
    fobj.write(Border+"\n")

    print()
    print("-----------------Automation Report-----------------")

    fobj.write("\n")
    # print("Total files scanned :", FileCount)
    fobj.write("Total files scanned : " + str(FileCount) + "\n")

    fobj.write("\n")
    # print("Total Empty files found :", EmptyFileCount)
    fobj.write("Total Empty Files : " + str(EmptyFileCount) + "\n")
    fobj.write("\n")

    fobj.write("This log file is created at : "+timestamp+"\n")

def main():
    
    Border = "-" * 51

    print()
    print(Border)

    print("---------Marvellous Directory Automation-----------")

    print(Border)

    if (len(sys.argv) != 2):

        print()
        print("Invalid number of arguments")
        print("Please specify the name of the directory")
        return
    
    # DirectoryScanner(sys.argv[1])
    schedule.every(1).minute.do(DirectoryScanner)

    while True:
        
        schedule.run_pending()
        time.sleep(1)

    print()
    print(Border)

    print("---------Marvellous Directory Automation----------")

    print(Border)

if __name__ == "__main__":
    main()