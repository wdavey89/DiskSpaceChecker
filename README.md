# DiskSpaceChecker
This program reads in a CSV file, containing the computer name, drive letter, and disk space threshold in MB. For each computer name and drive letter, the actual disk space is checked and compared to the threshold set in your csv file, and the results are written to the log file. You'll now be able to check a bunch of machines on the network to find out which ones have less available disk space than what you've set.

The output of the program looks like the following:
System: pc-name         DriveLetter: C  FreeSpace: 39373Mb
System: pc-name         DriveLetter: D  FreeSpace: 58648Mb      HIGHER

The C: drive was set to 70000Mb threshold, but actually only has 39373Mb available.
The D: drive was set to 40000Mb threshold, but actually has 58648Mb hence it is 'higher' than what you'd want it to be which is good.

You can add all your machines on the network to the CSV file and it'll return the available disk space for the drive letters you specify.

This was a project I worked on at home, but to be used in a domain environment as a infrastructure monitoring tool.
