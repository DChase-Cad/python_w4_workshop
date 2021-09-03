''' Week 4 workshop '''


class User:
    ''' User class'''
    def __init__(self, name, pin, password):
        self.name = name
        self.pin = pin
        self.password = password

    def change_name(self, name):
        '''changes name of a user'''
        if len(name)>=2 and len(name)<=10:
            self.name = name
        else:
            print('Sorry a name must be between 2 and 10 digits in length')

    def change_pin(self, pin):
        '''changes pin of a user'''
        try:
            pin=int(pin)
            if len(str(pin))==4 and pin!=self.pin:
                self.pin = pin
                print("PIN was successfully changed.")
            else:
                print('PIN must be exactly 4 numbers and be different from existing PIN')
        except ValueError:
            print('PIN can only contain only numbers')

    def change_pass(self, password):
        '''changes password of a user'''
        if len(password)>=5:
            self.password = password
        else:
            print('Password must be 5 characters or longer')


class BankUser(User):
    '''Extending User class to create a BankUser subclass'''
    def __init__(self, name, pin, password):
        super().__init__(name, pin, password)
        self.balance = 0

    def show_balance(self):
        '''shows balance of the user'''
        print(
            f'{self.name.capitalize()} has an account balance of : {"${:,.2f}".format(self.balance)}')

    def withdraw(self, amount):
        '''withdraws from balance of a user'''
        if amount < self.balance:
            self.balance -= amount
        else:
            print('Insufficient funds.')

    def deposit(self, amount):
        '''deposits to balance of a user'''
        if amount > 0:
            self.balance += amount

    def validate_balance(self,amount):
        '''validating that there is sufficient funds'''
        return True if self.balance>=amount else False

    def transfer_money(self, receivingUser):
        '''transfer authorization'''
        amount=input("Enter amount to be transferred: ")
        if validate_number(amount):
            amount=float(amount)
            print(f'You are transferring {"${:,.2f}".format(amount)} to {receivingUser.name.capitalize()}')
            print('Authorization required.')
            pinInput = int(input('Please enter your pin: '))
            if pinInput == self.pin:
                if self.validate_balance(amount):
                    print('Transfer authorized')
                    self.balance -= amount
                    receivingUser.balance += amount
                    return True
                else:
                    print("Insufficient funds transaction has been cancelled.")
            else:
                print('Invalid PIN transaction has been cancelled.')
                return False
        else:
            print('Transfer amount is negative or not a number, transaction has been cancelled.')

    def request_money(self, requestedUser):
        '''method for requesting a transfer of funds'''
        amount=input(f"Enter amount you are requesting from {requestedUser.name}: ")

        if validate_number(amount):
            amount=float(amount)
            print(f'You are requesting {"${:,.2f}".format(amount)} from {requestedUser.name.capitalize()}')
            pinInput = int(input(f"Please enter {requestedUser.name.capitalize()}'s PIN: "))
            if pinInput == requestedUser.pin:
                passInput = input('Please enter your password: ')
                if passInput == self.password:
                    if requestedUser.validate_balance(amount):
                        print('Request authorized')
                        requestedUser.balance-=amount
                        self.balance+=amount
                        print(f'{requestedUser.name.capitalize()} sent {"${:,.2f}".format(amount)}')
                    else:
                        print('Insufficient funds transaction has been cancelled.')
                else:
                    print('Incorrect Password transaction has been cancelled')
            else:
                print('Invalid PIN transaction has been cancelled.')
        else:
            print('Requested amount was either negative or not a number, transaction has been cancelled')


def validate_number(number):
    '''try/except to validate an input to a float that is a positive number'''
    try:
        number=float(number)
        if number>0:
            return True
        else:
            return False
    except ValueError:
        return False




# """Driver code for Task 1"""
# newUser=User('Bob',1234,'password')
# print(newUser.name,newUser.pin,newUser.password)
# """Driver code for Task 2"""
# newUser.change_name('Bobby')
# newUser.change_pin(4321)
# newUser.change_pass('newpassword')
# print(newUser.name,newUser.pin,newUser.password)
# """Driver code for Task 3"""
# print(user2.name, user2.pin, user2.password, user2.balance)


# """Driver code for task 4"""
# user2.show_balance()
# user2.deposit(1000)
# user2.show_balance()
# user2.withdraw(500)
# user2.show_balance()
# print(user2.transfer_money())

# user2.request_money(user1)

# '''Driver code for task 5'''

user1 = BankUser('bob', 1234, 'password')
user2 = BankUser('Alice', 4321, '123')

user2.deposit(5000)
user2.show_balance()
user2.show_balance()
user2.change_pin('12345')
user2.change_pin('4321')
user2.change_pin('1111')
user1.show_balance()
user2.transfer_money(user1)
user2.show_balance()
user1.show_balance()
user2.request_money(user1)
user2.show_balance()
user1.show_balance()
