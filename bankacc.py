class Bank:
    def __init__(self,accno,name,acctype,balance=0):       
        self.acc=accno
        self.na=name
        self.acctype=acctype
        self.bal=balance
    def deposit(self,amount):
      if amount>0:
         self.bal+=amount
         print(f"deposit successfull new{self.bal}")
      else:
         print("invalid pleace enter positive value")
    def withdraw(self,amount):
      if amount>0:
         if amount<=self.bal:
            self.bal-=amount
            print(f"withdraw succ new bala{self.bal}")
         else:
                 print("insuf balance")
                                
      else:
            print("Invalid withdrawal amount. Please enter a positive value.")
    def display (self):
        print(f"\n Account Number: {self.acc} \n Account Holder Name: {self.na}")
        print(f" Account Type: {self.acctype} \n Balance: {self.bal}")
        print("\n*** Menu ***")
        print("1. Deposit \n 2. Withdraw\n 3. Display \n 4. Exit ")
b1 = Bank(1002,"anjupar", "Savings", 0)   
b1.display()
while True:	
    choice = int(input("\nEnter your choice (1-4): "))
    if choice == 1:
        d = int(input("Enter amount to be deposited: "))
        b1.deposit(d)
    elif choice == 2:
        w = int(input("Enter amount to withdraw: "))
        b1.withdraw(w)
    elif choice == 3:
        b1.display()
    elif choice == 4:
        print("Exiting... Thank you!")
        break
    else:
        print("Enter a valid choice.")
