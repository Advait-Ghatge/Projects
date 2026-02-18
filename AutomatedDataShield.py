import os
import sys
import time
import schedule
import shutil
import hashlib
import zipfile

def make_zip(folder):

    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")

    zip_name = folder + "_" + timestamp + ".zip"

    # Open the zip file

    zobj = zipfile.ZipFile(zip_name, "w", zipfile.ZIP_DEFLATED)

    for root, dirs, files in os.walk(folder):

        for file in files:

            full_path = os.path.join(root, file)

            relative = os.path.relpath(full_path, folder)

            zobj.write(full_path, relative)

    zobj.close()

    return zip_name


def Calculate_Hash(path):

    hobj = hashlib.md5()

    fobj = open(path, "rb")

    while True:

        Data = fobj.read(1024)

        if not Data:
            break

        else:
            hobj.update(Data)

    fobj.close()

    return hobj.hexdigest()

def BackupFiles(Source, Destination):

    copied_files = []

    print("Creating the backup folder for backup process")

    os.makedirs(Destination, exist_ok=True)

    for root, dirs, files in os.walk(Source):

        for file in files:

            src_path = os.path.join(root, file)
            
            relative = os.path.relpath(src_path, Source)

            dest_path = os.path.join(Destination, relative)

            os.makedirs(os.path.dirname(dest_path), exist_ok=True)

            # Copy the files if its new

            if ((not os.path.exists(dest_path)) or (Calculate_Hash(src_path) != Calculate_Hash(dest_path))) :

                shutil.copy2(src_path, dest_path)
                copied_files.append(relative)

            # print()
            # print("CheckSum is :", Calculate_Hash(src_path))

    return copied_files

def MarvellousDataShieldStart(Source = "Data"):

    Border = "-" * 50

    BackupName = "Marvellous_Backup"

    print()
    print(Border)
    print("Backup process started successfully at :", time.ctime())
    print(Border)

    files = BackupFiles(Source, BackupName)

    zip_file = make_zip(BackupName)

    print()
    print(Border)
    print("Backup completed successfully")
    print("Files copied -", len(files))
    print("Zip File gets created :", zip_file)
    print(Border)



def main():

    print()
    Border = "-" * 50
    
    print(Border)
    print("----------Marvellous Data Shield System-----------")
    print(Border)

    if (len(sys.argv) == 2):

        if (sys.argv[1] == "--h" or sys.argv[1] == "--H"):

            print()
            print("This script is used to create : ")
            print("1 : Takes Auto-Backup at given time")
            print("2 : Backs up only new and updated files")
            print("3 : Create an archive of the backup periodically")
        
        
        elif (sys.argv[1] == "--u" or sys.argv[1] == "--U"):

            print()
            print("Use the automation script as - ")
            print("ScriptName.py 'Time Interval in minutes' 'Source Directory'")
            print("Source Directory : Name of directory to be backed up")

        else:

            print()
            print("Unable to proceed as there is no such option")
            print("Please use --h or --u to get more details")

  
    # Python Demo.py 5 Data

    elif (len(sys.argv) == 3):

        print()
        print("Inside project logic")

        print()
        print("Time interval :", sys.argv[1])
        print("Directory Name :", sys.argv[2])


        # Apply the scheduler

        schedule.every(int(sys.argv[1])).minutes.do(MarvellousDataShieldStart, sys.argv[2])

        print()
        print(Border)
        print("Data Shield System started successfully")

        print("Directory created with name :", sys.argv[2])
        print("Time interval in minutes :", sys.argv[1])

        print()
        print("Press Ctrl + C to stop the execution")
        print(Border)

        # Wait till abort

        while True :

            schedule.run_pending()
            time.sleep(1)


    else:
        print()
        print("Invalid number of command line arguments")
        print("Unable to proceed as there is no such option")
        print("Please use --h or --u to get more details")

    
    print()
    print(Border)
    print("----------Thank you for using our script----------")
    print(Border)


if __name__ == "__main__":
    main()