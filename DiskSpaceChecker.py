import sys, csv, wmi, datetime, time

def main():
    ctypes.windll.kernel32.SetConsoleTitleW('DiskSpaceChecker.py')
    if len(sys.argv) < 2:
       print('No argument was parsed.')
    else:
        file = sys.argv[1] # Assign the argument passed to file.
        checkDiskSpace(file)

def checkDiskSpace(file):
    try: # Open the csv file, create a log file of todays date and begin reading each line of the file.
        with open(file) as csvfile:
            logFileName = datetime.datetime.now().strftime('%d%m%y.txt')
            readCSV = csv.reader(csvfile, delimiter =',')
            for row in readCSV: # Assign value [0] to computer name, [1] to drive letter, [2] disk threshold.
                computer = row[0]
                drive = row[1]
                threshold = int(row[2])
                c = wmi.WMI() # Create an instance of WMI.
                logFile = open(logFileName, 'a')
                try:
                    c = wmi.WMI(computer)                    
                except wmi.x_wmi:
                    print('Cannot connect to {} '.format(computer))
                    logFile.write('Cannot connect to {} '.format(computer) + '\n')
                for disk in c.Win32_LogicalDisk(SystemName=computer,Caption=drive+':'): # Retrieves the disk using drive letter from specified machine.
                    actualspace = int(disk.FreeSpace) // 1048576 # Returns available free disk space in bytes, and convert to MegaBytes.
                    if(actualspace < threshold): # If actual space is less than specified threshold.
                        print('System: {}\t DriveLetter: {}\t FreeSpace: {}Mb'.format(computer, drive, actualspace))
                        logFile = open(logFileName, 'a')
                        logFile.write('System: {}\t DriveLetter: {}\t FreeSpace: {}Mb'.format(computer, drive, actualspace)+ '\n')
                    
                    else: # If actual space is higher than specified threshold, write to log file but add 'HIGHER' to the end of the line.
                        print('System: {}\t DriveLetter: {}\t FreeSpace: {}Mb\t HIGHER'.format(computer, drive, actualspace))
                        logFile = open(logFileName, 'a')
                        logFile.write('System: {}\t DriveLetter: {}\t FreeSpace: {}Mb'.format(computer, drive, actualspace)+ ' HIGHER\n')
               
    except FileNotFoundError:
        print('File does not exist')
                    


if __name__ == '__main__':
    main()
