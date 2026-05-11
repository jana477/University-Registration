from courses import Course
class LectureCourse(Course):

    def __init__(self, course_id, name, credit_hours, tech_fee_percent):

        super().__init__(course_id, name, credit_hours)

        self.__tech_fee_percent = tech_fee_percent

    def get_tech_fee_percent(self):
        return self.__tech_fee_percent

    def set_tech_fee_percent(self, percent):

        if percent >= 0:
            self.__tech_fee_percent = percent

        else:
            print("Invalid percentage!")

    def calculate_tuition(self):

        base = self.get_credit_hours() * 1000

        tuition = base + (base * self.__tech_fee_percent / 100)

        return tuition

    def display_course_info(self):

        print(f"[LECTURE] {self.get_course_id()} - {self.get_name()} "
              f"| Credit Hours: {self.get_credit_hours()} "
              f"| Tech Fee: {self.__tech_fee_percent}%")