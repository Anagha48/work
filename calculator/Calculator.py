num1 = int(input("ENTER TWO NUMBERS : "))
num2 = int(input())
while(True):
    print("\n____CALCULATOR____\n\nSELECT OPERATION:\n1.ADDITION\n2.SUBSTRACTION\n3.MULTIPLICATION\n4.DIVISION\n5.EXIT")
    choice = int(input("enter your choice (1/2/3/4/5) : "))
    if choice == 1:
        print("ADDITION = ",num1+num2)
    elif choice == 2:
        print("SUBSTRACTION = ",num1-num2)
    elif choice == 3:
        print("MULTIPLICATION = ",num1*num2)
    elif choice == 4 :
        print("DIVISION = ",num1/num2)
    elif choice == 5:
        print("exit")
        break
    else:
        print("invalid choice")