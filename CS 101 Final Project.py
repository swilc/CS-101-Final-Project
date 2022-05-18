import json
import csv
import time

# You do not need to worry about reading data from files. Reading in all of the data to the
# maui_high, maui_waena_intermediate, and lokelani_intermediate lists is handled for you.
maui_high = []
with open("MauiHigh.csv") as maui_high_file: # opens the file with data on Maui High
    for student in maui_high_file: # this goes through the file one line at a time
        student = student.split(",") # this splits the line of data into a list
        student[-1] = student[-1].strip() # this removes the "\n" from the end of the last item
        maui_high.append(student) # this adds the item to the list

maui_waena_intermediate = []
with open("MauiWaenaIntermediate.csv") as maui_waena_intermediate_file:
    for student in maui_waena_intermediate_file:
        student = student.split(",")
        student[-1] = student[-1].strip()
        maui_waena_intermediate.append(student)

lokelani_intermediate = []
with open("LokelaniIntermediate.csv") as lokelani_intermediate_file:
    for student in lokelani_intermediate_file:
        student = student.split(",")
        student[-1] = student[-1].strip()
        lokelani_intermediate.append(student)

class Student:
    #TODO: Complete this class. You will need to add additional methods.
    def __init__(self, student_data):
        # Check if the student is in high school or in middle school.
        # If the length of "student_data" is 5, then they are in high school
        # If it is 3, then it's in middle school.
        if len(student_data) == 5:
            # Set the name and grade to the corresponding value in "student_value"
            self.name = student_data[0]
            self.grade = int(student_data[1])
            # Check if they meet the graduation requirements add set that variable to true/false
            if student_data[2] == "met":
                self.graduation_requirements = True
            else:
                self.graduation_requirements = False
            # Set the number of credits corresponding to the value in "student_value"
            self.credits = int(student_data[3])
            # Set to true/false if transferring or not
            if student_data[4] == "transferring":
                self.transferring = True
            else:
                self.transferring = False
        elif len(student_data) == 3:
            # This part runs if the student is in middle school (only three values)
            # Sets the corresponding values
            self.name = student_data[0]
            self.grade = int(student_data[1])
            self.high_school = str(student_data[2])
        else:
            # This runs if there is the wrong number of values
            print("[ERROR]>> Looks like your CSV file has the wrong number of values per student. (3 or 5)")
    
    # defines the "less than" method for students (for sorting purposes)
    def __lt__(self, other):
        # This method has already been completed for you. Do NOT mess with it (for grading reasons).
        return self.name < other.name

    # provides a string representation of a student
    def __repr__(self):
        # This method has already been completed for you. Do NOT mess with it (for grading reasons).
        return self.name + "," + str(self.grade) + "," + str(self.graduation_requirements) + "," + str(self.credits) + "," + str(self.transferring)

    # Function to change the data structure from middle to high school and fill in the blanks
    def assignBlanks(self, student_data):
        self.name = student_data[0]
        self.grade = 9
        self.graduation_requirements = False
        self.credits = 0
        self.transferring = False

    def add_student(self, student_data):
        self.name = student_data[0]
        self.grade = student_data[1]
        self.graduation_requirements = False
        self.credits = student_data[2]
        self.transferring = False
        

def menu(title, ln1="", ln2="", ln3="", enter=False):
    # Set up the blanks
    titleSpace=""
    ln1Space=""
    ln2Space=""
    ln3Space=""

    # Make sure everything is within the charachter limits
    if len(title) > 30 or len(ln1) > 30 or len(ln2) > 30 or len(ln3) > 30:
        print("Menu error!")

    ### Title bar
    # Add blank spaces
    for i in range(int((30-int(len(title)))/2)):
        titleSpace=" "+titleSpace
    # Set the line
    titleBar = ("|"+str(titleSpace)+str(title)+str(titleSpace))
    # Add the end to the line, if short one character add a space
    if int(len(titleBar)) < 31:
        titleBar = titleBar + " |"
    else:
        titleBar = titleBar + "|"

    ### First Line
    for i in range(int((30-int(len(ln1)))/2)):
        ln1Space=" "+ln1Space
    line1 = ("|"+str(ln1Space)+str(ln1)+str(ln1Space))
    if int(len(line1)) < 31:
        line1 = line1 + " |"
    else:
        line1 = line1 + "|"

    ### Second Line
    for i in range(int((30-int(len(ln2)))/2)):
        ln2Space=" "+ln2Space
    line2 = ("|"+str(ln2Space)+str(ln2)+str(ln2Space))
    if int(len(line2)) < 31:
        line2 = line2 + " |"
    else:
        line2 = line2 + "|"

    ### Third Line
    for i in range(int((30-int(len(ln3)))/2)):
        ln3Space=" "+ln3Space
    line3 = ("|"+str(ln3Space)+str(ln3)+str(ln3Space))
    if int(len(line3)) < 31:
        line3 = line3 + " |"
    else:
        line3 = line3 + "|"
    
    ### Check if the prompt should have "press enter to continue" at the bottom
    if enter == False:
        bottomBar = "+------------------------------+"
    else:
        bottomBar = "+---Press Enter to Continue!---+"

    # Print the lines
    print ("")
    print ("")
    print ("")
    print ("")
    print ("+------------------------------+")
    print (titleBar)
    print ("+------------------------------+")
    print (line1)
    print (line2)
    print (line3)
    print (bottomBar)
    print ("")
    
# new_maui_high is a list for next year's student data. When you're finished, it should contain
# a list of Student objects updated for next school year.
new_maui_high = []

# stats is a dictionary. It has already been created for you with all of the data that you need.
# All you need to take care of is updating these values. This is easy to do. If you'd like to
# set "graduating" to 74, for instance, all you have to do is:
# stats["graduating"] = 74
stats = {
    "graduating":0, # the number of students who will be graduating this year
    "graduation_rate":0.0, # the number of students graduating divided by the total number of seniors this year (NOT next year's seniors)
    "maui_waena_incoming":0, # the number of students coming to Maui High from Maui Waena Intermediate
    "lokelani_incoming":0, # the number of students coming to Maui High from Lokelani Intermediate
    "freshmen":0, # the number of freshman for next year
    "sophomores":0, # the number of sophomores for next year
    "juniors":0, # the number of juniors for next year
    "seniors":0 # the number of seniors for next year
}

test_list = []
grad_pass = 0
total_seniors = 0

# Add a progress bar
menu("Processing Data", "25%", "███▒▒▒▒▒▒▒▒▒", "(Sort Maui High)")
# Add a fake delay so you can read the text
time.sleep(1.8)

for x in range(len(maui_high)):
    new_student = Student(maui_high[x])

    if new_student.grade == 9 and new_student.credits >= 13 and new_student.transferring == False:
        new_student.grade = 10
        stats["sophomores"] += 1

    elif new_student.grade == 9 and new_student.transferring == False  and new_student.credits <= 13:
        stats["freshmen"] += 1

    elif new_student.grade == 10 and new_student.credits >= 26 and new_student.transferring == False:
        new_student.grade = 11
        stats["juniors"] += 1
    
    elif new_student.grade == 10 and new_student.transferring == False and new_student.credits <= 26:
        stats["sophomores"] += 1

    elif new_student.grade == 11 and new_student.credits >= 39 and new_student.transferring == False:
        new_student.grade = 12
        stats["seniors"] += 1

    elif new_student.grade == 11 and new_student.transferring == False and new_student.credits <= 39:
        stats["juniors"] += 1

    elif new_student.graduation_requirements == True and new_student.grade == 12 and new_student.credits >= 52:
        stats["graduating"] += 1
        grad_pass += 1
        total_seniors += 1
        continue 

    elif new_student.grade == 12:
        stats["seniors"] += 1
        total_seniors += 1
        
    else:
        test_list.append(new_student)
        continue

    new_maui_high.append(new_student)

stats["graduation_rate"] = grad_pass/total_seniors 

# Add a progress bar
menu("Processing Data", "50%", "██████▒▒▒▒▒▒", "(Sort Maui Middle)")
# Add a fake delay so you can read the text
time.sleep(1.2)

for x in range(len(maui_waena_intermediate)):
    # Create a new class for the student with the student data
    new_student = Student(maui_waena_intermediate[x])
    if new_student.grade == 8 and new_student.high_school == "Maui High":
        # Convert the format from middle to high school and fill in the blanks
        new_student.assignBlanks(maui_waena_intermediate[x])
        # Add it to the new students list
        new_maui_high.append(new_student)
        # Update stats with the new student
        stats["maui_waena_incoming"] += 1
        stats["freshmen"] += 1
    else:
        continue
    
# Add a progress bar
menu("Processing Data", "75%", "█████████▒▒▒", "(Sort Loke. Middle)")
# Add a fake delay so you can read the text
time.sleep(1.2)

for x in range(len(lokelani_intermediate)):
    # Create a new class for the student with the student data
    new_student = Student(lokelani_intermediate[x])
    if new_student.grade == 8 and new_student.high_school == "Maui High":
        # Convert the format from middle to high school and fill in the blanks
        new_student.assignBlanks(lokelani_intermediate[x])
        # Add it to the new students list
        new_maui_high.append(new_student)
        # Update stats with the new student
        stats["lokelani_incoming"] += 1
        stats["freshmen"] += 1
    else:
        continue
 
# Add a progress bar
menu("Processing Data", "100%", "████████████", "(Writing Data)")
# Add a fake delay so you can read the text
time.sleep(2.8)

### Write initial data! ###
# This is before the user can modify anything.
# Write initial data to the CSV file
new_maui_high.sort()
with open("MauiHighUpdated.csv", "w") as maui_high_updated_file:
    for student in new_maui_high:
        maui_high_updated_file.write(repr(student) + "\n")

# Write the initial stats
with open("Stats.json", "w") as stats_file:
    json.dump(stats, stats_file, indent=4)

### Main user input loop ###
while True:
    # Add the menu GUI
    menu("Choose an Option [\"q\"=quit]", "(1) Add Student", "(2) Student Lookup", "(3) Student Update")

    # Ask the user for an option
    menu_choice = input("")

    # Check to see if the user wants to quit.
    if menu_choice.lower() == "q":
        menu("Info", "Exiting code..")
        break
    elif menu_choice == "1":
        add_list2 = []
        
        menu("Add Student", "What is the student's name?")
        add_list2.append(input())

        menu("Add Student", "What is the student's grade?")
        add_list2.append(int(input()))
        
        menu("Add Student", "What is the student's credits?")
        add_list2.append(int(input()))

        add_new_student = Student(add_list2)
        
        add_new_student.add_student(add_list2)
        
        new_maui_high.append(add_new_student)
        
        menu("Add Student", "The student was added!", "", "", True)
        input()
    elif menu_choice == "2":
        # This runs if the user wants to look up a student.
        # Prompt them for a name
        menu("Student Lookup", "What is the student's name?")
        name = input()

        # Open the CSV file with the new data
        csv_file = csv.reader(open('MauiHighUpdated.csv', "r"), delimiter=",")
        # Go through each row
        for row in csv_file:
            # If the current row's first value (the name) equals the name that the user put in, give them the info.
            if name == row[0]:
                menu(name, "Grade: " + str(row[1]) + " Credits: " + str(row[3]), "Meets Req.: " + str(row[2]), "Transferring: " + str(row[4]), True)
                input("")
                break
        # At the very end of the loop, the current row will be either the last person in the CSV or the person that was selected.
        # Double check that the selected name isn't equal to the currently selected row.
        # If not, let the user know.
        if name != row[0]:
            menu("Error!", "Could not find:", name, "Please try again.", True)
            input()
    else:
        # This will run after all the checks.
        # If this runs, the user typed an invalid input.
        menu("Error!", "Looks like an invalid", "input there bud.", "", True)
        print(menu_choice)
        input()
        
    # Keep all of the following code at the BOTTOM of the file (after all of the code you add).
    # Sorting and writing your updated new_maui_high data to a file is taken care of for you here.
    new_maui_high.sort()
    with open("MauiHighUpdated.csv", "w") as maui_high_updated_file:
        for student in new_maui_high:
            maui_high_updated_file.write(repr(student) + "\n")

    # Writing your stats to a file is taken care of for you here.
    with open("Stats.json", "w") as stats_file:
        json.dump(stats, stats_file, indent=4)

### Write the data one last time, just to be safe
# Keep all of the following code at the BOTTOM of the file (after all of the code you add).
# Sorting and writing your updated new_maui_high data to a file is taken care of for you here.
new_maui_high.sort()
with open("MauiHighUpdated.csv", "w") as maui_high_updated_file:
    for student in new_maui_high:
        maui_high_updated_file.write(repr(student) + "\n")

# Writing your stats to a file is taken care of for you here.
with open("Stats.json", "w") as stats_file:
    json.dump(stats, stats_file, indent=4)

# After running this file, run CS 101 Final Project Checker.py to see if you got everything right!
