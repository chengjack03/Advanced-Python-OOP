##Python classes using OOP concepts, working with common Python data types like lists, tuples, sets, and dictionaries##

##Class definition##

class Student:
    def __init__(self, name: str, email: str, grades):
        self.name = name          # String
        self.email = email        # String
        self.grades = grades   # List of integers

    def get_average_grade(self) -> float:                   ##returns the average of the student's grades##
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)

    def add_grade(self, grade: int):                      ##Adds a grade to the student's list of grades##
        self.grades.append(grade)               

    def display_info(self):                     ##Displays the student's information##
        print(f"Name: {self.name}")
        print(f"Email: {self.email}")   
        print(f"Grades: {self.grades}")
        print(f"Average Grade: {self.get_average_grade()}")
        
    def grades_tuple(self):               ##Returns the student's grades as a tuple##
        return tuple(self.grades)
    
    
    
##Working with Objects##
##Creating 3 student objects##
student1 = Student("Alice Wonderful", "alice@example.com", [85, 90, 78])
student2 = Student("Bob Builder", "bob@example.com", [92, 88, 95])
student3 = Student("Charlie Chapman", "charlie@example.com", [76, 82, 89])

##Adding 2 new grades to each students using add_grade method##
student1.add_grade(88)
student1.add_grade(91)

student2.add_grade(87)
student2.add_grade(90)

student3.add_grade(84)
student3.add_grade(79)

##Displaying student information and average grade for each using display_info method##
student1.display_info()
print()  # For better readability
student2.display_info()
print()  # For better readability
student3.display_info()
print()  # For better readability



##Dictionary & Set Integration##
##Dictionary called "student_dict" mapping student emails to student objects##
student_dict = {
    student1.email: student1,
    student2.email: student2,
    student3.email: student3
}

##Writing a function get_student_by_email(email) that retrieves a student object from the dictionary safely using .get()
def get_student_by_email(email: str):
    return student_dict.get(email, None)

##create a set of all unique grades across all students and print it##
all_grades = []
for student in student_dict.values():
    all_grades.extend(student.grades)

unique_grades = set(all_grades)
print(f"Unique Grades across all students: {unique_grades}")


##Tuples Practice##
##Add a method to the Student class called grades_tuples(self) that returns the grades as a tuple##
print(f"Grades of {student1.name} as tuple: {student1.grades_tuple()}")

##Demonstrate that tuples are immutable by trying to change a value (catch the exception with try/except and print a message).##
try:
    grades_tuple = student1.grades_tuple()
    grades_tuple[0] = 100                   ##Attempting to change the first grade raises TypeError because immutable##
except TypeError as e:
    print("Cannot modify tuple: Tuples are immutable.")
    print(f"Error: {e}")
    
    
##List Operations##
##Remove the last grade from each student's grades using .pop()##

students = [student1, student2, student3]
for student in students:
    if student.grades:  ##removes last grade##
        removed_grade = student.grades.pop()
        print(f"Removed last grade {removed_grade} from {student.name}'s grades.")
        
##Access and print the first and last grade for each student.##
    if student.grades:
        first_grade = student.grades[0]
        last_grade = student.grades[-1]
        print(f"{student.name}'s first grade: {first_grade}, last grade: {last_grade}")
    else:
        print(f"{student.name} has no grades left.")
    
    ##print the number of grades each student has using len()##
    print(f"{student.name} has {len(student.grades)} grades left.")
    
    
    
    
