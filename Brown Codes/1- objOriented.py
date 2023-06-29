class course:
    def __init__(self, students, teacher_name, name_course):
        self.students = students
        self.teacher_name = teacher_name
        self.name_course = name_course
    
    def listStudents(self):
        for i in self.students:
            print(i)
    
    def change_teacher(self, new_teacher_name):
        self.teacher_name = new_teacher_name
        print("Teacher name successfully changed to: " + self.teacher_name)

    def change_courseName(self, new_course_name):
        self.name_course = new_course_name
        print("Course name successfully changed to: " + self.name_course)