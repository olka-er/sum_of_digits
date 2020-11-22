#Program sums the digits in number entered by user
import sys
def Digits(digits):
   
    num=str(digits)

    numlist=[]
    i=0
    while i<len(num):
        numlist.append(num[i:1+i])
        i+=1

    i=0
    numlist1=[]
    while i < len(num):
        numlist1.append(int(numlist[i]))
        i+=1

    summ=sum(numlist1)

    return summ

print("Hello! This program will sum up all digits in number given by user")
digits=input("Please enter your number here: ")
print("Sum of all digits in given number is: ", Digits(digits))
