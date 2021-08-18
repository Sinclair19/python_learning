class User:
    def __init__(self,fname,lname,age):
        self.first_name = fname
        self.last_name = lname
        self.full_name = f"{self.first_name} {self.last_name}"
        self.age = age
    def describe_user(self):
        message = f"The user's name is {self.full_name.title()}, "
        message += f"The user's age is {self.age}."
        print(f"The user's name is {self.full_name.title()}, The user's age is {self.age}.")
        print(message)
    def greet_user(self):
        print(f"Hello, {self.full_name.title()}!")

user_a = User('john', 'willson', '21')
user_a.describe_user()
user_a.greet_user()


