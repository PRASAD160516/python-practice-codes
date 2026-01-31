number = int(input("Enter a number ="))
sumdigit = 0

while(number > 0):
    digit = number%10
    sumdigit = sumdigit+digit
    number = number // 10

print("Sum of the digits of the number is:",sumdigit)