#importing the csv library
import csv
#creating a new csv file where all changes will be saved
outfile = open('CSVOutput.csv ', 'w')
#opening the database
with open('employeedata.csv', 'r') as csv_file:
    #creating a reading var
    csv_reader = csv.reader(csv_file)
    header = next(csv_reader)
    #iterating through the different rows
    for row in csv_reader:
        name = row[0]
        contact =row[1]
        #while iterating through the third column i change the domain name once
        email = row[2]
        address =row[3]
        if 'helpinghands.cm' in email:
            upemail=(email).replace('helpinghands.cm','handsinhands.org')
        line = "{},{},{},{}\n".format(name, contact,upemail, address)
        outfile.write(line)
outfile.close()