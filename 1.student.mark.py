courses = []
# Function to input number course
def input_number_of_courses():
    return int(input("Enter the number of courses: "))

#function to find the course
def select_course_by_id():
    if len(courses) == 0:
        print("There aren't course yet!! PLS create it. ")
        return create_courses(courses)
    
    course_id_to_select = int(input("Enter the course ID you want to select: "))
    for i, course in enumerate(courses):
        if course["id"] == course_id_to_select:
            return i 
    return 0 
    
#function create coure in4
def input_course_information():
    course_id = input("Enter course ID: ")
    course_name = input("Enter course name: ")
    course_sll = input_number_of_students(course_name)
    course_students = []
    return {"id": course_id, "name": course_name, "sll":course_sll, "std":course_students }

#function create  many course in4 to store
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
 # function print the list of the course
def list_courses(courses):
    print("\nList of Courses:")
    for course in courses:
        print(f"{course['id']}: {course['name']} SLL: {course['sll']} ")

# funtion to input number of students in the select course
def input_number_of_students(course_id):
    number_students = int(input(f"Enter the number of students for course {course_id} (max 40): "))
    while number_students > 40:
        print("Can't add more than 40 students in 1 class!!\nPlease try again.")
        number_students = int(input(f"Enter the number of students for course {course_id} (max 40): "))
    return number_students

# funtion input information of student
def input_student_information():
    student_id = input("Enter student ID: ")
    student_name = input("Enter student name: ")
    student_dob = input("Enter student date of birth: ")
    student_mark = int(input("Enter student mark of course: "))
    return {"id": student_id, "name": student_name, "dob": student_dob, "mark": student_mark}

# funtion input students into course
def input_the_students_in_to_course():
    
    course_index = select_course_by_id()

    if course_index is not 0:
        selected_course = courses[course_index]
        numbers_students = int(input("Input the number students want to add to course: "))
        if numbers_students > int(selected_course["sll"]):
            print(f'Maximum number of students is: {selected_course["sll"]}. Please try again.')
            return numbers_students
        
        for _ in range(numbers_students):
            student_info = input_student_information()
            selected_course["std"].append(student_info)

    else:
        print("Course not found with the given ID. Enter ID course agian!!")


def input_student_marks(students, selected_course):
 
def list_students():
    selected_course_index = select_course_by_id()

    if selected_course_index is not 0:
        selected_course = courses[selected_course_index]
        print(f"\nList of Students in the {selected_course['name']}:")
        for student in selected_course["std"]:
            print(f"{student['id']}: {student['name']}")
    else:
        print("Course not found with the given ID.")



def show_student_marks():


def main():
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
            
        elif choice == "6":
            
        elif choice == "7":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()
