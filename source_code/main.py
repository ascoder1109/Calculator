print("Welcome to Calculator!")


def again():
    onemore = input("Do you want to calculate again?(Select Yes/No):")
    if onemore == "Yes":
        calculate()
    elif onemore == "No":
        print("See You Later")
    else:
        again()


def calculate():
    print("Choose your operation:\n1.Addition\n2.Subtraction\n3.Multiplication\n4.Divide\n5.Modulus\n6.Exponent")
    choice = int(input())

    num1 = float(input("Please Enter your 1st number:"))
    num2 = float(input("Please Enter your 2nd number:"))
    if choice == 1:
        result = num1+num2
        print(str(num1)+"+"+str(num2)+"="+str(result))
    elif choice == 2:
        result = num1-num2
        print(str(num1)+"-"+str(num2)+"="+str(result))
    elif choice == 3:
        result = num1 * num2
        print(str(num1)+"*"+str(num2)+"="+str(result))
    elif choice == 4:
        result = num1 / num2
        print(str(num1)+"/"+str(num2)+"="+str(result))
    elif choice == 5:
        result = num1 % num2
        print(str(num1)+"%"+str(num2)+"="+str(result))
    elif choice == 6:
        result = num1 ** num2
        print(str(num1)+"^"+str(num2)+"="+str(result))
    else:
        print("Invalid Input!")
    again()


calculate()
