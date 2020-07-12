class Student:

    def __init__(self, name=None, age=None, college_name=None, faculty=None, bank_account=None):
        self.name = name
        self.age = age
        self.college_name = college_name
        self.faculty = faculty
        self.account = bank_account
        self.set_student_props()

    def set_student_props(self):
        self.set_name()
        self.set_age()
        self.set_college_name()
        self.set_faculty()

    def get_account(self):
        return self.account

    def set_account(self, account):
        self.account = account

    def get_name(self):
        return self.name

    def set_name(self):
        usr_name = input("What is student name?")
        self.name = usr_name

    def get_age(self):
        return self.age

    def set_age(self):
        age = input("What is student age?")
        self.age = age

    def set_college_name(self):
        college = input("What is student college name?")
        self.college_name = college

    def get_faculty(self):
        return self.faculty

    def set_faculty(self):
        faculty = input("What is the student faculty?")
        self.faculty = faculty

    def get_detail(self):
        return f"{self.name} is {self.age} years old currently studying {self.faculty} in {self.college_name}."

    def __str__(self):
        return self.name