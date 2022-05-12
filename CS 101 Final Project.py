import json

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
        if len(student_data) == 5:
            self.name = student_data[0]
            self.grade = int(student_data[1])
            if student_data[2] == "met":
                self.graduation_requirements = True
            else:
                self.graduation_requirements = False
            self.credits = int(student_data[3])
            if student_data[4] == "transferring":
                self.transferring = True
            else:
                self.transferring = False
        elif len(student_data) == 3:
            self.name = student_data[0]
            self.grade = int(student_data[1])
            self.high_school = str(student_data[2])
        else:
            print("[ERROR]>> Looks like your CSV file has the wrong number of values per student. (3 or 5)")
    
    # defines the "less than" method for students (for sorting purposes)
    def __lt__(self, other):
        # This method has already been completed for you. Do NOT mess with it (for grading reasons).
        return self.name < other.name

    # provides a string representation of a student
    def __repr__(self):
        # This method has already been completed for you. Do NOT mess with it (for grading reasons).
        return self.name + "," + str(self.grade) + "," + str(self.graduation_requirements) + "," + str(self.credits) + "," + str(self.transferring)

    def assignBlanks(self, student_data):
        self.name = student_data[0]
        self.grade = 9
        self.graduation_requirements = "not met"
        self.credits = 0
        self.transferring = "not transferring"
        
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

#TODO: Write the rest of your code

for x in range(len(maui_high)):
    new_student = Student(maui_high[x])

    if new_student.grade == 9 and new_student.credits >= 13 and new_student.transferring == False:
        new_student.grade = 10

    elif new_student.graduation_requirements != "met" and new_student.grade == 12:
        continue

    else:
        continue


    new_maui_high.append(new_student)


for x in range(len(lokelani_intermediate)):
    new_student = Student(lokelani_intermediate[x])

    if new_student.grade == 8 and new_student.high_school == "Maui High":
        new_student.assignBlanks(lokelani_intermediate[x])
        new_maui_high.append(new_student)
        #[new_student.name, 9, 'not met', 0, 'not transferring']
    else:
        continue





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
