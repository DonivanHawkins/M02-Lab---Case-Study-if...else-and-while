#My name is Donivan Hawkins
#The name of my program is "GPA_Calculator"
#This program will tell the user whether or not the inputted students GPA qualifies them for honor roll or the Deans List

import sys

student_last_name = input(str("Please enter the students last name: "))

if student_last_name == 'ZZZ':
    sys.exit("This last name is \'ZZZ\' which ends the process")

student_first_name = input(str("Please enter the students first name: "))

GPA = input("Please enter the students GPA: ")

if float(GPA)< 0:
    sys.exit("Your GPA does not fit into the parameters")

if float(GPA) >= 3.5:
    print("Your GPA means that you qualify to be on the Dean\'s List!")

if float(GPA) >= 3.25:
    print("Your GPA means that you qualify to be on the Honor Roll!")