from enum import Enum

class AccountType(Enum) :
        CHECKING = 0
        SAVINGS = 1

class BankAccount :
    def __init__(self, balance = 0, accountType = AccountType.CHECKING):
        self.__accountType = accountType
        self.__balance = balance

	
    def getBalance(self) :
	    return self.__balance 
        
    def getAccountType(self) : #Cannot change account type
	    return self.__accountType
	
	#will have a deposit and withdraw methods instead to change balance
	
    def deposit(self, amount) :
        self.__balance += amount
	
    def withdraw(self, amount) :
        self.__balance -= amount