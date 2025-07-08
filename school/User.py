#inheritance

class User:
    def __init__(self,first_name=None,last_name=None,email=None,password=None,phone=None
                 ):
        self.first_name=first_name
        self.last_name=last_name
        self.email=email
        self.password=password
        self.phone=phone
        self.logged_in=False
    def register(self):
        print('Welcome to register:')
        self.first_name = input('enter your first_name:')
        self.last_name = input('enter your last_name:')
        self.email = input('enter your email:')
        self.password = input('enter your password:')
        self.phone = input('enter your phone:')

    def login(self):
        print('Welcome to login:')
        email=input('enter your email:')
        password=input('enter your password:')
        if self.email==email and self.password==password:
            print('log in successful')
            self.logged_in=True
    def logout(self):
        confirm=input('do yo want to log out(Y/N):')
        if self.logged_in:
            if confirm=='Y':
                self.logged_in=False
                print('Logout is successful')
        else:
            print('You are not logged in:')
    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.email} {self.password} {self.phone}"
# user1=User()
# user1.register()
# user1.login()
# user1.logout()

