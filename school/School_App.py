from school.Student import Student
from csv import reader


class School:
    def __init__(self,name=None,address=None):
        self.name=name
        self.school_address=address
        self.students={}
        self.teachers={}
        self.other_staff={}
        self.load_students()
    def run(self):
        choice=None
        while choice!=4:
            choice=int(input(f"""WELCOME TO {self.name} 
            1.Student
            2.Teacher
            3.Other staff
            4.Exit
            
            CHOOSE AN OPTION TO PROCEED:
            
            """))
            if choice==1:
                self.student_menu()

            elif choice==2:
                self.teacher_menu()

            elif choice==3:
                self.other_staff_menu()



    def student_menu(self):
        choice = None
        while choice != 3:
            choice = int(input(f"""WELCOME TO STUDENTS 
                    1.Sign up
                    2.Log in
                    3.Exit

                    CHOOSE AN OPTION TO PROCEED:

                    """))
            if choice == 1:
                student=Student()
                student.register()
                self.students[student.roll_number]=student

            elif choice == 2:
                roll_number=int(input("enter your roll number:"))
                try:
                    self.students[roll_number].login()
                    if self.students[roll_number].logged_in:
                        self.students[roll_number].dashboard()

                except:
                    print('roll_number not found')

            elif choice == 3:
                self.other_staff_menu()
    def teacher_menu(self):
        pass
    def other_staff_menu(self):
        pass

    def load_students(self):
        with open('student.csv','r') as file:
            data=reader(file)
            students=(list(data)[1:])
            for x in students:
                first_name,last_name,email,password,phone,roll_number,parent_number,house_address,house_color,grade=x
                print(x)
                student=Student(first_name,last_name,email,password,phone,int(roll_number),parent_number,house_address,house_color,grade)
                self.students[student.roll_number] = student



app=School(name='St Marks High school', address='123-roy st, calcutta 20')
app.run()

