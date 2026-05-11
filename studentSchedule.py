class StudentSchedule:

    def __init__(self):

        self.courses = []

    def add_course(self, course):

        self.courses.append(course)

        print(f"{course.get_name()} added successfully!")

    def view_schedule(self):

        if len(self.courses) == 0:
            print("No courses registered yet!")

        else:

            print("\n===== STUDENT SCHEDULE =====")

            for course in self.courses:
                course.display_course_info()

    def print_tuition_bill(self):

        total = 0

        print("\n===== TUITION BILL =====")

        for course in self.courses:

            course.display_course_info()

            course_cost = course.calculate_tuition()

            print(f"Course Cost: {course_cost}")

            total += course_cost

        print(f"\nTOTAL SEMESTER FEES = {total}")