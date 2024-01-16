import datetime
class Course:
    def __init__(self, course_id, course_name, max_students):
        self.id = course_id
        self.name = course_name
        self.max_students = max_students
        self.students = []

class Student:
    def __init__(self, student_id, student_name, dob, mark):
        self.id = student_id
        self.name = student_name
        self.dob = dob
        self.mark = mark

def input_number_of_courses():
    return int(input("Enter the number of courses: "))

def select_course_by_id(courses):
    if len(courses) == 0:
        print("There aren't any courses yet! Please create them.")
        return None
    
    course_id_to_select = int(input("Enter the course ID you want to select: "))
    for course in courses:
        if course.id == course_id_to_select:
            return course
    return None

def input_course_information():
    course_id = int(input("Enter course ID: "))
    course_name = input("Enter course name: ")
    course_max_students = int(input(f"Enter the maximum number of students for course {course_name}: "))
    return Course(course_id, course_name, course_max_students)

def create_courses(courses):
    num_courses = input_number_of_courses()
    for _ in range(num_courses):
        while True:
            check = True
            course_info = input_course_information()
            for course in courses:
                if course_info.id == course.id:
                    print("The course ID already exists! Please try again.\nCreate again!")
                    check = False
                    break
                if course_info.name == course.name:
                    print("The course NAME already exists! Please try again.\nCreate again!")
                    check = False
                    break
            if check:
                courses.append(course_info)
                break

def input_number_of_students(course_id):
    number_students = int(input(f"Enter the number of students for course {course_id} (max 40): "))
    while number_students > 40:
        print("Can't add more than 40 students in 1 class!!\nPlease try again.")
        number_students = int(input(f"Enter the number of students for course {course_id} (max 40): "))
    return number_students

def input_student_information(courses):
    while True:
        student_id = input("Enter student ID: ")
        check = False
        for course in courses:
            for student in course.students:
                if student.id == student_id:
                    print(f"Student ID '{student_id}' already exists. Please enter a different ID.")
                    check = True
                    break 
            if check:
                break 

        if not check:
            student_name = input("Enter student name: ")
            while True:
                dob_str = input("Enter student date of birth (format: dd/mm/yyyy): ")
                try:
                    student_dob = datetime.datetime.strptime(dob_str, "%d/%m/%Y").date()
                    break  
                except :
                    print("Incorrect date format! Please use dd/mm/yyyy.")
            student_mark = int(input("Enter student mark of course: "))
            return Student(student_id, student_name, student_dob, student_mark)

def input_the_students_in_to_course(courses):
    selected_course = select_course_by_id(courses)
    if selected_course is not None:
        while True:
            numbers_students = int(input("Input the number students want to add to the course: "))
            if numbers_students > selected_course.max_students:
                print(f'Maximum number of students is: {selected_course.max_students}. Please try again.')
            else:
                for _ in range(numbers_students):
                    student_info = input_student_information(courses)
                    selected_course.students.append(student_info)
                break
    else:
        print("Course not found with the given ID. Enter the ID of the course again!!")

def list_courses(courses):
    if len(courses) == 0:
        print("There are no courses! Please create some.")
    else:
        print("\nList of Courses:")
        for course in courses:
            print(f"{course.id}: {course.name} Max Students: {course.max_students}")

def list_students(courses):
    selected_course = select_course_by_id(courses)
    if selected_course is not None:
        if len(selected_course.students) == 0:
             print(f"There are no students in {selected_course.name}")
        else:
            print(f"Students in {selected_course.name} course:")
            for student in selected_course.students:
                print(f"ID: {student.id} - Name: {student.name}")
    else:
        print("Course not found with the given ID.")

def list_student_marks(courses):
    selected_course = select_course_by_id(courses)
    if selected_course is not None:
        if len(selected_course.students) == 0:
            print(f"There are no students in {selected_course.name}")
        else:
            print(f"Student Marks in {selected_course.name} course:")
            for student in selected_course.students:
                if student.mark == "":
                   print(f"ID: {student.id} - Name: {student.name} - Mark: N/A") 
                else: print(f"ID: {student.id} - Name: {student.name} - Mark: {student.mark}")
    else:
        print("Course not found with the given ID.")

def main():
    courses = [Course(1, "ADS", 2), Course(2, "Python", 3)]

    while True:
        print("\nMenu:")
        print("1. Create Courses")
        print("2. Enter students in the course and their mark")
        print("3. List Courses")
        print("4. List Students")
        print("5. Show Student Marks for a Course")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            create_courses(courses)
        elif choice == "2":
            input_the_students_in_to_course(courses)
        elif choice == "3":
            list_courses(courses)
        elif choice == "4":
            list_students(courses)
        elif choice == "5":
            list_student_marks(courses)
        elif choice == "6":
            print("END the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
