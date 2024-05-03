class BankAccount :
    def __init__(self , account_number) :
        self.account_number = str(account_number)
        self.balance = 0 
    
    def withdraw(self, amount) :
        if self.balance >= amount :
            self.balance -= amount
        else :
            raise ValueError("Insuffient Funds")
    
    def deposit(self, amount) :  
        self.balance += amount
    
    def get_balance(self) :
        return self.balance
        
def transfer_amount( account1 , account2 , amount ) :
    try :
        account1.withdraw( amount )
        account2.deposit( amount )
        return True 
    except ValueError as err : 
        print( str(err) )
        return False 

sender = BankAccount("001")
receiver = BankAccount("002")

sender.deposit( int(input()) )
receiver.deposit( int(input()) )

print("User 1 Balance: {}/-".format(sender.get_balance()) ) 
print("User 2 Balance: {}/-".format(receiver.get_balance()) ) 
print("")

transfer_amount( sender , receiver ,  int(input())  )  # here input  is the amount sender want to transfer to receiver

print("Transfering Money from User-1 to User-2")
print("")
print("User 1 Balance: {}/-".format(sender.get_balance()) ) 
print("User 2 Balance: {}/-".format(receiver.get_balance()) )
