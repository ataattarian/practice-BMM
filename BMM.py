def Bmm(firstNum, secondNum):
    if firstNum > secondNum:    
        while(secondNum):       
            firstNum, secondNum = secondNum, firstNum % secondNum
        return firstNum
    else:
        while(firstNum):
            secondNum , firstNum = firstNum , secondNum % firstNum
        return secondNum

num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))
print(Bmm(num1, num2))