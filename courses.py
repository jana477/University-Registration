class Course:

    def __init__(self, course_id, name, credit_hours):
        self.__course_id = course_id
        self.__name = name
        self.__credit_hours = credit_hours

    # Getters
    def get_course_id(self):
        return self.__course_id

    def get_name(self):
        return self.__name

    def get_credit_hours(self):
        return self.__credit_hours

    # Setter
    def set_credit_hours(self, hours):

        if hours > 0:
            self.__credit_hours = hours

        else:
            print("Invalid credit hours!")

    # Methods
    def calculate_tuition(self):
        pass

    def display_course_info(self):
        pass