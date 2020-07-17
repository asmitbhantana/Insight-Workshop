class Course:

    def __init__(self, name, duration, detail, price, __enrolled_student=None, __student_info_for_course=None,
                 __study_material=None):
        self.name = name
        self.duration = duration
        self.detail = detail
        self.price = price
        if __enrolled_student is None:
            self.__enrolled_student = []
        else:
            self.__enrolled_student = __enrolled_student
        if __student_info_for_course is None:
            self.__student_info_for_course = {}
        else:
            self.__student_info_for_course = __student_info_for_course
        if __study_material is None:
            self.__study_material = []
        else:
            self.__study_material = __study_material

    def add_student(self, student):
        if self.__enrolled_student.__contains__(student):
            print("Student already enrolled for the course!")
            return
        self.__enrolled_student.append(student)

    def remove_student(self, student):
        self.__enrolled_student.remove(student)

    def get_enrolled_student(self):
        return self.__enrolled_student

    def is_student_enrolled(self, student):
        for s in self.__enrolled_student:
            if s['name'] == student.get_name():
                return True
        return False

    def add_material_to_course(self, material):
        self.__study_material.append(material)

    def add_student_fee(self, student, balance):
        try:
            self.__student_info_for_course[student.get_name()]
            self.__student_info_for_course[student.get_name()]["fee"]
            self.__student_info_for_course[student.get_name()]["fee"] += balance
            print(f"Added new balance {balance} as fee...")
            print(f"New balance {self.__student_info_for_course[student.get_name()]['fee']} as fee...")
            return True

        except Exception as e:
            self.__student_info_for_course[student.get_name()] = {}
            self.__student_info_for_course[student.get_name()]["fee"] = balance
            print(f"Added {self.__student_info_for_course[student.get_name()]['fee']} fee...")
            return False

    def has_student_paid(self, student):
        try:
            self.__student_info_for_course[student.get_name()]
            paid_balance = self.__student_info_for_course[student.get_name()]["fee"]
            if paid_balance >= 2000:
                print(f"Student have paid {paid_balance}, the whole amount")
            elif paid_balance <= 1000:
                print(f"Only {paid_balance} is paid. Should pay more")
            return paid_balance
        except KeyError as e:
            # new student haven't paid the fee
            self.__student_info_for_course[student.get_name()] = {}
            return \
                0

    def has_paid_fully(self, student):
        try:
            paid_balance = self.__student_info_for_course[student.get_name()]["fee"]
            if paid_balance >= 2000:
                return True
            else:
                print(f"Have just paid {paid_balance}")
                return False
        except Exception:
            print("Haven't even paid the first installment!")
            return False

    def get_study_material_for_day(self, student):
        print("for debug __student_info_for_course", self.__student_info_for_course)
        try:
            if self.is_student_enrolled(student) and self.has_paid_fully(student):
                try:
                    progress = self.__student_info_for_course[student.get_name()]["progress"]
                    if progress == self.duration:
                        # return money for complete return_money()
                        material = self.__study_material[progress - 1]
                        self.remove_student_from_course(student)
                        return {'material': material, 'completed': True}
                    material = self.__study_material[progress - 1]
                    self.__student_info_for_course[student.get_name()]["progress"] += 1
                    return {'material': material, 'completed': False}
                except KeyError:
                    self.__student_info_for_course[student.get_name()]["progress"] = 1
                    material = self.__study_material[0]
                    return {'material': material, 'completed': False}
                except Exception as e:
                    print(e)
                    return False

            else:
                print("Student is not illegible for course")
                if not self.has_paid_fully(student):
                    print("Student have not paid full for the course")
                if not self.is_student_enrolled(student):
                    print("Student is not enrolled in the course.")
                return False

        except Exception as e:
            print(e)

    def remove_student_from_course(self, student):
        self.__enrolled_student.remove(student)
        del self.__student_info_for_course[student.get_name()]

    def __str__(self):
        return self.name
