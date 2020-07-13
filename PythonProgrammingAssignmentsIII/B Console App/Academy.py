# academy acts as a manager here!
from Student import *
from Course import *
from Finance import *
from FileHandling import *

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
        account = self.finance_manager.create_account(new_student.get_name(), True)
        new_student.set_account(account)
        self.student_list.append(new_student)

    def register_new_course(self):
        name = input("Course Name?")
        duration = int(input("Course Duration in days?"))
        detail = input("Course details?")
        price = int(input("Course price in integer?"))
        new_course = Course(name, duration, detail, price)
        for i in range(duration):
            material = input(f"What do you want to put material for day {i}\n")
            new_course.add_material_to_course(material)
        self.course_list.append(new_course)

    def register_student_in_course(self):
        try:
            course = self.choose_course()
            student = self.choose_student()
            self.pay(2000, student)
            course.add_student(student)
            course.add_student_fee(student, 2000)
        except Exception as e:
            print(e)
            return False
        return True

    def choose_student(self):
        self.list_student()
        choose0 = int(input("Type in the index of the student that you want to enroll.\n"))
        student = self.student_list[choose0]
        return student

    def choose_course(self):
        self.list_course()
        choose = int(input("Type in the index of the needed course."))
        course = self.course_list[choose]
        return course

    def list_student(self):
        print("########\n"
              "Available list of Students\n"
              "------------")
        for index, student in enumerate(self.student_list, 0):
            print(f"{index}.{student}")
        print("###########\n")

    def list_course(self):
        print("########\n"
              "Available list of Courses\n"
              "---------------")
        for index, course in enumerate(self.course_list, 0):
            print(f"{index}.{course}")
        print("###########\n")

    def admin_options(self):
        while True:
            admin_chosse = int(input("What do you want to do?\n"
                                     "1.Register new student\n"
                                     "2.Register new course\n"
                                     "3.List Student\n"
                                     "4.List Course\n"
                                     "5.Enroll Student in Course\n"
                                     "0.Exit\n"))

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

    def student_options(self):
        student_name = input("Type in your name for getting in!")
        for student in self.student_list:
            if student.get_name() == student_name:
                current_student = student
                break
        else:
            print("Your name doesn't exist!")
            return

        while True:
            student_choose = int(input(
                "What you want to do?\n"
                "1.Edit college name\n"
                "2.Edit Faculty\n"
                "3.Edit age\n"
                "4.Enroll in Course\n"
                "5.Pay For enrolled Course\n"
                "6.Take classes for enrolled courses\n"
                "0.Exit\n"
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
                try:  # check if he has paid or not
                    course = self.choose_course()
                    if course.is_student_enrolled(current_student):
                        amount = self.get_student_payment_options()
                        self.pay_for_course(course, current_student, amount)
                        self.student_register_in_course(course, current_student)
                    else:
                        print("You are not enrolled in the course. Enroll first!")
                except Exception as e:
                    print(e)
            elif student_choose == 6:
                course = self.choose_course()
                if course.is_student_enrolled(current_student):
                    print("Student is enrolled...\n")
                    paid_amount = course.has_student_paid(current_student)
                    if paid_amount >= 2000:
                        print("You have paid sufficient for course!")
                        material_returnee = course.get_study_material_for_day(current_student)
                        material = material_returnee['material']
                        print("This is the material\n", material)
                        if material_returnee["completed"]:
                            print("Congratulations Course is completed!!!")
                            print("Returning the money!")
                            self.finance_manager.transfer_money(2000, Academy.ACADEMY_NAME, current_student.get_name())
                        # get study material for student according to the
                        # day he have got to the content!
                    else:
                        print(f"Sorry you have not paid full. {paid_amount} is only paid.")
                # TODO
                # save details in .json file
                # check for payment on accessing for course material

    def get_student_payment_options(self):
        amount = int(input("What amount you want to pay "))
        return amount

    def pay_for_course(self, course, current_student, amount):
        paid_amount = course.has_student_paid(current_student)
        if paid_amount >= 2000:  # paid all
            print("No need to pay the amount is already paid!")
            return
        elif paid_amount < 2000:
            print(f"Only {paid_amount} is paid! Next {amount} will be paid for the course!")
            self.pay(amount, current_student)
            course.add_student_fee(current_student, amount)
            if paid_amount + amount >= 2000:
                print(f"amount is sufficient to take course now!")
            else:
                print(f"amount is not sufficient to take the course now!")

    def pay(self, amount, current_student):
        self.finance_manager.transfer_money(amount, current_student.get_name(), Academy.ACADEMY_NAME)


if __name__ == '__main__':
    academy = Academy()
    while True:
        usr_selection = int(input("What do you want to login as?\n"
                                  "1.Student\n"
                                  "2.Admin\n"
                                  "3.Exit\n"))
        if usr_selection == 2:
            academy.admin_options()
        elif usr_selection == 1:
            academy.student_options()
        elif usr_selection == 3:
            FileHandling.save_student_info(academy.courseinfo)
            FileHandeling.save_course_info(academy.course_list)
