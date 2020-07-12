# academy acts as a manager here!
from Student import *
from Course import *
from Finance import *


class Academy:
    ACADEMY_NAME = "I.W. ACADEMY"

    def __init__(self):
        self.student_list = []
        self.course_list = []
        self.account = None
        self.finance_manager = Finance()
        self.create_academy_account()

    def create_academy_account(self):
        self.account = self.finance_manager.create_account(Academy.ACADEMY_NAME)


    def register_student(self):
        new_student = Student()
        new_student.set_student_props()
        account = self.finance_manager.create_account(new_student.get_name(), True)
        new_student.set_account(account)
        self.student_list.append(new_student)

    def register_new_course(self):
        name = input("Course Name?")
        duration = int(input("Course Duration in days?"))
        detail = input("Course details?")
        price = int(input("Course price in integer?"))
        new_course = Course(name, duration, detail, price)
        self.course_list.append(new_course)

    def register_student_in_course(self):
        try:
            course = self.choose_course()
            student = self.choose_student()
            self.finance_manager.transfer_money(2000, student.get_name(), Academy.ACADEMY_NAME)
            course.add_student(student)
        except Exception as e:
            print(e)
            return False
        return True

    def choose_student(self):
        for index, student in enumerate(self.student_list, 0):
            print(f"{index}.{student}")
        choose0 = int(input("Type in the index of the student that you want to enroll."))
        student = self.student_list[choose0]
        return student

    def choose_course(self):
        for index, course in enumerate(self.course_list, 0):
            print(f"{index}.{course}")
        choose = int(input("Type in the index of the needed course.")
        course = self.course_list[choose]
        return course

    def list_student(self):
        print(self.student_list)

    def list_course(self):
        print(self.course_list)

    def admin_options(self):
        admin_chosse = int(input("What do you want to do?\n"
                              "1.Register new student\n"
                              "2.Register new course\n"
                              "3.List Student\n"
                              "4.List Course\n"
                              "5.Enroll Student in Course\n"
                              "0.Exit"))

        if admin_chosse == 1:
            self.register_student()
        elif admin_chosse == 2:
            self.register_new_course()
        elif admin_chosse == 3:
            self.list_student()
        elif admin_chosse == 4:
            self.list_course()
        elif admin_chosse == 5:
            self.register_student_in_course()
        elif admin_chosse == 0:
            return True

    def student_register_in_course(self, course, student):
        course.add_student(student)

    def is_student_paid(self,):

    def student_options(self):
        student_name = input("Type in your name for getting in!")
        for student in self.student_list:
            if student.get_name() == student_name:
                current_student = student
                break
        else:
            print("Your name doesn't exist!")
            return

        student_choose = int(input(
            "What you want to do?\n"
            "1.Edit college name\n"
            "2.Edit Faculty\n"
            "3.Edit age\n"
            "4.Enroll in Course\n"
            "5.Take Course Material For enrolled Course\n"
            "6.Take classes for enrolled courses\n"
            "0.Exit"
        ))

        if student_choose == 0:
            return True
        elif student_choose == 1:
            current_student.set_college_name()
        elif student_choose == 2:
            current_student.set_faculty()
        elif student_choose == 3:
            current_student.set_age()
        elif student_choose == 4:
            course = self.choose_course()
            self.student_register_in_course(course, current_student)
        elif student_choose == 5:
            try:
                course = self.choose_course()
                self.finance_manager.transfer_money(2000,current_student.get_name(),Academy.ACADEMY_NAME)
                self.student_register_in_course(course, current_student)

            except Exception as e:
                print(e)
        elif student_choose == 6:

            #TODO
            #check finance
            #save details in .json file
            #check payment 2 times installment
            #check for payment on accessing for course material


