import datetime
class bank:
    bank_name="SBI"

    def create_acct(self,acct_no,name,ph_no,balance):

        self.acct_no=acct_no
        self.name=name
        self.ph_no=ph_no
        self.balance=balance

    def deposit(self,amount):
        self.balance+=amount
        print("Your",bank.bank_name,"account with account number",self.acct_no,"is credited with RS",amount,"on",datetime.datetime.now(),"and your available balance is RS",self.balance)

    def withdrawal(self,amount):
        if amount>self.balance:
            print("insufficient amount")
        else:
            self.balance-=amount
            print("your debited amount is RS",amount,"and your aval balance is RS",self.balance)

obj=bank()
obj.create_acct(100,"amal",9876543210,50000)
obj.deposit(9000)
obj.withdrawal(1000)

