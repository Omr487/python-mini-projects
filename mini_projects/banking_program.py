def show_balance(balance):
    print("*****************************")
    print(f"your balance is ${balance:.2f}")
    print("*****************************")
def deposit():
    amount = float(input("Enter an amount to be deposited"))
    if amount <0:
        print("that's not a valid amount")
        return 0
    else:
        return amount
def withdraw(balance):
    amount = float(input("Enter amount to be withdrawn"))
    if amount >balance:
        print("insufficient funds")
    elif amount<0:
        print("Enter a valid amount")
    else:
        return amount
def main():
 balance = 0
 is_runing = True

 while is_runing :
      print("***********************")
      print("----Banking Program----")
      print("1.Show Balance")
      print("2.Deposit")
      print("3.Withdraw")
      print("4.Exit")
      choice = input("Enter you choice(1-4):")

      if choice == '1':
        show_balance(balance)
      elif choice =='2':
         balance += deposit()
      elif choice =='3':
        balance -= withdraw(balance)
      elif choice =='4':
        is_runing = False 
      else:
        print("*********************")
        print("enter valid choice:")
        print("*********************")
 print("************************")
 print("Thank you have nice day")
 print("************************")

if __name__ =='__main__':
   main()