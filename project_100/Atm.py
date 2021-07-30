class Atm(object):
    def __init__(self,pinnumber,cardnumber,withdrawl,balance,deducted):
        self.pinnumber = pinnumber
        self.cardnumber = cardnumber
        self.withdrawl = withdrawl
        self.balance = balance
        self.deducted = deducted

    def CashWithdrawl (self,withdrawlmoney):      
        print("Cash With withdrawl : " + withdrawlmoney)

    def BalanceEnquiry (self,balance) :
        print("The total Balance of the Account is :"+ balance)

    def DeductedAmount (self,deducted) :
        print("DeductedAmount is : " + deducted)



atm = Atm("Pin number : 5414", "card number : kaowd2121","$1000" ,"$100000", "$99000" )
print(atm.pinnumber)
print(atm.cardnumber)
atm.CashWithdrawl("$1000")
atm.BalanceEnquiry("$100000")  
atm.DeductedAmount("$99000") 