class BankAccount:
    bankName = "Turtle Bank"
    masterAccountList = []

    def __init__(self, intRate='1%', balance=0):
        self.intrestRate = BankAccount.convertPer2Dec(intRate)
        self.accountBalance = balance
        BankAccount.masterAccountList.append(self)

    def deposit(self, amount):
        self.accountBalance += amount
        return self

    def withdraw(self, amount):
        self.accountBalance -= amount
        return self

    def displayAccountInfo(self):
        print(f'Current balance is: {self.accountBalance}$')
        return self

    def yieldInterest(self):
        self.accountBalance += self.accountBalance * self.intrestRate
        return self

    @classmethod
    def sumOfAllAccounts(cls):
        sum = 0
        for x in cls.masterAccountList:
            sum += x.accountBalance
        print(sum)
        return sum

    @staticmethod
    def convertPer2Dec(percentage):
        temp = float(percentage.strip('%')) / 100.0
        return temp


jacob = BankAccount('1%', 300)

jacob.deposit(50).deposit(100).deposit(.50).withdraw(
    25).yieldInterest().displayAccountInfo()

will = BankAccount('2%', 500)

will.deposit(500).deposit(1000).withdraw(250).withdraw(
    50.50).yieldInterest().displayAccountInfo()


BankAccount.sumOfAllAccounts()
