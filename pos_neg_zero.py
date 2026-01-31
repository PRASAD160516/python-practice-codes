array = [10,20,-40,-35,-34,0,12,0]

positive = 0
negative = 0
zero = 0

for num in array:
    if num > 0:
        positive = positive+1
    elif num < 0:
        negative = negative+1
    else:
        zero = zero+1
print("Positive number count karo =",positive)
print("Negative numbers count karo =",negative)
print("Zero wale numbers count karo =",zero)
        