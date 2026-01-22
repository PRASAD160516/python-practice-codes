while(True):
    print("\n ----SIMPLE CALCULATOR----")
    print("1. Addition.")
    print("2. Substraction.")
    print("3. Multiplication.")
    print("4. Division.")
    print("5. Exit.")

    select = int(input("Please aap in 5 number mai se kuch select kijiye:"))
    if(select==5):
       print("Exit from the calculator:")
       break

    num1 = int(input("Enter your first number="))
    num2 = int(input("Enter your second number="))
    if(select==1):
       print("Result=",num1+num2)
    elif(select==2):
       print("Result=",num1-num2)
    elif(select==3):
       print("Result=",num1*num2)
    elif(select==4):
       print("Result=",num1/num2)
    else:
       print("Invalid apne jo number select kiya woo process apke calculator mai nahi hai, sorry.")
