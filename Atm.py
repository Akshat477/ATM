class ATM:

    def __init__(self,c,p,b) :
       self.cardNumber = c
       self.pinCode = p
       self.Balance = b
       b = input("HOW MUCH YOU WANT IN YOUR ACCOUNT")

    def showBalance(self)  :
        print(self.Balance)

    def withdraw(self,a) :
        a = input("THE AMOUNT YOU WANT TO WITHDRAW")
        self.Balance - a   

bank = ATM(1234,333,1000)