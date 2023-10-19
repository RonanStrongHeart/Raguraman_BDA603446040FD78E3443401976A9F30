

class bankAcc:
  #getting details from user
  def __init__(self):
    self.__accNum=int(input("Enter Your Account number: "))
    self.__accUser=str(input("Enter Your user name: "))
    self.__accbalance = 0
  
  #Deposition
  def deposit(self):
    Dmoney=int(input("Enter the amount to deposit: "))
    self.__accbalance+=Dmoney
    print("Your",Dmoney,"\bRs has been deposited successfully\n")
  
  #withdrawal
  def withdraw(self):
    Wmoney=int(input("Enter the amount to withdraw: "))
    print('\n')
    self.__accbalance-=Wmoney
  
  #display balace
  def displayBalance(self):
    print("Your account balance is",self.__accbalance,'\n')

b = bankAcc()

b.deposit()
b.withdraw()
b.displayBalance()

print("\nSayonera")

