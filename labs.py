from courses import  Course
class LabCourse(Course):

    def __init__(self, course_id, name, credit_hours, lab_fee):

        super().__init__(course_id, name, credit_hours)

        self.__lab_fee = lab_fee

    def get_lab_fee(self):
        return self.__lab_fee

    def set_lab_fee(self, fee):

        if fee >= 0:
            self.__lab_fee = fee

        else:
            print("Invalid lab fee!")

    def calculate_tuition(self):

        tuition = (self.get_credit_hours() * 1000) + self.__lab_fee

        return tuition

    def display_course_info(self):

        print(f"[LAB] {self.get_course_id()} - {self.get_name()} "
              f"| Credit Hours: {self.get_credit_hours()} "
              f"| Lab Fee: {self.__lab_fee}")