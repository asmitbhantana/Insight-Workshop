import json


class FileHandling:
    FOLDER_NAME = "consoleAppData/"

    @staticmethod
    def save_student_info(student_data):
        student_info_file = open(FileHandling.FOLDER_NAME + "student-info.json", "w", encoding='utf-8')
        json.dump(student_data, student_info_file, default=lambda i: i.__dict__, ensure_ascii=False, indent=4)
        student_info_file.close()

    @staticmethod
    def save_course_info(course_info):
        course_file = open(FileHandling.FOLDER_NAME + "course-info.json", "w", encoding='utf-8')
        json.dump(course_info, course_file, default=lambda i: i.__dict__, ensure_ascii=False, indent=4)
        course_file.close()

    @staticmethod
    def save_finance_info(finance_info):
        finance_file = open(FileHandling.FOLDER_NAME + "finance-info.json", "w", encoding='utf-8')
        json.dump(finance_info, finance_file, ensure_ascii=False, indent=4)
        finance_file.close()

    @staticmethod
    def retrieve_student_info():
        try:
            student_info_file = open(FileHandling.FOLDER_NAME + "student-info.json", "r", encoding='utf-8')
            ma = json.load(student_info_file)
            student_info_file.close()
            return ma
        except Exception:
            return []

    @staticmethod
    def retrieve_course_info():
        try:
            course_info_file = open(FileHandling.FOLDER_NAME + "course-info.json", "r", encoding='utf-8')
            ma = json.load(course_info_file)
            course_info_file.close()
            return ma
        except Exception:
            return []

    @staticmethod
    def retrieve_finance_info():
        try:
            finance_info_file = open(FileHandling.FOLDER_NAME + "finance-info.json", "r", encoding='utf-8')
            ma = json.load(finance_info_file)
            finance_info_file.close()
            return ma
        except Exception:
            return {}
