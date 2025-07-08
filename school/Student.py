from User import User
from csv import writer


class Student(User):
    def __init__(self,first_name=None,last_name=None,email=None,password=None,phone=None,roll_number=None,parent_number=None,house_address=None,grade=None,house_color=None):
        super().__init__(first_name,last_name,email,password,phone)
        self.roll_number=roll_number
        self.parent_number=parent_number
        self.house_address=house_address
        self.grade=grade
        self.house_color=house_color

    def register(self):
        super().register()
        self.roll_number = int(input('Enter your roll_number'))
        self.parent_number = input('Enter your parent_number')
        self.house_address = input('Enter your house_address')
        self.grade = input('Enter your grade')
        self.house_color = input('Enter your house_color')
        self.save_info()
        print('you are registered successfully')
    def save_info(self):
        with open('student.csv','a',newline='') as file:
            csv_writer=writer(file)
          #  csv_writer.writerow(['first_name','last_name','email','password','phone','roll_number','parent_number','house_address','house_color','grade'])
            csv_writer.writerow([self.first_name,self.last_name,self.email,self.password,self.phone,self.roll_number,self.parent_number,self.house_address,self.house_color,self.grade])



    def __str__(self):
        return f"{super().__str__()}  {self.grade} {self.roll_number} {self.parent_number}"

    def dashboard(self):
        info=f''' Student Info
        {self.first_name}: {self.last_name}:
        {self.roll_number} 
        {self.grade}
        {self.parent_number}
'''
        print(info)

