from csv import writer

from User import User


class Teacher(User):
    def __init__(self,subject=None,experience=None,pay=None):
        super().__init__()
        self.subject=subject
        self.experience=experience
        self.pay=pay
    def register(self):
        super().register()
        self.subject = input('Enter your subject you teach ')
        self.experience = input('Enter your experience in years')
        self.pay = input('Enter your base pay')
        self.save_info()
        print('you are registered successfully')

    def __str__(self):
        return f"{super().__str__()}  {self.experience} {self.subject} {self.pay}"

    def save_info(self):
        with open('teacher.csv','a',newline='') as file:
            csv_writer=writer(file)
          #  csv_writer.writerow(['first_name','last_name','email','password','phone','roll_number','parent_number','house_address','house_color','grade'])
            csv_writer.writerow([self.first_name,self.last_name,self.email,self.password,self.phone,self.subject,self.experience,self.pay])