
def input_number_of_courses():
    return int(input("Enter the number of courses: "))

def seclect_course(courses):
    course_id = input("Enter course ID: ")
    return {"id": course_id}

def list_courses(courses):
    print("\nList of Courses:")
    for course in courses:
        print(f"{course['id']}: {course['name']}")

def input_course_information():
    course_id = input("Enter course ID: ")
    course_name = input("Enter course name: ")
    course_sll = input_number_of_students(course_name)
    course_students = []
    return {"id": course_id, "name": course_name, "sll":course_sll, "std":course_students }

def create_courses(courses):
    num_courses = input_number_of_courses()
    for _ in range(num_courses):
        while (True):
            check = True
            course_info = input_course_information()
            for i in courses:
                if course_info['id'] == i["id"]:
                    print("The course ID already exists! Please try again. \n Create again!")
                    check = False
                    break
            if check == True:
                courses.append(course_info)
                break
            else:
                course_info = input_course_information()

def input_number_of_students(course_name):
    number_students = int(input(f"Enter the number of students for course {course_name} (max 40): "))
    while number_students > 40:
        print("Can't add more than 40 students in 1 class!!\nPlease try again.")
        number_students = int(input(f"Enter the number of students for course {course_name} (max 40): "))
    return number_students

def input_student_information():
    student_id = input("Enter student ID: ")
    student_name = input("Enter student name: ")
    student_dob = input("Enter student date of birth: ")
    return {"id": student_id, "name": student_name, "dob": student_dob}

def input_the_students_in_to_course(courses,courses_id,course_students,course_sll):
    if len(courses) == 0:
        print("There aren't course yet!! PLS create it. ")
        return create_courses(courses)
    course = seclect_course(courses)
    check = False
    while not check:
        for i in courses:
            if course['id'] == i["id"]:
                check = True
                break
        if not check:
            print("The course ID doesn't exist! Please try again. \n Input again!")
            course = seclect_course(courses)

    numbers_students = input_number_of_students(course['id'])


def input_student_marks(students, selected_course):
 

def list_students(students):



def show_student_marks(students, marks, selected_course):


def main():
    students = []
    courses = []
    marks = {}
    while True:
        print("\nMenu:")
        print("1. Create a Courses")
        print("2. Enter students in the course")
        print("3. List Courses")
        print("4. List Students")
        print("5. Enter Student Marks")
        print("6. Show Student Marks for a Course")
        print("7. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            create_courses(courses)
        elif choice == "2":
            input_the_students_in_to_course(courses)
        elif choice == "3":
            list_courses(courses)
        elif choice == "4":
            list_students(students)
        elif choice == "5":
            selected_course = input_course_information()
            marks[selected_course['id']] = input_student_marks(students, selected_course)
        elif choice == "6":
            selected_course = input_course_information()
            show_student_marks(students, marks.get(selected_course['id'], {}), selected_course)
        elif choice == "7":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()
