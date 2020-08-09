import csv
import rhinoscriptsyntax as rs


def CSVbuilding():
    #prompt the user for a file to import
    filter = "CSV file (Subject.csv)
    filename = rs.OpenFileName("Open Point File", filter)
    if not filename: return

    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            print(row['Use'], row['Square Footage'])
#            print(row)

##########################################################################
# Check to see if this file is being executed as the "main" python
# script instead of being used as a module by some other python script
# This allows us to use the module which ever way we want.
if( __name__ == "__main__" ):
    CSVbuilding()