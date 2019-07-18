class Account:

    def __init__(self,filepath):
        with open(filepath,'r') as file:
            self.filepath = filepath
            self.balance = int(file.read())

    def withdraw(self,amount):
        self.balance = self.balance - amount

    def deposit(self,amount):
        self.balance = self.balance + amount

    def commit(self):
        with open(self.filepath,'w') as file:
            file.write(str(self.balance))


# account = Account("balance.txt")
# print(account.balance)
# account.deposit(400)
# print(account.balance)
# account.commit()

class Checking(Account):

    type = "checking"

    def __init__(self,filepath,fee):
        Account.__init__(self,filepath)
        self.fee = fee

    def transfer(self,amount):
        self.balance = self.balance - amount - self.fee

jacks_check = Checking("jack.txt",10)
jacks_check.transfer(200)
print(jacks_check.balance)
jacks_check.commit()
print(jacks_check.type)

johnscheck = Checking("john.txt",10)
johnscheck.transfer(100)
print(johnscheck.balance)
johnscheck.commit()
print(johnscheck.type)
