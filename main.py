from studentSchedule import StudentSchedule
from lectureCourse import LectureCourse
from labs import LabCourse

course1 = LabCourse("CS101", "Python Lab", 3, 500)

course2 = LectureCourse("CS102", "AI Lecture", 2, 5)

course3 = LabCourse("CS103", "Electronics Lab", 4, 700)

course4 = LectureCourse("CS104", "Data Science", 3, 10)

all_courses = [course1, course2, course3, course4]
student_schedule = StudentSchedule()
while True:

    print("\n===== UNIVERSITY REGISTRATION SYSTEM =====")

    print("1. View Available Courses")

    print("2. Register For Course")

    print("3. View Student Schedule")

    print("4. Print Tuition Bill")

    print("5. Exit")

    try:

        choice = int(input("Enter your choice: "))

    except:

        print("Please enter a valid number!")

        continue

    # OPTION 1
    if choice == 1:

        print("\n===== AVAILABLE COURSES =====")

        for course in all_courses:
            course.display_course_info()

    # OPTION 2
    elif choice == 2:

        course_id = input("Enter course ID: ")

        found = False

        for course in all_courses:

            if course.get_course_id().lower() == course_id.lower():

                student_schedule.add_course(course)

                found = True

                break

        if found == False:
            print("Course not found!")

    # OPTION 3
    elif choice == 3:

        student_schedule.view_schedule()

    # OPTION 4
    elif choice == 4:

        student_schedule.print_tuition_bill()

    # OPTION 5
    elif choice == 5:

        print("Exiting system...")

        break

    else:

        print("Invalid choice!")