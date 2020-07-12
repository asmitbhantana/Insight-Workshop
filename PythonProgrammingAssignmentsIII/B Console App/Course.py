class Course:

    def __init__(self, name, duration, detail, price):
        self.name = name
        self.duration = duration
        self.detail = detail
        self.price = price
        self.__enrolled_student = []
        self.__study_material = []

    def add_student(self, student):
        if self.__enrolled_student.__contains__(student):
            print("Student already enrolled for the course!")
            return
        self.__enrolled_student.append(student)

    def remove_student(self, student):
        self.__enrolled_student.remove(student)

    def get_enrolled_student(self):
        return self.__enrolled_student

    def get_study_material_for_day(self, day):
        return self.__study_material[day]

    def __str__(self):
        return self.name

