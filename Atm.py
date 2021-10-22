class ATM:

    def __init__(self,c,p,b) :
       self.cardNumber = c
       self.pinCode = p
       self.Balance = b
   

    def showBalance(self)  :
        print(self.Balance)

    def withdraw(self) :
        a = int(input("THE AMOUNT YOU WANT TO WITHDRAW :"))
        self.Balance = self.Balance - a   
        print("BALANCE LEFT : ",self.Balance)

bank = ATM(1234,333,1000)
bank.showBalance()
bank.withdraw()
