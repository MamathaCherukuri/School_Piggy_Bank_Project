#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("Hello, Welcome to Foster school Piggy Bank")
print("")
print("Please begin with creating an account")
name=input("Enter your Name: ")
phone=input("Enter your Class: ")
address=input("Enter your Section: ")
code=input("Please enter a 4 digit pin to use as your passcode: ")

print()
print("Your account summary is:")
print("Name:" + name)
print("Phone Number:" + phone)     
print("Address:" + address)
print("Pin Code:" + code)    
print()
balance=float(input("Enter an amount to deposit into the account: "))
print()
print(name,", Thank you for creating an account.")
def printMenu():
    print()
    print("Please choose an option below:")
    print("""
    Enter b to Check your Balance
    Enter d to Deposit money into your Account
    Enter w to Withdraw money from your Account
    Enter q to Quit the Program """)
    print("")

def getTransaction():
    transaction=str(input("What would you like to do? "))
    return transaction

def withdraw(bal,amt):
    global balance
    balance=bal-amt
    if balance<0:
        balance=balance-10

def formatCurrency(amt):
    return "$%.2f" %amt

###MAIN PROGRAM###

printMenu()
command=str(getTransaction())

while command!="q":
    if (command=="b"):
        print(name,"Your current balance is",formatCurrency(balance))
        printMenu()
        command=str(getTransaction())
    elif (command=="d"):
        amount=float(input("Amount to deposit? "))
        balance=balance+amount
        printMenu()
        command=str(getTransaction())
    elif (command=="w"):
        amount=float(input("Amount to withdraw? "))
        withdraw(balance,amount)
        printMenu()
        command=str(getTransaction())
    else:
        print("Incorrect command. Please try again.")
        printMenu()
        command=str(getTransaction())

print(name,"Goodbye! See you again soon")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




