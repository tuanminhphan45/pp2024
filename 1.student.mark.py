# Function to input number of courses
def input_number_of_courses():
    return int(input("Enter the number of courses: "))

# Function to find the course by ID
def select_course_by_id(courses):
    if len(courses) == 0:
        print("There aren't any courses yet! Please create them.")
        return None
    
    course_id_to_select = int(input("Enter the course ID you want to select: "))
    for course in courses:
        if course["id"] == course_id_to_select:
            return course
    return None
    
# Function to input course information
def input_course_information():
    course_id = int(input("Enter course ID: "))
    course_name = input("Enter course name: ")
    course_max_students = input_number_of_students(course_name)
    course_students = []
    return {"id": course_id, "name": course_name, "sll": course_max_students, "std": course_students}

# Function to create multiple courses and store their information
def create_courses(courses):
    num_courses = input_number_of_courses()
    for _ in range(num_courses):
        while True:
            check = True
            course_info = input_course_information()
            for i in courses:
                if course_info['id'] == i["id"]:
                    print("The course ID already exists! Please try again.\nCreate again!")
                    check = False
                    break
            if check:
                courses.append(course_info)
                break

# Function to input the number of students for a given course
def input_number_of_students(course_id):
    number_students = int(input(f"Enter the number of students for course {course_id} (max 40): "))
    while number_students > 40:
        print("Can't add more than 40 students in 1 class!!\nPlease try again.")
        number_students = int(input(f"Enter the number of students for course {course_id} (max 40): "))
    return number_students

# Function to input student information
def input_student_information():
    student_id = input("Enter student ID: ")
    student_name = input("Enter student name: ")
    student_dob = input("Enter student date of birth: ")
    student_mark = int(input("Enter student mark of course: "))
    return {"id": student_id, "name": student_name, "dob": student_dob, "mark": student_mark}

# Function to input students into a course
def input_the_students_in_to_course(courses):
    selected_course = select_course_by_id(courses)
    if selected_course is not None:
        while True:
            numbers_students = int(input("Input the number students want to add to the course: "))
            if numbers_students > int(selected_course["sll"]):
                print(f'Maximum number of students is: {selected_course["sll"]}. Please try again.')
            else:
                for _ in range(numbers_students):
                    student_info = input_student_information()
                    selected_course["std"].append(student_info)
                break
    else:
        print("Course not found with the given ID. Enter the ID of the course again!!")

# Function to list the courses
def list_courses(courses):
    if len(courses) == 0:
        print("There are no courses! Please create some.")
    else:
        print("\nList of Courses:")
        for course in courses:
            print(f"{course['id']}: {course['name']} SLL: {course['sll']} ")

# Function to list students in a course
def list_students(courses):
    selected_course = select_course_by_id(courses)
    if selected_course is not None:
        if len(selected_course["std"]) == 0:
             print(f"There are no students in {selected_course['name']}")
        else:
            print(f"Students in {selected_course['name']} course:")
            for student in selected_course['std']:
                print(f"ID: {student['id']} - Name: {student['name']}")
    else:
        print("Course not found with the given ID.")

# Function to list all mark of students in the course
def list_student_marks(courses):
    selected_course = select_course_by_id(courses)
    if selected_course is not None:
        if len(selected_course["std"]) == 0:
            print(f"There are no students in {selected_course['name']}")
        else:
            print(f"Student Marks in {selected_course['name']} course:")
            for student in selected_course['std']:
                if len(student['mark']) == 0:
                   print(f"ID: {student['id']} - Name: {student['name']} - Mark: N/A") 
                else: print(f"ID: {student['id']} - Name: {student['name']} - Mark: {student['mark']}")
    else:
        print("Course not found with the given ID.")


# Main function
def main():
    courses = []

    while True:
        print("\nMenu:")
        print("1. Create Courses")
        print("2. Enter students in the course and their mark")
        print("3. List Courses")
        print("4. List Students")
        print("5. Show Student Marks for a Course")
        print("6. Exit")

        choice = input("Enter your choice (1-7): ")

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
